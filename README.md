# Image De-hazing/De-smoking


Dehazing is a process of enhancing the visibility and clarity of an image that has been degraded due to the presence of haze or fog. It is a crucial task in computer vision and image processing, especially for applications like autonomous driving, surveillance, and remote sensing.

![Image](https://github.com/Sgvkamalakar/Dehazing-Images/assets/103712713/87e90554-6a63-4e18-ba7c-2a799e48ffa0)


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

