import serial
import RPi.GPIO as GPIO      
import os, time

GPIO.setmode(GPIO.BCM)    

# Enable Serial Communication
port = serial.Serial("/dev/ttyS0", baudrate=115200, timeout=3)

# Transmitting AT Commands to the Modem
# '\r\n' indicates the Enter key
val = 'AT'
port.write(val.encode())
rcv = port.read(10)
print(rcv)
time.sleep(1)


val1 = 'AT+CREG?'
port.write(val1.encode())      # Disable the Echo
rcv = port.read(10)
print(rcv)
time.sleep(1)


val1 = 'AT+CGATT?'
port.write(val1.encode())      # Disable the Echo
rcv = port.read(10)
print(rcv)
time.sleep(1)

val = 'AT+CIPSHUT'
port.write(val.encode())
rcv = port.read(10)
print(rcv)
time.sleep(3)



val = 'AT+CIPSTATUS'
port.write(val.encode())
rcv = port.read(10)
print(rcv)
time.sleep(1)

val = 'AT+CIPMUX=0'
port.write(val.encode())
rcv = port.read(10)
print(rcv)
time.sleep(1)




val2 = 'AT+CSTT="internet","",""'+'\r\n'
port.write(val2.encode())  # Select Message format as Text mode 
rcv = port.read(10)
print(rcv)
time.sleep(50)


# Sending a message to a particular Number

val4 = 'AT+CIICR"'+'\r\n'
port.write(val4.encode())
rcv = port.read(10)
print(rcv)
time.sleep(5)

val5 = 'AT+CIFSR'+'\r\n'
port.write(val5.encode())  # Message
rcv = port.read(10)
print(rcv)
time.sleep(3)

val5 = 'AT+CIPSTART="TCP","www.google.com","80"'+'\r\n'
port.write(val5.encode())  # Message
rcv = port.read(10)
print(rcv)
time.sleep(1)

rcv=""
val5 = 'AT+CIPSEND'
port.write(val5.encode())
while not rcv :
    rcv = port.read(10)
    print(rcv)
 