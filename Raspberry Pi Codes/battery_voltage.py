import serial
import time
import minimalmodbus

instrument = minimalmodbus.Instrument('/dev/ttyUSB0',2)

instrument.serial.baudrate = 9600
instrument.serial.dataformat = 'decimal'
instrument.serial.parity = serial.PARITY_EVEN
instrument.serial.bytesize = 8
instrument.serial.stopbits = 1
instrument.serial.timeout = 3.0
#instrument.mode = minimalmodbus.MODE_RTU
instrument.serial.apply_settings
#print(battery)
battery = instrument.read_register(61,0,3)
#battery = instrument.read_bit(12,1)
#battery = battery * 0.1
print(battery)
#print(instrument)
#print(minimalmodbus._getDiagnosticString())
                                        
                                        
