import cv

cv.NamedWindow("RGB", cv.CV_WINDOW_AUTOSIZE)
cv.NamedWindow("HSV", cv.CV_WINDOW_AUTOSIZE)
camera_index = 0
capture = cv.CaptureFromCAM(camera_index)

def repeat():
  global capture #declare as globals since we are assigning to them now
  global camera_index
  frame = cv.QueryFrame(capture)
  frame2 = frame
  cv.Circle(frame, (20,20), 10, [1,1,1], thickness=1, lineType=8, shift=0)
#  cv.cvCvtColor(frame ,frame2, CV_RGB2HSV)
  cv.ShowImage("w1", frame)
  cv.ShowImage("w2", frame2)
  
  c = cv.WaitKey(100)
  
  if(c=="n"): #in "n" key is pressed while the popup window is in focus
    camera_index += 1 #try the next camera index
    capture = cv.CaptureFromCAM(camera_index)
    if not capture: #if the next camera index didn't work, reset to 0.
        camera_index = 0
        capture = cv.CaptureFromCAM(camera_index)
  return c

while True:
    repeat()

