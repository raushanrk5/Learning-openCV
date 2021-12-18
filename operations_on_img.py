import cv2 as cv
import numpy as np

img = cv.imread('messi.jpg')
print(img.shape)
print(img.size)
print(img.dtype)
b,g,r = cv.split(img)
img = cv.merge((b,g,r))
res_img = cv.resize(img, (740,411))
 
cv.imshow('img', img)
cv.imshow('res_img', res_img)

img1 = cv.imread('test2.jpeg')
img2 = cv.imread('test3.jpg')

img1 = cv.resize(img1, (512,512))
img2 = cv.resize(img2, (512,512))

#res = cv.add(img1,img2)

res = cv.addWeighted(img1, .7, img2, .1, 3)

cv.imshow('res', res)

cv.waitKey(0)
cv.destroyAllWindows()