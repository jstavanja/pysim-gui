import Tkinter as tk
import tkMessageBox


APP_TITLE = "PySIM GUI"


class PySIMGUI(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title(APP_TITLE)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (SIMConnector, MainPanel):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("SIMConnector")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class SIMConnector(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        com_port_entry_label = tk.Label(
            self, text="Enter the name of the COM port where the SIM card is connected:")
        com_port_entry_label.pack()

        com_port_entry = tk.Entry(self)
        com_port_entry.pack()

        button = tk.Button(self, text="Connect", command=self.connect)
        button.pack()

    def connect(self):
        # connect to serial port

        # FAIL: open error warning window
        # tkMessageBox.showwarning("Fail", "Couldn't connect to port.")
        # return

        # SUCCESS: close current SIM Connector frame and open main panel
        tkMessageBox.showinfo("Success", "Successfully connected to port!")

        self.controller.show_frame("MainPanel")


class MainPanel(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Choose operation")
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Connect to different serial port",
                           command=lambda: controller.show_frame("SIMConnector"))
        button.pack()


if __name__ == "__main__":
    app = PySIMGUI()
    app.mainloop()
