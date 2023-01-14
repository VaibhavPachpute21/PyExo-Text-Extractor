import pytesseract
import cv2
import os
import re
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
os.environ['TESSDATA_PREFIX'] = 'C:\Program Files\Tesseract-OCR\\tessdata'

target_img=cv2.imread('./src/test/adhar5.jpg')
template_img = cv2.imread('./src/imgs/templates/aadharFront.jpg')


sift = cv2.xfeatures2d.SIFT_create()
template_gray = cv2.cvtColor(template_img, cv2.COLOR_BGR2GRAY)
template_kp, template_des = sift.detectAndCompute(template_gray, None)

target_gray = cv2.cvtColor(target_img, cv2.COLOR_BGR2GRAY)
target_kp, target_des = sift.detectAndCompute(target_gray, None)

FLANN_INDEX_KDTREE = 0
MIN_MATCH_COUNT = 100
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
search_params = dict(checks = 50)
flann = cv2.FlannBasedMatcher(index_params, search_params)
matches = flann.knnMatch(template_des, target_des, k=2)

good = []

for m,n in matches:
    if m.distance < 0.7*n.distance:
        good.append(m)
if len(good)>MIN_MATCH_COUNT:
    src_pts = np.float32([ template_kp[m.queryIdx].pt for m in good ]).reshape(-1,1,2)
    dst_pts = np.float32([ target_kp[m.trainIdx].pt for m in good ]).reshape(-1,1,2)
    M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC,5.0)
    matchesMask = mask.ravel().tolist()
    h,w,d = template_img.shape
    pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
    dst = cv2.perspectiveTransform(pts,M)
    target_img = cv2.polylines(target_img,[np.int32(dst)],True,255,3, cv2.LINE_AA)
else:
    print("Not enough matches are found - %d/%d" % (len(good),MIN_MATCH_COUNT))


text = pytesseract.image_to_string(target_img, lang='eng')
print(text)

""" 
image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Driving",image)
cv2.waitKey(0)

text=pytesseract.image_to_string(image,lang='eng+hin+mar')

print(str(text).replace('\t','').replace('\n\n','\n'))
# match=re.search(r'^[A-Z]{5}[0-9]{4}[A-Z]$',str(text)).group(0)
# print(match)



# if str(text).__contains__('Permanent Account Number'):
#     PanNO=str(text).split('Number')[1].split('\n')[1]
#     filePath = os.getcwd()+'\\src\\extracts\\%s_pan.txt'%PanNO
#     with open(filePath, "w", encoding="utf-8") as file:
#             file.write(str(text).replace('\t','').replace('\n\n','\n'))
# else:
#     print("didn't found") """