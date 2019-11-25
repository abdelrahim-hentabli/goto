from datetime import datetime
#from astropy.time import Time



print(datetime.now())

def julianDate():
    now = datetime.utcnow()
    month = now.month
    year = now.year
    day = now.day
    if(month <= 2):
        y-= 1
        m += 12
    a = year //100
    b = a//4
    c = 2-a+b
    e = int(365.25*(year +4716))
    f = (int)(30.6001 * (month +1))
    return c+day+e+f- 1524.5 + now.hour / 24 + (now.minute / (24 * 60)) + (now.second / (24 * 60 *60))

def GreenwichMeanSiderialTime():
    d = julianDate() - 2451545.0    #Days since 2000 Jan. 1 12H UT1
    T = d / 36525.0;                #Centuries since 2000 Jan. 1 12H UT1
    temp = 24110.54841 + (8640184.812866 * T) + (.093104 * T**2) - (.0000062 * (T **3))
    now = datetime.utcnow()
    UT = now.hour * 3600 + now.minute * 60 + now.second     #in seconds
    temp += (1.00273790935 + .000000000059 * T) * UT
    temp = temp % 86400
    return temp / 3600


def getSiderealTime():
    gst = GreenwichMeanSiderialTime()
    siderealHour = int(gst)
    remainder = (gst- siderealHour) * 60
    siderialMinute = int(remainder)
    siderialSecond = int( (remainder - siderialMinute) * 60)
    return (siderealHour, siderialMinute, siderialSecond)

print("Julian Date according to my code: ", julianDate())
#print("Julian Date according to astroPy: ", Time.now().jd)

print("Sidereal Time according to my code: ", getSiderealTime())
#print("Sidereal Time according to astroPy: ", Time.now().sidereal_time('mean'))
