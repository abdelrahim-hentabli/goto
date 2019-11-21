import time
import adafruit_gps
import serial

def get_gps():
    theDict = {}
    uart = serial.Serial("/dev/serial0", baudrate=9600, timeout=3000)
    gps = adafruit_gps.GPS(uart, debug=False)
    # Turn on the basic GGA and RMC info (what you typically want)
    gps.send_command(b'PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0')
    # Turn on just minimum info (RMC only, location):
    #gps.send_command(b'PMTK314,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0')
    # Turn off everything:
    # Tuen on everything (not all of it is parsed!)
    #gps.send_command(b'PMTK314,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0')

    gps.send_command(b'PMTK220,1000')
    last_print = time.monotonic()
    gps.update()
    while not gps.has_fix:
        gps.update()
        current = time.monotonic()
        if current - last_print >= 1.0:
            last_print = current
            if not gps.has_fix:
                print('Waiting for fix...')
                continue
    
    print('=' * 40)  # Print a separator line.
    print('Fix timestamp: {}/{}/{} {:02}:{:02}:{:02}'.format(
        gps.timestamp_utc.tm_mon,   # Grab parts of the time from the
        gps.timestamp_utc.tm_mday,  # struct_time object that holds
        gps.timestamp_utc.tm_year,  # the fix time.  Note you might
        gps.timestamp_utc.tm_hour,  # not get all data like year, day,
        gps.timestamp_utc.tm_min,   # month!
        gps.timestamp_utc.tm_sec))
    theDict["latitude"] = gps.latitude
    theDict["longitude"] = gps.longitude
    if gps.satellites is not None:
       theDict["satellites"] = gps.satellites
    else:
        theDict["satellites"] = 0
    if gps.altitude_m is not None:
       theDict["altitude"] = gps.altitude_m
    else:
        theDict["altitude"] = 0
    gps.send_command(b'PMTK314,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0')
    return theDict
