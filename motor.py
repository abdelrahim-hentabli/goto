from time import sleep
import RPi.GPIO as GPIO
from accel_mag

_azimuth = 0
#74236 halfsteps for 1 revolution

_altitude = 90
#4085 halfsteps for 1 revolution

halfstep_seq = [
        [1,0,0,1],
        [1,0,0,0],
        [1,1,0,0],
        [0,1,0,0],
        [0,1,1,0],
        [0,0,1,0],
        [0,0,1,1],
        [0,0,0,1]]

def gotoAltAzimuth(alt, az): 
    alt_pins = [7, 11, 13,15]
    az_pins = [12, 16, 18, 22]
    global _altitude
    global _azimuth
    GPIO.setmode(GPIO.BOARD)
    for pin in alt_pins:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, False)
    for pin in az_pins:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, False)
    
    if alt < 0 or alt > 90:
        print("You goofed")
        return
    if alt < _altitude:
        alt_steps = int(round((4085 / 360) * (_altitude - alt)))
        alt_direction = 1
    else:
        alt_steps = int(round((4085 / 360) * (alt - _altitude)))
        alt_direction = -1
    _altitude += -alt_direction * alt_steps * 360/4085

    az_forward = az - _azimuth
    if az_forward < 0:
        az_forward += 360
    az_backward = _azimuth - az
    if az_backward < 0:
        az_backward += 360
    if (az_forward < az_backward):
        az_steps = int(round((74236 / 360) * az_forward))
        az_direction = -1
    else:
        az_steps = int(round((74236 /360) * az_backward))
        az_direction = 1
    _azimuth += az_steps *360/74236 *-az_direction
    if _azimuth < 0:
        _azimuth += 360
    if _azimuth > 360:
        _azimuth -=360
    i = 0
    j = 0
    while az_steps > 0 or alt_steps > 0:
        if alt_steps > 0:
            for pin in range(4):
                if(halfstep_seq[i][pin] == 1):
                    GPIO.output(alt_pins[pin], True)
                else:
                    GPIO.output(alt_pins[pin], False)
        if az_steps > 0:
            for pin in range(4):
                if(halfstep_seq[j][pin] == 1):
                    GPIO.output(az_pins[pin], True)
                else:
                    GPIO.output(az_pins[pin], False)
        sleep(.00075)
        i += alt_direction
        if i == len(halfstep_seq):
            i = 0
        if i < 0:
            i = len(halfstep_seq)-1
        alt_steps-=1

        j+=az_direction
        if j == len(halfstep_seq):
            j = 0
        if j < 0:
            j = len(halfstep_seq)-1
        az_steps-=1
    GPIO.cleanup()

