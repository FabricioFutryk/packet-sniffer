from libs.sniffer import PacketSniffer
from gui.main import GUI
import ctypes
import sys
from threading import Thread


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


if __name__ == "__main__":
    if is_admin():
        gui = GUI()
        sniffer = PacketSniffer(gui)

        sniffer_thread = Thread(target=sniffer.start_sniffing)
        sniffer_thread.start()

        gui.render()
    else:
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, " ".join(sys.argv), None, 1)
