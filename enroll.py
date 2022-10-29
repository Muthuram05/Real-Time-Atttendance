import cv2

cap = cv2.VideoCapture(0) # video capture source camera (Here webcam of laptop)
ret,frame = cap.read() # return a single frame in variable `frame`

while(True):
    cv2.imshow('img1',frame) #display the captured image
    if cv2.waitKey(0) & 0xFF == ord('y'): #save on pressing 'y'
        name = input("enter your name:")
        cv2.imwrite(f'student_images/{name}.png',frame)
        cv2.destroyAllWindows()
        break

cap.release()