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
        for F in (SIMConnectorPanel, MainPanel, PINInformationPanel):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("SIMConnectorPanel")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class SIMConnectorPanel(tk.Frame):

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


class PINInformationPanel(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        chv1_enabled = True # TODO: add pysim call
        chv1_tries_left = 3 # TODO: add pysim call

        chv1_enabled_label = tk.Label(
            self, text="CHV1 Code enabled: " + str(chv1_enabled))
        chv1_enabled_label.pack()

        chv1_tries_left_label = tk.Label(
            self, text="CHV1 Tries left: " + str(chv1_tries_left))
        chv1_tries_left_label.pack()

        button = tk.Button(self, text="Back to main panel", command=self.returnToMainPanel)
        button.pack()

    def returnToMainPanel(self):
        self.controller.show_frame("MainPanel")


class MainPanel(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Choose operation")
        label.pack(side="top", fill="x", pady=10)

        pin_information_button = tk.Button(self, text="View PIN information",
                           command=lambda: controller.show_frame("PINInformationPanel")) 
        pin_information_button.pack()

        reconnect_button = tk.Button(self, text="Connect to different serial port",
                           command=lambda: controller.show_frame("SIMConnectorPanel"))
        reconnect_button.pack()


if __name__ == "__main__":
    app = PySIMGUI()
    app.mainloop()
