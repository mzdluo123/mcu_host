import tkinter as tk
from tkinter import ttk
from .. import connector
from serial.tools import list_ports
from tkinter import messagebox


class SerialManager(ttk.Frame):
    def __init__(self, master=None ):
        super().__init__(master)
        self.master = master

        self.var_baudrate = tk.IntVar()
        self.var_baudrate.set(9600)
        self.create_widgets()
        self.refresh_serial_list()

    def create_widgets(self):
        self.label1 = ttk.Label(self, text="串口选择")
        self.label1.grid(row=0, column=0, padx=2)

        self.serial_box = ttk.Combobox(self)
        self.serial_box.grid(row=0, column=1)

        self.label2 = ttk.Label(self, text="波特率")
        self.baudrate_input = ttk.Entry(self, textvariable=self.var_baudrate)
        self.label2.grid(row=1, column=0)
        self.baudrate_input.grid(row=1, column=1)

        self.refresh_btn = ttk.Button(self, text="刷新串口列表", command=self.refresh_serial_list)
        self.refresh_btn.grid(row=0, column=2, padx=2, ipady=20, rowspan=2)

        self.start_btn = ttk.Button(self, text="开启串口", command=self.start_serial)
        self.start_btn.grid(row=0, column=3, padx=2)

        self.stop_btn = ttk.Button(self, text="关闭串口", command=self.stop_serial)
        self.stop_btn.grid(row=1, column=3, padx=2)
        self.stop_btn["state"] = tk.DISABLED

    def refresh_serial_list(self):
        ports = [i.device for i in list_ports.comports()]
        self.serial_box["values"] = ports
        self.serial_box.update()
        if len(ports) > 0:
            self.serial_box.current(0)

    def start_serial(self):
        try:
            connector.serial_port = self.serial_box.get()
            connector.baudrate = self.var_baudrate.get()
            connector.open_serial()
            self.start_btn["state"] = tk.DISABLED
            self.stop_btn["state"] = tk.NORMAL
        except Exception as e:
            messagebox.showerror("ERROR",e)

    def stop_serial(self):
        try:
            connector.close_serial()
            self.stop_btn["state"] = tk.DISABLED
            self.start_btn["state"] = tk.NORMAL
        except Exception as e:
            messagebox.showerror("ERROR", e)
