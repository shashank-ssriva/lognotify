from time import sleep
import time, os
from sys import version_info
import logging
import pynotify
import scorer.notification as notify
#Defining function to exit.
def exitApp():
    print "Exiting the application now..."
    sys.exit()
#Notification module
logger = logging.getLogger('scorer.notification')
def popUpMessage(title, message):
    logger.info("Initializing pynotify")
    try:
        pynotify.init("Scorer")
        pynotify.Notification(title, message, "dialog-information").show()
    except Exception as e:
        logger.error("Error initializing pynotify")
        logger.debug(e)
        logger.info("Unable to initialize pynotify: Connection Refused")
        logger.info("Quitting the app")
        exitApp()
#Set the filename and open the file
filename = '/var/log/apache2/other_vhosts_access.log'
file = open(filename,'r')

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
        title = "404 Log Entries : "
        if "404" in line:
            print line
            msg = line
            notify.popUpMessage(title,msg)
