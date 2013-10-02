
# Biblioteca: http://learn.adafruit.com/setting-up-io-python-library-on-beaglebone-black

import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.ADC as ADC
import time

a = "P8_12"
b = "P8_14"
c = "P8_16"
d = "P8_18"
e = "P8_20"
f = "P8_22"
g = "P8_24"
p = "P8_26"
pot = "P9_33"

GPIO.setup(pot, GPIO.IN)
GPIO.setup(a, GPIO.OUT)
GPIO.setup(b, GPIO.OUT)
GPIO.setup(c, GPIO.OUT)
GPIO.setup(d, GPIO.OUT)
GPIO.setup(e, GPIO.OUT)
GPIO.setup(f, GPIO.OUT)
GPIO.setup(g, GPIO.OUT)
GPIO.setup(p, GPIO.OUT) 

ADC.setup()   
    
while True:
    for i in [f, a, b, c, d, e]:
       GPIO.output(i, GPIO.HIGH)
       delay = ADC.read_raw(pot)
       time.sleep(delay)
       GPIO.output(i, GPIO.LOW)