import gradio as gr
from dehazer import dehaze_image

iface = gr.Interface(fn=dehaze_image,inputs="image",outputs="image",live=True,title="Image Dehazing App",
                     description="Dehazing is a process of enhancing the visibility and clarity of an image that has been degraded due to the presence of haze or fog. It is a crucial task in computer vision and image processing, especially for applications like autonomous driving, surveillance, and remote sensing.",
                     inputs_kwargs={"type": "file", "label": "Upload an Image"},
                     live_button="Dehaze")

if __name__ == "__main__":
    iface.launch()
