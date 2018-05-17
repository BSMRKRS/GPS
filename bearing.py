import math
import time


def robot_control(x1, y1, x2, y2, b1):
    tup1 = (x1, y1)
    tup2 = (x2, y2)
    def calculate_initial_compass_bearing(pointA, pointB):
        if (type(pointA) != tuple) or (type(pointB) != tuple):
            raise TypeError('Only tuples are supported as arguments')
        lat1 = math.radians(pointA[0])
        lat2 = math.radians(pointB[0])

        diffLong = math.radians(pointB[1] - pointA[1])

        p = math.sin(diffLong) * math.cos(lat2)
        t = math.cos(lat1) * math.sin(lat2) - (math.sin(lat1)
            * math.cos(lat2) * math.cos(diffLong))

        initial_bearing = math.atan2(p, t)

        # Now we have the initial bearing but math.atan2 return values
        # from -180 to + 180 which is not what we want for a compass bearing
        # The solution is to normalize the initial bearing as shown below
        initial_bearing = math.degrees(initial_bearing)
        compass_bearing = (initial_bearing + 360) % 360

        return compass_bearing
    b2 = calculate_initial_compass_bearing(tup1, tup2)
    if b2 > b1:
        return '+'
    if b2 == b1:
        return '0'
    if b2 < b1:
        return '-'

f = open('bearing-output.txt', 'w')

print robot_control(100, 400, 200, 100, 180)

if robot_control(100, 400, 200, 100, 180) == "+":
    f.write('+')
if robot_control(100, 400, 200, 100, 180) == "-":
    f.write('-')
if robot_control(100, 400, 200, 100, 180) == "0":
    f.write('0')

f.close()


