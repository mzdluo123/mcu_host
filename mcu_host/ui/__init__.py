import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
from mcu_host.mcu.connector import MCUConnector


class ControlFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self.create_widgets()

    def create_widgets(self):
        self.up_btn = ttk.Button(self, text="增加")
        self.up_btn.grid(row=0, column=0, pady=30, ipady=20)
        self.down_btn = ttk.Button(self, text="减少")
        self.down_btn.grid(row=1, column=0,pady = 5, ipady=20)


class DataShowFrame(tk.Frame):
    def __init__(self, master=None, data_name="默认名称"):
        super().__init__(master)
        self.master = master
        self.data_name = data_name
        self.var_input = tk.StringVar()
        self.data_font = tkFont.Font(size=20)
        self.label_font = tkFont.Font(size=15)
        self.var_input.set("text")
        self.create_widgets()

    def create_widgets(self):
        self.label = ttk.Entry(self, font=self.data_font, state=tk.DISABLED, textvariable=self.var_input, width=10)
        self.label.grid(row=0, column=1, ipady=15)
        self.label = ttk.Label(self, font=self.label_font, text=self.data_name)
        self.label.grid(row=0, column=0, padx=10)


class SerialManager(ttk.Frame):
    def __init__(self, master=None, connector: MCUConnector = None):
        super().__init__(master)
        self.master = master
        self.connector = connector
        self.serial_box = ttk.Combobox(self)
