import tkinter as tk  # 使用Tkinter前需要先导入
from concurrent.futures import ThreadPoolExecutor
from mcu_host.ui.main import MainFrame
from mcu_host.mcu.connector import MCUConnector
from mcu_host.mcu import DataStorage

data = DataStorage()
pool = ThreadPoolExecutor()
window = tk.Tk()


def on_closing():
    pool.shutdown(False)
    window.destroy()


if __name__ == '__main__':
    connector = MCUConnector(data, pool)
    connector.start_receive()
    window.protocol("WM_DELETE_WINDOW", on_closing)
    app = MainFrame(window, serial_connector=connector)
    app.bind_data(data)
    window.title('主窗口')
    window.geometry('500x300')
    window.mainloop()
