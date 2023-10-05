# Image De-hazing/De-smoking


Dehazing is a process of enhancing the visibility and clarity of an image that has been degraded due to the presence of haze or fog. It is a crucial task in computer vision and image processing, especially for applications like autonomous driving, surveillance, and remote sensing.

![image](https://github.com/Sgvkamalakar/Dehazing-Images/assets/103712713/d272cf85-efe9-48fb-86fc-b4a056d76ca0)



## Dehazing Process:

1. **Dark Channel Prior:** One of the key insights in dehazing is the dark channel prior. It states that in most outdoor images, there exists a local dark channel that contains very low-intensity values for the majority of image regions. This dark channel represents the scene's haziness and is used as a basis for estimating the haze thickness.

2. **Atmospheric Light Estimation:** The atmospheric light represents the light that directly reaches the camera without being scattered by haze. It is usually estimated from the brightest pixels in the dark channel.

3. **Transmission Map:** The transmission map describes the fraction of light that has been attenuated or scattered due to the haze. It is calculated using the dark channel and the estimated atmospheric light. The transmission map helps in understanding how much the scene's details have been obscured by haze.

4. **Dehazing:** With the atmospheric light and transmission map, the dehazing process involves recovering the original scene radiance by dividing the observed image by the transmission map and adding back the atmospheric light. This step restores image clarity and reduces the effects of haze.

## Working of the Code:

The provided Python code is an implementation of a dehazing algorithm. Here's how it works:

1. **Input Image:** The code takes an input hazy image as an input.

2. **Dark Channel Prior:** It calculates the dark channel of the input image. The dark channel represents the haziness in the image.

3. **Atmospheric Light Estimation:** The code estimates the atmospheric light by finding the top percentile (e.g., 90th percentile) of pixel values in the input image. This represents the brightest part of the image not affected by haze.

4. **Transmission Map Calculation:** Using the dark channel and atmospheric light, the code calculates the transmission map. This map indicates the degree of haze in different parts of the image.

5. **Dehazing:** The dehazing process involves dividing each color channel of the input image by the transmission map and then adding back the atmospheric light. This operation enhances the image clarity by removing the haze.

6. **Output Image:** The code returns the dehazed image, where the majority of the haze has been removed, leading to improved visibility and detail.

This dehazing code is based on the dark channel prior principle and can significantly improve the quality of hazy images, making them suitable for various computer vision applications.

## Web Application Structure

- `main.py`: Contains the code for the web interface using the Gradio framework.
- `app.py`, `templates`, and `static` folders: Together, these components make up the Flask-based web application for additional functionality, styling and presentation.


# Sample Results

![image](https://github.com/Sgvkamalakar/Dehazing-Images/assets/103712713/e0597485-23ed-4757-be4d-954761d543d5)

![image](https://github.com/Sgvkamalakar/Dehazing-Images/assets/103712713/12c59847-31ef-45cc-8808-9e3ae3090669)

![image](https://github.com/Sgvkamalakar/Dehazing-Images/assets/103712713/4b33f898-26f2-4535-a98c-a4547e846d67)

![image](https://github.com/Sgvkamalakar/Dehazing-Images/assets/103712713/e46f5d51-0f4c-43a9-8ff5-e7bd7dac8fb2)

![image](https://github.com/Sgvkamalakar/Dehazing-Images/assets/103712713/a5999baa-fe10-4926-884a-3f149e60f8c7)

![image](https://github.com/Sgvkamalakar/Dehazing-Images/assets/103712713/98a0ecd4-d03f-4b4d-a3c7-bfb776563db4)






