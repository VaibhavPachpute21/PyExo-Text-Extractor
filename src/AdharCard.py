import pytesseract

def AdharCard(img):
   return pytesseract.image_to_string(img, lang="eng")
