from math import atan, asin, sin, cos, tan, degrees, radians

def getAltAz(latitude, localSiderialTime, ra, dec):
    LHA = (localSiderialTime - ra)#degrees
    if LHA < 0:
        LHA += 360
    azimuth = degrees(atan(sin(radians(LHA))/(cos(radians(LHA))*sin(radians(latitude)) - tan(radians(dec))*cos(radians(latitude)))))
    altitude = degrees(asin(sin(radians(latitude))*sin(radians(dec)) + cos(radians(latitude))*cos(radians(dec))*cos(radians(LHA))))
    if azimuth < 0:
        azimuth += 180
    if LHA < 180:
        azimuth = 180 + azimuth
    return altitude, azimuth
