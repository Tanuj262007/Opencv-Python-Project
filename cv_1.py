import cv2

img = cv2.imread("C:/Users/Deepak/PycharmProjects/OPENCV/images/highway.jpeg" )
print("Dimensions of image: ", img.shape)
width=400
height=400
dim=(width,height)
resized = cv2.resize(img, dim)


if img is None:
    print("Image not found or could not be loaded")
else:

    cv2.imshow("Window", resized)
    cv2.imwrite("C:/Users/Deepak/PycharmProjects/OPENCV/images/car.jpeg" , img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
