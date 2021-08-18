# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import time, webbrowser
import random

from time import localtime, strftime

starttime = time.time()
id = 0
hour = 0
minute = 0
second = 0
date = strftime("%Y-%m-%d", localtime())
time2 = strftime("%H:%M:%S", localtime())
while True:
    id = random.randint(15, 30)
    url = "http://ec2-35-80-151-233.us-west-2.compute.amazonaws.com/measurements/" \
          "url_create?instrument_id=2&bmp_temp={0}&email=luthyka@wfu.edu&api_key=" \
          "s-ZNstQ32Uz3uoSWpPHN&at={1}T{2}".format(id, date, time2)
    webbrowser.open(url)  # Go to example.com
    time.sleep(5.0 - ((time.time() - starttime) % 5.0))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
