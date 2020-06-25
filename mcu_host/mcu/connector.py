import serial
from mcu_host.mcu import DataStorage
from concurrent.futures import ThreadPoolExecutor
from queue import Queue


class MCUConnector:
    def __init__(self, data_storage: DataStorage, pool: ThreadPoolExecutor):
        self.data_storage = data_storage
        self.serial_port = None
        self.baudrate = None
        self.pool = pool
        self.write_queue = Queue()
        self.__serial = serial.Serial()
        self.is_open = False

    def open_serial(self):
        if not self.is_open:
            self.__serial.baudrate = self.baudrate
            self.__serial.port = self.serial_port
            self.__serial.timeout = 0.1
            self.__serial.open()
            self.is_open = True
            self.start_receive()
            self.start_send()

    def close_serial(self):
        self.is_open = False
        self.write_queue.empty()
        self.__serial.close()

    def __receive_loop(self):
        try:
            while self.is_open:
                rec = self.__serial.read(1)
                # print(f"readed {rec}")
                if rec == b'':
                    continue
                self.data_storage.update("pwm", int.from_bytes(rec, byteorder='big'))
        except Exception as e:
            pass

    def __send_loop(self):
        try:
            while self.is_open:
                data = self.write_queue.get(False, timeout=1)
                if data is not bytes:
                    continue
                self.__serial.write(data)
        except Exception as e:
            pass

    def start_receive(self):
        self.pool.submit(self.__receive_loop)

    def start_send(self):
        self.pool.submit(self.__send_loop)

    def error_handle(self):
        self.is_open = False
        if not self.__serial.is_open:
            self.open_serial()
