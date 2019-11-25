from datetime import datetime

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
    return c+day+e+f- 1524.5

def GreenwichMeanSiderialTime():
    d = julianDate() - 2451545.0    #Days since 2000 Jan. 1 12H UT1
    T = d / 36525.0;                #Centuries since 2000 Jan. 1 12H UT1
    now = datetime.utcnow()
    GMST = 6.697374558 + .06570982441908 * d + 1.00273790935 * (now.hour + (now.minute/60) + (now.second/3600)) + .000026 * (T**2)
    return GMST - ((GMST // 24) * 24)

def getSiderealTime():
    gst = GreenwichMeanSiderialTime()
    siderealHour = int(gst)
    remainder = (gst- siderealHour) * 60
    siderialMinute = int(remainder)
    siderialSecond = int( (remainder - siderialMinute) * 60)
    return (siderealHour, siderialMinute, siderialSecond)

print(getSiderealTime())
