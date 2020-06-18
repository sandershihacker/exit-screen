#!/usr/bin/env python

import os
import sys
import subprocess
from PIL import ImageTk, Image
if sys.version_info[0] == 2:  # Just checking your Python version to import Tkinter properly.
    from Tkinter import *
else:
    from tkinter import *


class PowerControls:
    def __init__(self):
        pass

    def get_power_function(self, name):
        if name == "shutdown":
            return self.shutdown
        elif name == "restart":
            return self.restart
        elif name == "sleep":
            return self.sleep
        elif name == "logout":
            return self.logout
        elif name == "lock":
            return self.lock
        return None

    def lock(self, event):
        subprocess.call(["i3lock"])
        sys.exit()
    
    def shutdown(self, event):
        subprocess.call(["shutdown", "now"])

    def restart(self, event):
        subprocess.call(["reboot"])
    
    def logout(self, event):
        subprocess.call(["i3-msg", "exit"])

    def sleep(self, event):
        subprocess.call(["i3lock"])
        subprocess.call(["systemctl", "suspend"])
        sys.exit()


class ExitScreen:

    def __init__(self):
        self.define_constants()
        self.tk = Tk()
        self.tk.title(self.title)
        self.frame = Frame(master=self.tk, background=self.background_color)
        self.set_buttons()
        self.bind_keys()
        self.tk.wait_visibility(self.tk)
        self.set_style()
        self.frame.place(relx=.5, rely=.5, anchor="c")

    def define_constants(self):
        self.background_color = "#202020"
        self.icon_size = (72, 72)
        self.title = "Exit Screen"

    def set_style(self):
        self.tk.attributes("-fullscreen", True)
        self.tk.attributes("-alpha", 0.8)
        self.tk["bg"] = self.background_color
    
    def bind_keys(self):
        self.tk.bind("<Escape>", self.destroy)
        self.tk.bind("<s>", self.get_power_function("shutdown"))
        self.tk.bind("<r>", self.get_power_function("restart"))
        self.tk.bind("<h>", self.get_power_function("sleep"))
        self.tk.bind("<q>", self.get_power_function("logout"))
        self.tk.bind("<l>", self.get_power_function("lock"))
        self.tk.bind("<Button>", self.destroy)
    
    def get_power_function(self, name):
        power_controls = PowerControls()
        power_fn = power_controls.get_power_function(name)
        if power_fn is not None:
            return power_fn
        return self.destroy
    
    def set_buttons(self):
        power_options = ["shutdown", "restart", "sleep", "logout", "lock"]
        dir_path = os.path.dirname(os.path.realpath(__file__))
        for i in range(len(power_options)):
            power_option = power_options[i]

            self.tk.columnconfigure(i)
            self.tk.rowconfigure(1)
            frame = Frame(master=self.frame)
            frame.grid(row=1, column=i, padx=40)
            image_path = os.path.join(dir_path, "icons", power_option + ".png")
            img = ImageTk.PhotoImage(ImageTk.Image.open(image_path).resize(self.icon_size))
            lab = Label(
                frame,
                background=self.background_color,
                image=img)
            lab.image = img
            lab.pack()
            lab.bind("<Button>", self.get_power_function(power_option))
    
    def start(self):
        self.tk.mainloop()

    def destroy(self, event=None):
        sys.exit()

if __name__ == '__main__':
    app = ExitScreen()
    app.start()