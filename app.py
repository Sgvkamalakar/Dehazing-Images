from flask import *
import os
import cv2
import numpy as np


UPLOADS_FOLDER = 'static/uploads'
DEHAZED_FOLDER = 'static/dehazed'

app = Flask(__name__)
app.secret_key = '9ae52ad014c879078f798507be8ac651' 

@app.route('/')  
def upload():  
    return render_template("index.html") 

@app.route('/info')
def info():
    return render_template('info.html')

def dehaze_image(image, omega=0.78, t0=0.01):
    dark_channel = cv2.ximgproc.createFastGlobalSmootherFilter(image, 10, 0.05)
    dark_channel = dark_channel.filter(image)
    atmospheric_light = np.percentile(image, 90, axis=(0, 1))
    transmission = 1 - omega * dark_channel / atmospheric_light
    transmission[transmission < t0] = t0
    dehazed_channels = []
    for i in range(3):
        dehazed_channel = ((image[:, :, i].astype(np.float32) - atmospheric_light[i]) / transmission[:, :, 0]) + atmospheric_light[i]
        dehazed_channels.append(dehazed_channel)
    dehazed_image = np.stack(dehazed_channels, axis=-1)
    dehazed_image = np.clip(dehazed_image, 0, 255).astype(np.uint8)
    return dehazed_image 

@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        f = request.files['file']
        if f.filename == '':
            return render_template("index.html",error="No file selected. Please choose a file to upload.")
        original_image_path = os.path.join(UPLOADS_FOLDER, f.filename)
        f.save(original_image_path)
        x = cv2.imread(original_image_path)
        dehazed_image = dehaze_image(x)
        name='dehazed_'+f.filename
        dehazed_image_path = os.path.join(DEHAZED_FOLDER,name)
        cv2.imwrite(dehazed_image_path, dehazed_image)
        return render_template("result.html", original_image=original_image_path, dehazed_image=dehazed_image_path)
  
if __name__ == '__main__':  
    app.run(debug = True)  