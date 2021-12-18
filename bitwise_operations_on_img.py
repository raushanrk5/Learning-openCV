import cv2 as cv
import numpy as np

img = np.zeros((540,460,3),np.uint8)
img = cv.circle(img, (225,285), 90, (255,255,255), -1)
cv.imshow('img', img)

img2 = cv.imread('black&white.png')
img2 = cv.resize(img2,(460,540))
cv.imshow('img2',img2)

and_img = cv.bitwise_and(img2, img)
cv.imshow('and_img', and_img)

or_img  = cv.bitwise_or(img,img2)
cv.imshow('or_img', or_img)

xor_img = cv.bitwise_xor(img, img2)
cv.imshow('xor_img', xor_img)

not_img1 = cv.bitwise_not(img)
not_img2 = cv.bitwise_not(img2)

cv.imshow('not_img1',not_img1)
cv.imshow('not_img2',not_img2)


cv.waitKey(0)
cv.destroyAllWindows()