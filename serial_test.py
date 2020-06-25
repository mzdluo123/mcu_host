import serial.tools.list_ports

print(serial.tools.list_ports.comports()[0].device)