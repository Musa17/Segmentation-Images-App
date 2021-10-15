import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load image
image = cv2.imread('Pikachu.jpg')

# Converting images to grayscale
image_gray_original = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image_gray_segmented = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

retci = image_gray_segmented.shape[0]
stupci = image_gray_segmented.shape[1]

# Pixel transformations - Segmenting image
for i in range(0, retci):
	for j in range(0, stupci):
		if (image_gray_segmented[i, j] >= 0 and image_gray_segmented[i, j] <= 85):
			image_gray_segmented[i, j] = 0
		elif (image_gray_segmented[i, j] >= 86 and image_gray_segmented[i, j] <= 171):
			image_gray_segmented[i, j] = 128
		else:
			image_gray_segmented[i, j] = 255


# Show original grayscale image
cv2.namedWindow('Original gray image')
cv2.imshow('Original gray image', image_gray_original)

# Show segmented grayscale image
cv2.namedWindow('Segmented gray image')
cv2.imshow('Segmented gray image', image_gray_segmented)

cv2.waitKey(0)
cv2.destroyAllWindows()
