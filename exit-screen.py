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
            pass
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


class ExitScreen:

    def __init__(self):
        self.define_constants()

        self.tk = Tk()
        self.tk.title(self.title)
        self.frame = Frame(master=self.tk, background=self.background_color)
        self.frame.place(relx=.5, rely=.5, anchor="c")
        self.tk.wait_visibility(self.tk)

        self.set_buttons()
        self.bind_keys()
        self.set_style()

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
    
    def get_power_function(self, name):
        power_controls = PowerControls()
        power_fn = power_controls.get_power_function(name)
        if power_fn is not None:
            return power_fn
        return self.destroy
    
    def set_buttons(self):
        # img = ImageTk.PhotoImage(file="icons/lock.png")
        window = self.tk
        power_options = ["shutdown", "restart", "sleep", "logout", "lock"]
        for i in range(len(power_options)):
            power_option = power_options[i]

            window.columnconfigure(i)
            window.rowconfigure(1)
            frame = Frame(master=self.frame)
            frame.grid(row=1, column=i, padx=40)
            
            img = ImageTk.PhotoImage(ImageTk.Image.open("icons/" + power_option + ".png").resize(self.icon_size))
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