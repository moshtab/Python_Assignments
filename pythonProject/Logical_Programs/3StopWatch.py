'''
@Author: Mohsin
@Date: 2021-10-19 18:00:30
@Last Modified by: Mohsin
@Last Modified time: 2021-10-19 18:00:30
@Title : StopWatch Calculating elapsed time”
'''

import time


def stopwatch():
    start = int(input("Press 1 to start"))
    currentTime = round(time.time()*1000)
    print("Start Time :", currentTime)
    stop = int(input("Press 1 to stop"))
    endTime = round(time.time()*1000)
    print("Stop Time :", endTime)
    elapsedTime = complex(endTime - currentTime)
    print("ElapsedTime :", elapsedTime)
stopwatch()
