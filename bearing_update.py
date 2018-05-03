import math

tup2 = (47.545643, -96.483100)
tup1 = (41.072876, -96.655662)

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

def Rturn():
    RPL.servoWrite(7, 1550)
    RPL.servoWrite(6, 1420)
    print "Turning Right"

def Lturn():
    RPL.servoWrite(6, 1460)
    RPL.servoWrite(7, 1550)
    print "Turning Left"

print calculate_initial_compass_bearing(tup1, tup2)

while True:
    go_right = False
    go_left = False

    if calculate_initial_compass_bearing > 180:
        go_right = True
    if calculate_initial_compass_bearing < 180:
        go_left = True

if go_right:
    Rturn()
elif go_left:
    Lturn()
