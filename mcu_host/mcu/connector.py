import serial
from mcu_host.mcu import DataStorage
from concurrent.futures import ThreadPoolExecutor


class MCUConnector:
    def __init__(self, data_storage: DataStorage, serial_port: str, serial_baudrate: int, pool: ThreadPoolExecutor):
        self.data_storage = data_storage
        self.serial_port = serial_port
        self.pool = pool
        self.__serial = serial.Serial(serial_port, serial_baudrate)

    def __receive_loop(self):
        try:
            while True:
                rec = self.__serial.read(1)
                # print(f"readed {rec}")
                if rec == b'':
                    continue
                self.data_storage.update("pwm", int.from_bytes(rec, byteorder='big'))
        except Exception as e:
            self.__when_loop_stop()

    def __when_loop_stop(self):
        if not self.__serial.is_open:
            self.__serial.open()
        self.start_receive()

    def start_receive(self):
        self.pool.submit(self.__receive_loop)
