#Author : - Shashank Srivastava
#description=A real-time log monitoring & notification utility which pops up a notification (while running your application) whenever it sees an error in log-file.

#Loading modules & other functionalities
from time import sleep
import time, os
import sys
from sys import version_info
import pynotify
import logging
import scorer.notification as notify
import os.path
import re
#Important to let user specify a log-file in advance.
if len(sys.argv) < 2:
    print("No log-file specified. Kindly specify a valid log-file for monitoring. Exiting now...")
    sys.exit()

#Defining function to exit.
def exitApp():
    print "Exiting the application now..."
    sys.exit()

#Notification module
logger = logging.getLogger('notification')
def popUpMessage(title, message):
    logger.info("Initializing pynotify")
    try:
        pynotify.Notification(title, message, "dialog-information").show()
    except Exception as e:
        logger.error("Error initializing pynotify")
        logger.debug(e)
        logger.info("Unable to initialize pynotify: Connection Refused")
        logger.info("Quitting the app")
        exitApp()

#Set the filename and open the file
filename = sys.argv[1]
if os.path.isfile(sys.argv[1]):
    file = open(filename,'r')
else:
    print ("Log-file you specified doesn't seem to be present. Please specify a valid file.")
    sys.exit()

#Find the size of the file and move to the end
st_results = os.stat(filename)
st_size = st_results[6]
file.seek(st_size)

while 1:
    where = file.tell()
    line = file.readline()
    if not line:
        time.sleep(1)
        file.seek(where)
    else:
        title = "Log Entries : "
        searchString = line
        regex = r"(404|500|503|failed to open stream|Unable to move)"
        #if "404" in line or "503" in line or "Unable to move" in line or "failed to open stream" in line:
        result = re.findall(regex,searchString)
        if len(result) > 0:
            print line
            msg = line+"Check the directory permissions!"
            notify.popUpMessage(title,msg)
