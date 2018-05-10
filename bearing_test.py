import RoboPiLib as RPL
RPL.RoboPiInit("/dev/ttyAMA0",115200)
import math
import time

tup1 = (44.963883, -93.351047)
tup2 = (100, 500)
tup3 = (int(raw_input("X coorxinate: ")), int(raw_input("Y coordinate: ")))

(x1, x2) = tup1
(y1, y2) = tup2
(z1, z2) = tup3

def robot_control(x1, x2, y1, y2, b2):

def calculate_initial_compass_bearing(pointA, pointB):
    if (type(pointA) != tuple) or (type(pointB) != tuple):
        raise TypeError("Only tuples are supported as arguments")
    lat1 = math.radians(pointA[0])
    lat2 = math.radians(pointB[0])

    diffLong = math.radians(pointB[1] - pointA[1])

    x = math.sin(diffLong) * math.cos(lat2)
    y = math.cos(lat1) * math.sin(lat2) - (math.sin(lat1)
            * math.cos(lat2) * math.cos(diffLong))

    initial_bearing = math.atan2(x, y)

    # Now we have the initial bearing but math.atan2 return values
    # from -180 to + 180 which is not what we want for a compass bearing
    # The solution is to normalize the initial bearing as shown below
    initial_bearing = math.degrees(initial_bearing)
    compass_bearing = (initial_bearing + 360) % 360

    return compass_bearing

b1 = calculate_initial_compass_bearing(tup1, tup2)
b2 = calculate_initial_compass_bearing(tup3, tup2)
print "Initial bearing is %r" %calculate_initial_compass_bearing(tup1, tup2)
print "Your bearing is %r" %calculate_initial_compass_bearing(tup3, tup2)
# Bearing 1 is the point you are trying to get to

if b2 > b1:
    print "+"
if b2 == b1:
    print "0"
if b2 < b1:
    print "-"
