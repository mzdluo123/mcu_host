import tkinter as tk  # 使用Tkinter前需要先导入
from concurrent.futures import ThreadPoolExecutor
from mcu_host.ui import SerialManager

from mcu_host.mcu import DataStorage

data = DataStorage()
pool = ThreadPoolExecutor()
window = tk.Tk()


def on_closing():
    pool.shutdown(False)
    window.destroy()


if __name__ == '__main__':

    app = SerialManager(window)
    window.title('主窗口')
    window.geometry('500x300')
    window.mainloop()
