import busio
import board
import adafruit_lsm303_accel
import adafruit_lsm303dlh_mag
import geomag as gm
from math import degrees, atan

def get_accel_mag():
    theDict = {}
    i2c = busio.I2C(board.SCL, board.SDA)
    theDict["magnetic"]=  adafruit_lsm303dlh_mag.LSM303DLH_Mag(i2c).magnetic
    theDict["acceleration"]= adafruit_lsm303_accel.LSM303_Accel(i2c).acceleration
    return theDict

def getNorthAngle(latitude, longitude):
    magDec = gm.declination(latitude, longitude)
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
    return trueNorth
