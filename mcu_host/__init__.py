import tkinter as tk  # 使用Tkinter前需要先导入

from mcu_host.mcu.connector import MCUConnector
from mcu_host.mcu import DataStorage


def __on_closing():
    connector.close_serial()
    window.destroy()


window = tk.Tk()
connector = MCUConnector()
window.protocol("WM_DELETE_WINDOW", __on_closing)
