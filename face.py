import cv2  # importing OpenCV library

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) #in this line webcam is taken
face_cascade = cv2.CascadeClassifier("face.xml") #here xml file is defined

# need a while true loop to get whole frames from webcam
while True:
    ret,frame = cap.read()
    frame = cv2.flip(frame,1) # in this line frame is flipped
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #here, frame is transformed to the gray frame

    faces = face_cascade.detectMultiScale(gray,1.2,15) #by this function, face is detected on frame.

    if len(faces) == 1:  # this if condition checks whether faces have value or not
        for (x,y,w,h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255))  #a rectangle is drawn around face in frame
            cv2.putText(frame, "Please Wear a Mask", (150, 50), cv2.FONT_HERSHEY_SIMPLEX, 1,(0, 0, 255), 2, cv2.LINE_AA)
    else:
        cv2.putText(frame, "Thanks for wearing Mask", (150, 50), cv2.FONT_HERSHEY_SIMPLEX, 1,(0, 255, 0), 2, cv2.LINE_AA)

    cv2.imshow("Frame",frame) #Frame is showed

    if cv2.waitKey(1) & 0xFF ==ord("q"):
        break

cap.release()
cv2.destroyAllWindows()