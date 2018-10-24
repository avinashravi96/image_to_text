import cv2
import pytesseract
from matplotlib import pyplot as plt
filename = 'image.jpeg'

# read the image and get the dimensions
img = cv2.imread(filename)
h, w, _ = img.shape # assumes color image
boxes = pytesseract.image_to_boxes(img)
for b in boxes.splitlines():
    b = b.split(' ')
    img = cv2.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)
plt.imshow(img)
