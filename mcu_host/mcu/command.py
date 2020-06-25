from .. import connector
from . import data_storage


def set_pwm(pwm):
    connector.write_queue.put(bytes([1, pwm]))
    pass


def set_direction(direction):
    connector.write_queue.put(bytes([2, direction]))


data_storage.register("pwm", set_pwm)
data_storage.register("direction", set_direction)
