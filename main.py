from gps import get_gps
from stars import getAltAz
from times import getLocalSiderialTimeAngle
from motor import calibrate, gotoAltAzimuth

File = open('TopStars.txt', 'r')
topStars = []
topStarsByName = {}

for line in File:
    split = line.split(',')
    topStars.append((split[1],split[2],15 * (float(split[3]) + float(split[4])/60), float(split[5]),float(split[6])))
    if(split[2] != ''):
        topStarsByName[split[2]] = (split[1],split[2],15 * (float(split[3]) + float(split[4])/60), float(split[5]),float(split[6]))


#latitude, longitude = get_gps()
latitude = 33.8953781
longitude = -117.3231389

calibrate(latitude, longitude)

exit = False
while not exit:
    temp = input('Which star do you wanna see?:  ')
    if temp == 'exit':
        exit = True
    star = None
    try:
        starNumber = int(temp)
        star = topStars[starNumber-1]
    except:
        if temp in topStarsByName:
            star = topStarsByName[temp]
    if star is not None:
        alt, az =getAltAz(latitude, getLocalSiderialTimeAngle(longitude), star[2], star[3])
        gotoAltAzimuth(alt, az)
gotoAltAzimuth(90 , 0)
