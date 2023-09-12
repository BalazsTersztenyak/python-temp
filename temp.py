#! /usr/bin/python

TEMP_PATH="/sys/class/thermal/thermal_zone0/"

fo = open(TEMP_PATH + "temp","r")
temp=fo.read()
print(temp)
