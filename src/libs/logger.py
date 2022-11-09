import configparser
from libs.utils import Utils
import tkinter as tk
import os
import sys


class Logger():
    def __init__(self, gui):
        self.gui = gui

        config = configparser.ConfigParser()
        path = os.path.dirname(os.path.abspath(sys.argv[0]))
        configPath = os.path.join(path, "config.ini")

        config.read(configPath)

        if config["FILTERS"].get("source_ports") is not None:
            self.sP = set()

            for arg in config["FILTERS"].get("source_ports").split(","):
                if ":" in arg:
                    start, end = map(int, arg.split(":"))
                    self.sP.update(set(range(start, end)))
                else:
                    self.sP.add(int(arg))
        else:
            self.sP = None

        if config["FILTERS"].get("destination_ports") is not None:
            self.dP = set()

            for arg in config["FILTERS"].get("destination_ports").split(","):
                if ":" in arg:
                    start, end = map(int, arg.split(":"))
                    self.dP.update(set(range(start, end)))
                else:
                    self.dP.add(int(arg))
        else:
            self.dP = None

    def check_filters(self, ipv4_header, packet):
        if ipv4_header["protocol"] in ["TCP", "UDP"]:
            if self.sP is not None and packet["sourcePort"] not in self.sP:
                return False
            if self.dP is not None and packet["destinationPort"] not in self.sdP:
                return False

        return True

    def log(self, ipv4_header, packet):
        if not self.check_filters(ipv4_header, packet):
            return

        protocol, ttl = ipv4_header["protocol"], ipv4_header["ttl"]
        source, target = ipv4_header["source"], ipv4_header["target"]

        source_port, destination_port = packet["sourcePort"], packet["destinationPort"]

        self.gui.text.configure(state=tk.NORMAL)
        self.gui.text.insert(tk.INSERT, f"[{protocol}] ", protocol)
        self.gui.text.insert(tk.INSERT, "{}:{} -> {}:{} \tTTL: {}\n".format(
            source, source_port, target, destination_port, ttl))

        if protocol == "TCP":
            self.gui.text.insert(tk.INSERT, "\t\t")
            for flag in packet["flags"]:
                if packet["flags"][flag] != 0:
                    self.gui.text.insert(
                        tk.INSERT, f" {flag.upper()} ", "activeFlag")
                else:
                    self.gui.text.insert(
                        tk.INSERT, f" {flag.upper()} ", "disabledFlag")
            self.gui.text.insert(tk.INSERT, "\n")

        self.gui.text.configure(state=tk.DISABLED)
