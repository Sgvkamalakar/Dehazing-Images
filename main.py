import gradio as gr
import cv2
import numpy as np
import pandas as pd

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

iface = gr.Interface(fn=dehaze_image,inputs="image",outputs="image",live=True,title="Image Dehazing App",
                     description="Dehazing is a process of enhancing the visibility and clarity of an image that has been degraded due to the presence of haze or fog. It is a crucial task in computer vision and image processing, especially for applications like autonomous driving, surveillance, and remote sensing.",
                     inputs_kwargs={"type": "file", "label": "Upload an Image"},
                     live_button="Dehaze")

if __name__ == "__main__":
    iface.launch()
