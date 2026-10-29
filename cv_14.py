import cv2

video =cv2.VideoCapture("C:/Users/Deepak/PycharmProjects/OPENCV/images/flower.mp4" )

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output =cv2.VideoWriter("Output.mp4", fourcc,120.00, (1080,1920) )

while video.isOpened():
    ret, frame = video.read()
    if ret:
        output.write(frame)
        cv2.imshow("Frame",frame)

        if cv2.waitKey(10) & 0xFF == ord('s'):
           break
    else:
        break

cv2.destroyAllWindows()
