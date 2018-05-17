import RoboPiLib as RPL
import time
import math
RPL.RoboPiInit("/dev/ttyAMA0",115200)

f = open('bearing-output.txt', 'r')

if f.read() == '+':
    RPL.servoWrite(2, 1000)
    RPL.servoWrite(3, 2000)
if f.read() == '-':
    RPL.servoWrite(2, 1000)
    RPL.servoWrite(3, 2000)
if f.read() == '0':
    RPL.servoWrite(2, 1000)
    RPL.servoWrite(3, 2000)
