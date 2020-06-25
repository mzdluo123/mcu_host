import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
from mcu_host.mcu import *
from mcu_host.ui.serial_select import SerialManager


class ControlFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.up_btn = ttk.Button(self, text="增加")
        self.up_btn.grid(row=0, column=0, ipady=20)
        self.down_btn = ttk.Button(self, text="减少")
        self.down_btn.grid(row=1, column=0, ipady=20)
        self.direction_btn = ttk.Button(self, text="正转", command=self.change_direction)
        self.direction_btn.grid(row=0, column=1, columnspan=2, ipady=20)

    def change_direction(self):
        pass


class DataShowFrame(tk.Frame):
    def __init__(self, master=None, data_name="默认名称"):
        super().__init__(master)
        self.master = master
        self.data_name = data_name
        self.var_input = tk.StringVar()
        self.data_font = tkFont.Font(size=20)
        self.label_font = tkFont.Font(size=15)

        self.create_widgets()

    def create_widgets(self):
        self.label = ttk.Entry(self, font=self.data_font, state=tk.DISABLED, textvariable=self.var_input, width=10)
        self.label.grid(row=0, column=1, ipady=15)
        self.label = ttk.Label(self, font=self.label_font, text=self.data_name)
        self.label.grid(row=0, column=0, padx=10)


class MainPanel(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.load_other_frame()

    def load_other_frame(self):
        self.control_frame = ControlFrame(self)
        self.data_frame = DataShowFrame(self, data_name="PWM")
        self.control_frame.grid(row=0, column=1, padx=20)
        self.data_frame.grid(row=0, column=0)


class MainFrame(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.load_other_frame()

    def load_other_frame(self):
        self.main_panel = MainPanel(self)
        self.main_panel.grid(row=1, column=0, pady=10)
        self.serial_manage = SerialManager(self)
        self.serial_manage.grid(row=0, column=0)

    def bind_data(self, data_storage: DataStorage):
        data_storage.register("pwm", lambda x: self.main_panel.data_frame.var_input.set(str(x)))
