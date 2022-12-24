#This code will connect with the ender and send gcode

#Import necessary libraries
import ender_startup_serial
import time

#Functions
def config_settings(connected_ser):
    connected_ser.write('M302 S0'.encode() + b'\n')
    connected_ser.write('M211 S0'.encode() + b'\n') 
    connected_ser.write('G91'.encode() + b'\n')
    connected_ser.write('G4 S5'.encode() + b'\n')

def gcode_write(connected_ser, c_list):
    for element in c_list:
        g_code_string = element.encode() + b'\n'
        time.sleep(1)
        connected_ser.write(g_code_string)
        time.sleep(7)
        print('Command Executed')

if __name__ == '__main__':

    #GCode command list for testing
    g_code_list = [
       'G0 X-100 Y20 Z10',
       'G0 X-20 Y40 Z-30',
       'G0 X-5 Y-5 Z15',
       'G0 X22 Y17 Z-20' 
    ]

    #Connect ender
    port = ender_startup_serial.get_port()
    ser = ender_startup_serial.serial_connect(port)
    print('Connection Open...\n')

    #Configure settings/test GCode
    config_settings(ser)
    gcode_write(ser, g_code_list)

    #Close connection
    ser.close()
    print('\nConnection Closed!')
