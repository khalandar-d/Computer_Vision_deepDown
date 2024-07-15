import cv2
import matplotlib.pyplot as plt
import os
print(os.getcwd())

# Load an image
image = cv2.imread('sample_data/0000000089.png')

# Convert BGR (default in OpenCV) to RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Convert RGB to HSV
image_hsv = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2HSV)

# Convert RGB to Lab
image_lab = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2Lab)

# Convert RGB to YUV
image_yuv = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2YUV)

# Display the images
plt.figure(figsize=(10, 10))

plt.subplot(2, 2, 1)
plt.imshow(image_rgb)
plt.title('RGB')

plt.subplot(2, 2, 2)
plt.imshow(image_hsv)
plt.title('HSV')

plt.subplot(2, 2, 3)
plt.imshow(image_lab)
plt.title('Lab')

plt.subplot(2, 2, 4)
plt.imshow(image_yuv)
plt.title('YUV')

plt.show()

