from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

pins = [12, 16, 18, 22]

for pin in pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, False)

halfstep_seq = [
        [1,0,0,1],
        [1,0,0,0],
        [1,1,0,0],
        [0,1,0,0],
        [0,1,1,0],
        [0,0,1,0],
        [0,0,1,1],
        [0,0,0,1]]


for i in range(1024):
    for halfstep in range(8):
        for pin in range(4):
            if(halfstep_seq[halfstep][pin] == 1):
                GPIO.output(pins[pin], True)
            else:
                GPIO.output(pins[pin], False)
        sleep(.00075)

GPIO.cleanup()
