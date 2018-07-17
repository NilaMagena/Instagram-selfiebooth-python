import time
import sys
import os

from datetime import datetime
from time import sleep

from InstagramAPI import InstagramAPI

while True:
     
     from InstagramAPI import InstagramAPI
     InstagramAPI = InstagramAPI (" ", " ") # username and password
     InstagramAPI.login()  # login
     sourcepath="/home/pi/capture"
     destpath="/home/pi/uploaded"
     filelist=os.listdir(sourcepath)
     for file in filelist:
         imagename = sourcepath + "/" + file
         imagename2 = destpath + "/" + file
         caption = "Ridiculously Simple to Hack #makered #sciencecentresg #caltexfys18"
         caption = "Ridiculously Simple to Hack #makered #sciencecentresg #caltexfys18"

         InstagramAPI.uploadPhoto(imagename, caption)
         os.rename(imagename, imagename2)
         print imagename2 + "uploaded"
     sleep(60)
