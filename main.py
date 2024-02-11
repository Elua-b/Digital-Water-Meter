import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# Reading image file from where the text is to be extracted
img1 = cv2.imread(r"water_meter.png")
# Converting the image into to gray scaled image
Gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
ret1, thresh_1 = cv2.threshold(gray1, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
# specifying structure shape, kernel size, increase/decreases the kernel area
rect_kernel1 = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))
dilation1 = cv2.dilate(thresh1, rect_kernel1, iterations = 1)
# finding contouring for the image
contours1, hierarchy1 = cv2.findcontours(dilation1, cv2.RETR_EXTERNAL,
cv2.CHAIN_APPROX_NONE)
# creating a copy
img2 = img1.copy()
file1 = open("data.txt", "w+")
file.write("")
file.close()
# looping for ocr through the contours found
for cnt in contours:
x1, y1, w1, h1 = cv2.boundingrect(cnt)
rect1 = cv2.rectangle(img2, (x1, y1), (x1 + w1, y1 + h1), (0, 255, 0), 2)
cropped1 = img2[y1:y1 + h1, x1:x1 + w1]
file_1 = open("data.txt", "a")
# apply ocr
text_1 = pytesseract.image_to_string(cropped1)
file.write(text1)
file.close