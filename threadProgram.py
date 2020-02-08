import cv2
import numpy as np
import pyautogui
import threading
import time

def initThreads():
    ##
    ##
    threadRecordWebcam = threading.Thread(target=recordScreen)
    threadRecordWebcam.start()


def recordScreen():
    i=0
    while(True):
        time.sleep(1)
        if i==10:
            break
        print('hello')
        i+=1
'''
# display screen resolution, get it from your OS settings
SCREEN_SIZE = (1920, 1080)
# define the codec
fourcc = cv2.VideoWriter_fourcc(*"XVID")
# create the video write object
out = cv2.VideoWriter("ScreenRecord.avi", fourcc, 20.0, (SCREEN_SIZE))

while True:
    # make a screenshot
    img = pyautogui.screenshot()
    # convert these pixels to a proper numpy array to work with OpenCV
    frame = np.array(img)
    # convert colors from BGR to RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # write the frame
    out.write(frame)
    # show the frame
    cv2.imshow("screenshot", frame)
    # if the user clicks q, it exits
    if cv2.waitKey(1) == ord("q"):
        break

# make sure everything is closed when exited
cv2.destroyAllWindows()
out.release()

img = pyautogui.screenshot(region=(0, 0, 300, 400))
'''
def main():
    initThreads()
    print('hey')

if __name__ == "__main__":
    main()
    
