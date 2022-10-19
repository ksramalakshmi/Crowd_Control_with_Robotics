import cv2

vid1 = cv2.VideoCapture(0)
vid2 = cv2.VideoCapture(1)

while(True):
    
    cv2.namedWindow("output1", cv2.WINDOW_NORMAL)    
    cv2.namedWindow("output2", cv2.WINDOW_NORMAL)    

    ret1, frame1 = vid1.read()
    ret2, frame2 = vid2.read()

    frame3 = cv2.resize(frame1, (640, 480))
    frame4 = cv2.resize(frame2, (640, 480))

    final = cv2.hconcat([frame3, frame4])
    cv2.imshow('output', final)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
vid1.release()
vid2.release()
cv2.destroyAllWindows()