import time
import sys
import RPi.GPIO as GPIO

from datetime import datetime
from picamera import PiCamera
from time import sleep
import picamera

import cv2
num_down = 2       # number of downsampling steps
num_bilateral = 7  # number of bilateral filtering steps
 


camera = PiCamera()

GPIO.setmode(GPIO.BCM)

fairyAC = 14
button = 9
led3 = 22
led2 = 27
led1 = 17


GPIO.setup(button, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(led3,GPIO.OUT)
GPIO.setup(led2,GPIO.OUT)
GPIO.setup(led1,GPIO.OUT)
GPIO.setup(fairyAC,GPIO.OUT)


GPIO.output(led3, 0)
GPIO.output(led2, 0)
GPIO.output(led1, 0)
GPIO.output(fairyAC, 0)

def lights(): # LED lights blinking before taking a photo
    GPIO.output(fairyAC,1)
    GPIO.output(led3,1)
    GPIO.output(led2,1)
    GPIO.output(led1,1)
    time.sleep(1)
    GPIO.output(led3,0)
    GPIO.output(led2,1)
    GPIO.output(led1,1)
    time.sleep(1)
    GPIO.output(led3,0)
    GPIO.output(led2,0)
    GPIO.output(led1,1)
    time.sleep(0.2)
    GPIO.output(led1,0)
    time.sleep(0.2)
    GPIO.output(led1,1)
    time.sleep(0.2)
    GPIO.output(led1,0)
    time.sleep(0.2)
    GPIO.output(led1,1)
    time.sleep(0.2)
    GPIO.output(led1,0)
    time.sleep(0.2)
    GPIO.output(led1,1)
    time.sleep(0.2)
  

while True:
           if(GPIO.input(button)):
                                  lights()
                                  datestr = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                                  camera.rotation = 180 
                                  camera.iso = 200 
                                  imgName="/home/pi/capture/image" + datestr + ".jpg"
                                  camera.capture(imgName)
                                  img_rgb = cv2.imread(imgName) # cartoonise the image
                                  img_color = img_rgb
                                  for _ in range(num_down):
                                      img_color = cv2.pyrDown(img_color)
                                  for _ in range(num_bilateral):
                                     img_color = cv2.bilateralFilter(img_color,d=9,sigmaColor=9,sigmaSpace=7)

                                  for _ in range(num_down):
                                    img_color = cv2.pyrUp(img_color)

                                  width=img_rgb.shape[1]
                                  height=img_rgb.shape[0]
                                  img_color = cv2.resize(img_color, (width, height))

                                  img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
                                  img_blur = cv2.medianBlur(img_gray, 7)

                                  img_edge = cv2.adaptiveThreshold(img_blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,blockSize=9,C=2)                                  
                                  img_edge = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2RGB)
                                  img_cartoon = cv2.bitwise_and(img_color, img_edge) 
                                  imgName="/home/pi/capture/Cimage" + datestr + ".jpg"
                                  cv2.imwrite(imgName,img_cartoon) 
                                  print("done")
                                  sleep (2)
                                  GPIO.output(led1,0)
                                  GPIO.output(fairyAC,0)
                                  photostr= imgName
                                  photo_path = photostr

                                  sleep (10)
##                                  
##                                
                                   
           
           else:                     
                print(":(")
                sleep(5)
