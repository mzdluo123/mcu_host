from mcu_host import window
from mcu_host.ui.main import MainFrame


if __name__ == '__main__':
    app = MainFrame(window)

    window.title('主窗口')
    window.geometry('500x300')
    window.mainloop()
