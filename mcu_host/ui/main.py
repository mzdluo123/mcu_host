from mcu_host.ui import *
from mcu_host.mcu import *
from mcu_host.ui.serial_select import SerialManager


class MainPanel(ttk.Frame):
    def __init__(self, master=None, serial_connector: MCUConnector = None):
        super().__init__(master)
        self.master = master
        self.load_other_frame()

    def load_other_frame(self):
        self.control_frame = ControlFrame(self)
        self.data_frame = DataShowFrame(self, data_name="PWM")
        self.control_frame.grid(row=0, column=1,padx = 20)
        self.data_frame.grid(row=0, column=0)


class MainFrame(ttk.Frame):
    def __init__(self, master=None, serial_connector: MCUConnector = None):
        super().__init__(master)
        self.master = master
        self.connector = serial_connector
        self.pack()
        self.load_other_frame()

    def load_other_frame(self):
        self.main_panel = MainPanel(self)
        self.main_panel.grid(row=1, column=0)
        self.serial_manage = SerialManager(self, self.connector)
        self.serial_manage.grid(row=0, column=0)

    def bind_data(self, data_storage: DataStorage):
        data_storage.register("pwm", lambda x: self.main_panel.data_frame.var_input.set(str(x)))
