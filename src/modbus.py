import minimalmodbus
import serial

from ctypes import *

global instr


def check_com():
    try:
        uart = serial.Serial(
            port="COM4",
            baudrate=3000000,
        )
        uart.close()
        return True
    except:
        return False

def open_com():
    global instr            # find out a better way of declaring variables
    try:
        instr = minimalmodbus.Instrument(port="COM4", slaveaddress=1)
    except:
        print("Uffff")


    instr.debug = True
    # instr.serial.port                      # this is the serial port name
    instr.serial.baudrate = 3000000
    instr.serial.timeout = 0.020


def modbus_enable_motor(slave_id: int):
    instr.write_register(40004, 1, 0, 6, False)


def modbus_update_target_angle(value: int):
    instr.serial.timeout = 0.100
    instr.write_register(40003, value, 0, 6, False)


def modbus_read_registers(modbus_function: int,
                          register_address: int,
                          amount_of_read: int,
                          ):
    slave_response = instr.read_registers(register_address, amount_of_read, functioncode=modbus_function)
    return slave_response


def convert_float(value: int):
    # i = int(s, 16)                 # convert from hex to a Python int
    cp = pointer(c_int(value))       # make this into a c integer
    fp = cast(cp, POINTER(c_float))  # cast the int pointer to a float pointer
    return fp.contents.value         # dereference the pointer, get the float

def modbus_write_single(value: int):
    instr.serial.timeout = 0.100
    instr.write_register(40003, value, 0, 6, False)