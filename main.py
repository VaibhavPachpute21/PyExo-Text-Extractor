import pytesseract
import os
from PIL import Image
import cv2
from src import AdharCard

abc=AdharCard.sum(2,4)
print(abc)

# img = cv2.imread('download.png')
# print(pytesseract.__version__)
# print(pytesseract.image_to_string(img))