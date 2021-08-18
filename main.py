# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import time
import random
import urllib
from time import localtime, strftime

starttime = time.time() #starts time
id = 0
while True:
    id = random.randint(15, 30) #generates random temp
    date = strftime("%Y-%m-%d", localtime()) #gets current date
    time2 = strftime("%H:%M:%S", localtime()) #gets current time
    url = "http://ec2-35-80-151-233.us-west-2.compute.amazonaws.com/measurements/" \
          "url_create?instrument_id=2&bmp_temp={0}&email=luthyka@wfu.edu&api_key=" \
          "s-ZNstQ32Uz3uoSWpPHN&at={1}T{2}".format(id, date, time2) #inserts rand temp, date, time into url
    urllib.urlopen(url) #opens url silently
    time.sleep(0.5 - ((time.time() - starttime) % 0.5))



