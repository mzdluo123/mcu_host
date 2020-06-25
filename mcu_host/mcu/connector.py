import serial
from queue import Queue
from concurrent.futures import ThreadPoolExecutor
from .receiver import on_receive


class MCUConnector:
    def __init__(self):
        self.serial_port = None
        self.baudrate = None
        self.write_queue = Queue()
        self.__serial = serial.Serial()
        self.__pool = None
        self.is_open = False

    def open_serial(self):
        if not self.is_open:
            self.__pool = ThreadPoolExecutor()
            self.__serial.baudrate = self.baudrate
            self.__serial.port = self.serial_port
            self.__serial.timeout = 0.1
            self.write_queue.empty()
            self.__serial.open()
            self.is_open = True
            self.start_receive()
            self.start_send()

    def close_serial(self):
        self.is_open = False
        if self.__pool is not None:
            self.__pool.shutdown(False)
        self.write_queue.empty()
        self.__serial.close()

    def __receive_loop(self):
        try:
            while self.is_open:
                rec = self.__serial.read(1)
                # print(f"readed {rec}")
                if rec == b'':
                    continue
                on_receive(rec)
        except Exception as e:
            pass

    def __send_loop(self):
        while self.is_open:
            try:
                data = self.write_queue.get(False, timeout=1)
                if type(data) != bytes:
                    continue
                self.__serial.write(data)
                print(f"send {data}")
            except Exception as e:
                pass


    def start_receive(self):
        self.__pool.submit(self.__receive_loop)

    def start_send(self):
        self.__pool.submit(self.__send_loop)

    def error_handle(self):
        self.is_open = False
        if not self.__serial.is_open:
            self.open_serial()
