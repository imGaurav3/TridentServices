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
instrument.serial.apply_settings

control_switch_position = instrument.read_register(9,0,3)
fault_type = instrument.read_register(11,0,3)
fault_code = instrument.read_register(12,0,3)
battery = instrument.read_register(60,1,3)
oil_pressure = instrument.read_register(61,0,3)
oil_temperature = instrument.read_register(62,0,3)
fuel_rate = instrument.read_register(66,1,3)
run_time1 = instrument.read_register(69,1,3)
run_time2 = instrument.read_register(70,1,3)
fuel_consumption1 = instrument.read_register(71,0,3)
fuel_consumption2 = instrument.read_register(72,0,3)
no_of_runs = instrument.read_register(74,0,3)

print("Control Switch Position : " + str(control_switch_position))
print("Fault Type : " + str(fault_type))
print("Fault Code : " + str(fault_code))
print("Battery : " + str(battery))
print("Oil Pressure : " + str(oil_pressure))
print("Oil Temperature : " + str(oil_temperature))
print("Fuel Rate : " + str(fuel_rate))
print("Run Time 1 : " + str(run_time1))
print("Run Time 2 : " + str(run_time2))
print("Fuel Consumption 1 : " + str(fuel_consumption1))
print("Fuel Consumption 2 : " + str(fuel_consumption2))
print("Number of Runs : " + str(no_of_runs))
