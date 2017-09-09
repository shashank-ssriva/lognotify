# lognotify

## Introduction

Wouldn't it be super convenient if you are working on your web-app code & you see a notification popping up on your screen with the exact error, in the realtime whenever there is an error in your log?
It personally find it very helpful because I can get to know why my application is not working. Whenever an error is encountered, the pop-up message tells me about it right away :wink:

lognotify is a simple utility (*& my first ever Python script*) that displays a pop-up notification showing me the exact error message in real-time while I am working on my PHP web-app.
This utility is very simple, small & highly customisable. You can customise it to tailor to your specific needs. For example, you can customise it to monitor your system logs, Apache logs, MySQL logs & potentially an log-file.
Please note that this version of lognotify is for Ubuntu only. I will be releasing similar versions for other OSes soon. 

## Installation

Clone/unzip the repository, ``cd`` to ``lognotify`` directory & issue : -
```bash
sudo python setup.py install
```

Below is what the step looks like.

```bash
shashank@shashank-server ~/lognotify> sudo python setup.py install
running install
running bdist_egg
running egg_info
writing lognotify.egg-info/PKG-INFO
writing top-level names to lognotify.egg-info/top_level.txt
writing dependency_links to lognotify.egg-info/dependency_links.txt
writing entry points to lognotify.egg-info/entry_points.txt
reading manifest file 'lognotify.egg-info/SOURCES.txt'
writing manifest file 'lognotify.egg-info/SOURCES.txt'
installing library code to build/bdist.linux-x86_64/egg
running install_lib
running build_py
creating build/bdist.linux-x86_64/egg
copying build/lib.linux-x86_64-2.7/lognotify.py -> build/bdist.linux-x86_64/egg
byte-compiling build/bdist.linux-x86_64/egg/lognotify.py to lognotify.pyc
creating build/bdist.linux-x86_64/egg/EGG-INFO
copying lognotify.egg-info/PKG-INFO -> build/bdist.linux-x86_64/egg/EGG-INFO
copying lognotify.egg-info/SOURCES.txt -> build/bdist.linux-x86_64/egg/EGG-INFO
copying lognotify.egg-info/dependency_links.txt -> build/bdist.linux-x86_64/egg/EGG-INFO
copying lognotify.egg-info/entry_points.txt -> build/bdist.linux-x86_64/egg/EGG-INFO
copying lognotify.egg-info/not-zip-safe -> build/bdist.linux-x86_64/egg/EGG-INFO
copying lognotify.egg-info/top_level.txt -> build/bdist.linux-x86_64/egg/EGG-INFO
creating 'dist/lognotify-0.1-py2.7.egg' and adding 'build/bdist.linux-x86_64/egg' to it
removing 'build/bdist.linux-x86_64/egg' (and everything under it)
Processing lognotify-0.1-py2.7.egg
removing '/usr/local/lib/python2.7/dist-packages/lognotify-0.1-py2.7.egg' (and everything under it)
creating /usr/local/lib/python2.7/dist-packages/lognotify-0.1-py2.7.egg
Extracting lognotify-0.1-py2.7.egg to /usr/local/lib/python2.7/dist-packages
lognotify 0.1 is already the active version in easy-install.pth
Installing lognotify script to /usr/local/bin

Installed /usr/local/lib/python2.7/dist-packages/lognotify-0.1-py2.7.egg
Processing dependencies for lognotify==0.1
Finished processing dependencies for lognotify==0.1
```

## Usage

Once installed, lognotify is available as a shell command ``lognotify``. To invoke it, type ``lognotify`` followed by the absolute or relative path to the log file that you want to monitor.
Depending upon the context, you will see a pop-up notification.

```bash
root@shashank-dbserver /h/s/lognotify# lognotify
No log-file specified. Kindly specify a valid log-file for monitoring. Exiting now...
```
```bash
root@shashank-dbserver /h/s/lognotify# lognotify /var/log/apache2/other_vhosts_access.log2
Log-file you specified doesn't seem to be present. Please specify a valid file.
```
```bash
root@shashank-dbserver /h/s/lognotify# lognotify /var/log/apache2/other_vhosts_access.log
192.168.0.51:80 127.0.0.1 - - [08/Sep/2017:15:00:51 +0200] "GET /jsdate/jsDatePick.min.1.3.js HTTP/1.1" 404 517 "http://localhost/CabBIlls/feedData.php" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"
```
## Screenshot

Below is the pop-up notification I saw because of a resource being not available(404) :

<img src="https://github.com/shashank-ssriva/lognotify/blob/master/lognoify_in_action.png" height="350" width="250">

## YouTube Demo Video

Click below thumbnail to watch the demo video  

<a href="http://www.youtube.com/watch?feature=player_embedded&v=K8I_xFdfYFs
" target="_blank"><img src="http://img.youtube.com/vi/K8I_xFdfYFs/0.jpg" 
alt="lognotify YourTube demo video" width="480" height="360" border="10" /></a>
