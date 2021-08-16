# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import time, webbrowser
starttime = time.time()
while True:
    # print "tick"
    webbrowser.open('http://ec2-35-80-151-233.us-west-2.compute.amazonaws.com/measurements/url_create?instrument_id=2&bmp_temp=22.2&email=luthyka@wfu.edu&api_key=s-ZNstQ32Uz3uoSWpPHN&at=2021-08-12T13:40:30')  # Go to example.com
    time.sleep(5.0 - ((time.time() - starttime) % 5.0))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
