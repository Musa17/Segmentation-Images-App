import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load image
image = cv2.imread('Pikachu.jpg')

# Converting images to grayscale
image_gray_original = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image_gray_segmented = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)



# Show original grayscale image
cv2.namedWindow('Original gray image')
cv2.imshow('Original gray image', image_gray_original)

# Show segmented grayscale image
cv2.namedWindow('Segmented gray image')
cv2.imshow('Segmented gray image', image_gray_segmented)

cv2.waitKey(0)
cv2.destroyAllWindows()
