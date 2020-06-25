from . import data_storage


def on_receive(rec: bytes):
    # data_storage.update("pwm", int.from_bytes(rec, byteorder='big'))
    print(rec)
    pass
