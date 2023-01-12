import cv2
from PIL import Image

img=cv2.imread('src\imgs\\templates\\aadharFront.jpg');
cv2.imshow('Original', img)
cv2.waitKey(0)

# bnwImg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY);
# cv2.imshow('GRAY IMG',bnwImg);
# cv2.waitKey(0)