import cv2

capture = cv2.VideoCapture(0)
cascade = cv2.CascadeClassifier("haarcascade_fullbody.xml")

while True:
    _, image = capture.read()
    im_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(im_gray)
    for x,y, width, height in faces:
        cv2.rectangle(image, (x,y), (x + width, y + height), color=(0, 0, 255), thickness=5)
    cv2.imshow("Cam", image)
    if cv2.waitKey(1) == ord("q"):
        break

capture.release()
cv2.destroyAllWindows()