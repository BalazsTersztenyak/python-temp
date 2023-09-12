#! /usr/bin/python
import time
import os

TEMP_PATH="/sys/class/thermal/thermal_zone0/"

#fo = open(TEMP_PATH + "temp","r")
#temp=fo.read()
#print(temp)

def readTemp():
    fo = open(TEMP_PATH + "temp", "r")
    temp = fo.read()
    return int(temp)*0.001



def avgTemp(n):
    avg = 0
    for i in range(n):
        avg += readTemp()
    avg /= n
    return avg

def continous():
    while True:
        os.system("clear")
        print(avgTemp(40),"°C")
        time.sleep(1)
