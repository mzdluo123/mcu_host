from mcu_host import window
from mcu_host.ui.main import MainFrame
from mcu_host.mcu import data_storage

if __name__ == '__main__':
    app = MainFrame(window)
    app.bind_data(data_storage)
    window.title('主窗口')
    window.geometry('500x300')
    window.mainloop()
