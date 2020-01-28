# python3.7

# get positional arguments
import sys

from math import sin, cos, sqrt, atan2, radians

lat1 = radians(float(sys.argv[1]))
lon1 = radians(float(sys.argv[2]))
lat2 = radians(float(sys.argv[3]))
lon2 = radians(float(sys.argv[4]))

# approximate radius of earth in km
R = 6373.0

dlon = lon2 - lon1
dlat = lat2 - lat1

a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
c = 2 * atan2(sqrt(a), sqrt(1 - a))

distance = R * c

print("Result:", distance)
