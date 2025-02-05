import pyautogui
import cv2
import numpy as np

reso = (1920, 1080)
codec = cv2.VideoWriter_fourcc(*"CLCO")
file = "Recording.mp4"
fps = 70.0
out = cv2.VideoWriter(file, codec, fps, reso)
cv2.namedWindow("Video", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Video", 500, 400)

while True:
 img = pyautogui.screenshot()
 frame = np.array(img)
 frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
 out.write(frame)
 cv2.imshow('Video', frame)
 if cv2.waitKey(1) == ord('q'):
    break

print("Screen Recording started")
out.release()
cv2.destroyAllWindows()