import cv2

# img = cv2.VideoCapture(0)
#
# while True:
#     ret, frame = img.read()
#     cv2.imshow('frame', frame)
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# img.release()
# cv2.destroyAllWindows()

img = cv2.imread("test2.jpeg", 1)
print(img)

cv2.imshow('image', img)

k = cv2.waitKey(0)

if(k==27):
    cv2.destroyAllWindows()
    
elif(k==ord('s')):
    cv2.imwrite('writeimg.png', img)
    cv2.destroyAllWindows()
