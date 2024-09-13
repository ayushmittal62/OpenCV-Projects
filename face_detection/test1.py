import cv2
def face_detection():
 while True:
    ret, video_data = video_cap.read()
    col = cv2.cvtColor(video_data,cv2.COLOR_BGR2GRAY)
    face = face_cap.detectMultiScale(
        col,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    for (x, y, w, h) in face:
        cv2.rectangle(video_data, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.imshow("video_live", video_data)
    if cv2.waitKey(30) == ord(" "):
        video_cap.release()
        break

while(1):
 print("Enter your choice:")
 print("1.Face\n 2.Eye\n 3.Upperbody\n 4.Lowerbody\n 5.EXIT")
 x = int(input("Enter your choice: "))
 match x:
    case 2:
        print("you choose Eye Detection:")
        face_cap = cv2.CascadeClassifier("C:/Users/AYush Mittal/AppData/Local/Programs/Python/Python311/Lib/site-packages/cv2/data/haarcascade_righteye_2splits.xml")
        video_cap = cv2.VideoCapture(0)
        face_detection()
    case 1:
      print("You choose face detection:")
      face_cap = cv2.CascadeClassifier("C:/Users/AYush Mittal/AppData/Local/Programs/Python/Python311/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")
      video_cap = cv2.VideoCapture(0)
      face_detection()

    case 3:
       print("You Choose Upperbody:")
       face_cap = cv2.CascadeClassifier("C:/Users/AYush Mittal/AppData/Local/Programs/Python/Python311/Lib/site-packages/cv2/data/haarcascade_upperbody.xml")
       video_cap = cv2.VideoCapture(0)
       face_detection()

    case 4:
       print("You Choose lowerbody:")
       face_cap = cv2.CascadeClassifier("C:/Users/AYush Mittal/AppData/Local/Programs/Python/Python311/Lib/site-packages/cv2/data/haarcascade_lowerbody.xml")
       video_cap = cv2.VideoCapture(0)
       face_detection()

          
    case 5:
       exit(0)


print("hello world")


