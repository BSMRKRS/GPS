import RoboPiLib as RPL
RPL.RoboPiInit("/dev/ttyAMA0",115200)
import math

tup1 = (44.963883, -93.351047)
tup2 = (44.956990, -93.345725)
(x1, x2) = tup1
(y1, y2) = tup2

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

dist1 = math.hypot(x2 - x1, y2 - y1)
print dist1

print calculate_initial_compass_bearing(tup1, tup2)

def Rturn():
    RPL.servoWrite(7, 1550)
    RPL.servoWrite(6, 1420)
    print "Turning Right"

def Lturn():
    RPL.servoWrite(6, 1460)
    RPL.servoWrite(7, 1550)
    print "Turning Left"
def Stop():
    RPL.servoWrite(6, 0)
    RPL.servoWrite(7, 0)
    print "Stopping"


new = time.time()
while time.time() < new + 3:
    RPL.servoWrite(6, 1000)
    RPL.servoWrite(7, 1000)
if time.time() > new + 3:
    RPL.servoWrite(6, 0)
    RPL.servoWrite(7, 0)

# Here is where you would get the readings from the GPS
# For an example, I am going to use the point (44.967861, -93.344609),
# which is northwest and farther away from the endpoint.
tup3 = (44.967861, -93.344609)
(z1, z2) = tup3
dist2 = math.hypot(z2 - z1, y2 - y1)

if dist2 > dist1:
    new1 = time.time()
    while time.time() < new + 3:
        Rturn()
    if time.time() > new + 3:
        Stop()
