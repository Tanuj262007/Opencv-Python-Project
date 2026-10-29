import cv2

img =cv2.imread("C:/Users/Deepak/PycharmProjects/OPENCV/images/highway.jpeg")
print("Dimension of Original Image: ", img.shape)
scale=100
width=int(img.shape[1] *scale /100)
height=int(img.shape[0] *scale /100)
dim=(width,height)
resized=cv2.resize(img,dim ,interpolation = cv2.INTER_LINEAR)
print("Dimension of Resized Image: ", resized.shape)

cv2.imshow("Resized Image",resized)
cv2.imshow("Original Image",resized)

cv2.waitKey(0)
cv2.destroyAllWindows()