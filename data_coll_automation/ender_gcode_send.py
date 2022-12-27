#This code will connect with the ender and send gcode

#Import necessary libraries
import ender_startup_serial
import mixture_experiment_prep
import time

#Functions
def config_settings(connected_ser):
    connected_ser.write('M302 S0'.encode() + b'\n')
    connected_ser.write('M211 S0'.encode() + b'\n') 
    connected_ser.write('G91'.encode() + b'\n')
    connected_ser.write('G4 S5'.encode() + b'\n')

def gcode_write(connected_ser, c_list):
    for element in c_list:
        to_send = 'G01 X' + str(element[0]) + ' Y' + str(element[1]) + ' Z' + str(element[2])
        g_code_string = element.encode() + b'\n'
        time.sleep(1)
        connected_ser.write(g_code_string)
        time.sleep(7)
        print('Command Executed')

if __name__ == '__main__':

    #Vertices to generate convex hull
    vertices = [
        [0, 1],
        [1, 0],
        [0, 0]
    ]

    #List of mole fractions
    g_list = generate_points(vertices, 100)

    #Connect ender
    port = ender_startup_serial.get_port()
    ser = ender_startup_serial.serial_connect(port)
    print('Connection Open...\n')

    #Configure settings
    config_settings(ser)

    #Write gcode commands
    gcode_write(ser, g_list)

    #Close connection
    ser.close()
    print('\nConnection Closed!')
