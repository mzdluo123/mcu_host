import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
from mcu_host.mcu import command
from mcu_host.ui.serial_select import SerialManager
from ..mcu import data_storage
from tkinter import messagebox


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

        self.direction_btn = ttk.Button(self, text="正转")
        self.direction_btn.grid(row=0, column=1, columnspan=2, ipady=20)

        self.set_pwm_btn = ttk.Button(self, text="设置PWM")
        self.set_pwm_btn.grid(row=1, column=1, columnspan=2, ipady=20)


class DataShowFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self.var_pwm = tk.StringVar()
        self.var_input = tk.IntVar()
        self.data_font = tkFont.Font(size=20)
        self.label_font = tkFont.Font(size=15)

        self.create_widgets()

    def create_widgets(self):
        self.entry1 = ttk.Entry(self, font=self.data_font, state=tk.DISABLED, textvariable=self.var_pwm, width=10)
        self.entry1.grid(row=0, column=1, ipady=15)

        self.label = ttk.Label(self, font=self.label_font, text="PWM")
        self.label.grid(row=0, column=0, padx=10)

        self.entry2 = ttk.Entry(self, font=self.data_font, textvariable=self.var_input, width=10)
        self.entry2.grid(row=1, column=1, ipady=15)

        self.label2 = ttk.Label(self, font=self.label_font, text="输入PWM值")
        self.label2.grid(row=1, column=0, padx=10)


class MainPanel(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.load_other_frame()

    def load_other_frame(self):
        self.control_frame = ControlFrame(self)
        self.data_frame = DataShowFrame(self)
        self.control_frame.grid(row=0, column=1, padx=20)
        self.data_frame.grid(row=0, column=0)

        self.control_frame.set_pwm_btn["command"] = self.set_pwm
        self.control_frame.direction_btn["command"] = self.change_direction
        self.control_frame.up_btn["command"] = self.up_pwm
        self.control_frame.down_btn["command"] = self.down_pwm

    def set_pwm(self):
        try:
            pwm = int(self.data_frame.var_input.get())
            if pwm > 255:
                messagebox.showerror("ERROR", "PWM值不能大于255")
            data_storage.update("pwm", pwm)
        except Exception as e:
            print(e)
            messagebox.showerror("ERROR", "输入无效")

    def change_direction(self):
        if data_storage["direction"] == 1:
            data_storage["direction"] = 2
            self.control_frame.direction_btn["text"] = "反转"
        else:
            data_storage["direction"] = 1
            self.control_frame.direction_btn["text"] = "正转"
        self.control_frame.direction_btn.update()

    def up_pwm(self):
        pwm = data_storage["pwm"] + 10
        if pwm > 255:
            return
        data_storage["pwm"] = pwm

    def down_pwm(self):
        pwm = data_storage["pwm"] - 10
        if pwm < 0:
            return
        data_storage["pwm"] = pwm


class MainFrame(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.init_data()
        self.load_other_frame()
        self.bind_data()

    def init_data(self):
        data_storage["pwm"] = 0
        data_storage["direction"] = 1

    def load_other_frame(self):
        self.main_panel = MainPanel(self)
        self.main_panel.grid(row=1, column=0, pady=10)
        self.serial_manage = SerialManager(self)
        self.serial_manage.grid(row=0, column=0)

    def bind_data(self):
        data_storage.register("pwm", lambda x: self.main_panel.data_frame.var_pwm.set(str(x)))
