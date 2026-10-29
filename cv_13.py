import cv2

video = cv2.VideoCapture("C:/Users/Deepak/PycharmProjects/OPENCV/images/nature.mp4")

if not video.isOpened():
    print("Video not found. Check the file path.")
    exit()

while True:
    ret, frame = video.read()

    if not ret:
        break

    frame = cv2.resize(frame, (500, 720))
    cv2.imshow("Output", frame)

    if cv2.waitKey(25) & 0xFF == ord("q"):
        break

video.release()
cv2.destroyAllWindows()