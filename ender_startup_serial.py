#This code provides functions that allow for ender3 connection by serial port

#import necessary libraries
import serial
import serial.tools.list_ports as list_ports


"""
Function to find desired port
"""
def get_port():
    ports = list_ports.comports()
    for port in ports:
        if 'usbserial' in port.name:
            desired_port = port
    return desired_port.device

"""
Function to connect to serial port 
"""
def serial_connect(p):
    ser = serial.Serial(
        port = p,
        baudrate = 115200
    )
    return ser
