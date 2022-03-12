import serial


def open_com():
    try:
        global uart
        uart = serial.Serial(
            port="COM4",
            baudrate=3000000,
        )
    except:
        print("Ufffff")

def modbus_read_registers(modbus_function: int,
                          register_address: int,
                          amount_of_read: int,
                          ):
    uart.write()
    return slave_response