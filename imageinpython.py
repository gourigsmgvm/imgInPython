import cv2

img = cv2.imread("C:/Users/gopui/OneDrive/Pictures/cat.jfif")
print(img)
cv2.imshow("cat", img)
grayimg = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
print(grayimg)
cv2.imshow("grayimg", grayimg)
