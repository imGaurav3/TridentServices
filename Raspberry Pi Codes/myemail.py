

import smtplib
import RPi.GPIO as GPIO
import time


def emails():

        smtpUser = 'ketkikokate199@gmail.com'
        smtpPass = '7798398892'
        toAdd = 'ketkikokate199@gmail.com'
        fromAdd= smtpUser

        subject = 'test'
        body = 'hiii'
        print (body)
        s = smtplib.SMTP('smtp.gmail.com',587)
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(smtpUser,smtpPass)
        s.sendmail(fromAdd,toAdd,body)
        s.quit()


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
    if distance<5:
	emails()
	break
    time.sleep(1)
