import serial
import time
import os

def readEepromBinary(filename):
    arduino = serial.Serial(port='COM3', baudrate=9600, timeout=10)
    time.sleep(2)
    command = "C\n"
    arduino.write(command.encode('utf-8'))
    # Open file to write
    with open(filename, 'w') as file:
        while True:
            data = arduino.readline().decode('utf-8').strip()
            if data:
                file.write(data + '\n')
            if data == "DONE":
                break
    arduino.close()

def writeToEeprom(filename):
    filename_without_extension = os.path.splitext(filename)[0]
    binfilename = f'static/decfiles/{filename_without_extension}.txt'

    arduino = serial.Serial(port='COM3', baudrate=9600, timeout=10)
    # Wait for the Arduino to initialize
    time.sleep(2)  # 2 seconds is usually enough
    arduino.write('D\n'.encode('utf-8'))
    # Read the data from the text file
    with open(binfilename, 'r') as file:
        lines = file.readlines()
    # Send the data to the Arduino
    for line in lines:
        if line.strip().isdigit():  # Check if the line contains a number
            arduino.write((line.strip() + '\n').encode('utf-8'))
            time.sleep(0.05)  # Give the Arduino some time to process each line
    # Send a 'DONE' signal to indicate the end of the data
    arduino.write('DONE\n'.encode('utf-8'))
    # Close the serial port
    arduino.close()

# def writeToEeprom(filename):
#     # Take out .png from the filename
#     filename_without_extension = os.path.splitext(filename)[0]
#     binfilename = f'static/binfiles/{filename_without_extension}.txt'
#     print(binfilename)