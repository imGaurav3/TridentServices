import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

trig = 4
echo = 18

GPIO.setup(trig,GPIO.OUT)
GPIO.setup(echo,GPIO.IN)

def get_distance():
    GPIO.output(trig,True)
    time.sleep(1)
    GPIO.output(trig,False)
    
    while GPIO.input(echo) == False:
        start = time.time()
    while GPIO.input(echo) == True:
        end = time.time()
        
    sig_time = end - start
    
    distance = sig_time / 0.000058
    
    print('Distance : {} cm'.format(distance))
    return distance

while True:
    distance = get_distance()
    print(distance)
    time.sleep(0.05)
        