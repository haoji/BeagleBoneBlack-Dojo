
# Biblioteca: http://learn.adafruit.com/setting-up-io-python-library-on-beaglebone-black

import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.ADC as ADC
import time

a = "P8_12" # topo
b = "P8_13" # direita cima
c = "P8_14" # direita baixo
d = "P8_15" # baixo
e = "P8_16" # esquerda baixo
f = "P8_17" # esquerda cima
g = "P8_18" # meio
p = "P8_19" # ponto
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
       delay = ADC.read(pot)
       time.sleep(delay)
       GPIO.output(i, GPIO.LOW)