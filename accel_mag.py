import busio
import board
import adafruit_lsm303_accel
import adafruit_lsm303dlh_mag

def get_accel_mag():
    theDict = {}
    i2c = busio.I2C(board.SCL, board.SDA)
    theDict["magnetic"]=  adafruit_lsm303dlh_mag.LSM303DLH_Mag(i2c).magnetic
    theDict["acceleration"]= adafruit_lsm303_accel.LSM303_Accel(i2c).acceleration
    return theDict 
