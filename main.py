from gps import get_gps
from accel_mag import get_accel_mag 
import geomag as gm
from time import sleep
from math import atan, degrees
from stars import getAltAz
from times import getLocalSiderialTimeAngle

File = open('TopStars.txt', 'r')

topStars = []
topStarsByName = {}

for line in File:
    split = line.split(',')
    topStars.append((split[1],split[2],15 * (float(split[3]) + float(split[4])/60), float(split[5]),float(split[6])))
    if(split[2] != ''):
        topStarsByName[split[2]] = (split[1],split[2],15 * (float(split[3]) + float(split[4])/60), float(split[5]),float(split[6]))




#latitude, longitude = get_gps()

#magDec = gm.declination(latitude, longitude)
magDec = gm.declination(33.975599,-117.326188)



'''
while True: 
    accel_mag = get_accel_mag()
    acceleration = accel_mag["acceleration"]
    magnetic = accel_mag["magnetic"]
    while(acceleration[0] **2 + acceleration[1] ** 2 + acceleration[2] **2 < 56.25 or acceleration[0] **2 + acceleration[1] ** 2 + acceleration[2] **2 > 156.25  ):
        accel_mag = get_accel_mag()
        acceleration = accel_mag["acceleration"]
        magnetic = accel_mag["magnetic"]
    if(magnetic[0] != 0):
        magNorth = degrees(atan(magnetic[1]/magnetic[0]))
        if(magnetic[0] < 0):
            magNorth += 180
        if(magNorth < 0):
            magNorth += 360
    else:
        if(magnetic[1] < 0):
            magNorth = 270
        else:
            magNorth = 90

    trueNorth = magNorth + magDec
    if(trueNorth < 0):
        trueNorth += 360
    elif(trueNorth > 360):
        trueNorth -= 360
    print("Magnetic North Angle from +X", magNorth)
    print("True North Angle from +X", trueNorth)
    print("\n\n")
    sleep(1)
'''

while True:
    temp = input('Which star do you wanna see?:  ')
    star = None
    try:
        starNumber = int(temp)
        star = topStars[starNumber-1]
    except:
        if temp in topStarsByName:
            star = topStarsByName[temp]
    if star is not None:
        print(getAltAz(34.1478, getLocalSiderialTimeAngle(-118.1268), star[2], star[3]))


