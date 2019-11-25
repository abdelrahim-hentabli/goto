from gps import get_gps
from accel_mag import get_accel_mag 
import geomag as gm
from time import sleep
from math import atan, degrees



magDec = gm.declination(33.975599,-117.326188)
while True: 
    accel_mag = get_accel_mag()
    acceleration = accel_mag["acceleration"]
    magnetic = accel_mag["magnetic"]
    while(acceleration[0] **2 + acceleration[1] ** 2 + acceleration[2] **2 < 56.25 or acceleration[0] **2 + acceleration[1] ** 2 + acceleration[2] **2 > 156.25  ):
        #print(acceleration[0] **2 + acceleration[1] ** 2 + acceleration[2] **2) 
        accel_mag = get_accel_mag()
        acceleration = accel_mag["acceleration"]
        magnetic = accel_mag["magnetic"]
    #print("Declination Angle: ", magDec)
    #print("Acceleration: ", accel_mag["acceleration"])
    print("Magnetic: ", accel_mag["magnetic"])
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
#gps = get_gps()
#print(gps)
