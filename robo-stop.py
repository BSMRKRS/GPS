import RoboPiLib as RPL
from setup import RPL
import post_to_web as PTW
RPL.RoboPiInit("/dev/ttyAMA0",115200)

print "Please type in the pin number of your motors:"
motorL = int(raw_input("Left Motor > "))
motorR = int(raw_input("Right Motor > "))


RPL.servoWrite(motorR, 0)
RPL.servoWrite(motorL, 0)
