from mcu_host.ui import *
from mcu_host.mcu import *


class MainFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.load_other_frame()

    def load_other_frame(self):
        self.control_frame = ControlFrame(self)
        self.data_frame = DataShowFrame(self, data_name="PWM")
        self.control_frame.grid(row=0, column=1, padx=15)
        self.data_frame.grid(row=0, column=0)

    def bind_data(self, data_storage: DataStorage):
        data_storage.register("pwm", lambda x: self.data_frame.var_input.set(str(x)))
