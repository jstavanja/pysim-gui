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
        for F in (SIMConnectorPanel, MainPanel, PINInformationPanel, MandatoryFieldsPanel):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("SIMConnectorPanel")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

    def returnToMainPanel(self):
        self.show_frame("MainPanel")


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

        self.controller.returnToMainPanel()


class PINInformationPanel(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        chv1_enabled = True  # TODO: add pysim call
        chv1_tries_left = 3  # TODO: add pysim call

        chv1_enabled_label = tk.Label(
            self, text="CHV1 Code enabled: " + str(chv1_enabled))
        chv1_enabled_label.pack()

        chv1_tries_left_label = tk.Label(
            self, text="CHV1 Tries left: " + str(chv1_tries_left))
        chv1_tries_left_label.pack()

        button = tk.Button(self, text="Back to main panel",
                           command=self.controller.returnToMainPanel)
        button.pack()


class MandatoryFieldsPanel(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        value_ICCID = 0  # TODO: add pysim call
        value_LP = 0  # TODO: add pysim call
        value_IMSI = 0  # TODO: add pysim call
        value_KC = 0  # TODO: add pysim call
        value_HPLMN = 0  # TODO: add pysim call
        value_SST = 0  # TODO: add pysim call
        value_BCCH = 0  # TODO: add pysim call
        value_ACC = 0  # TODO: add pysim call
        value_FPPLMN = 0  # TODO: add pysim call
        value_LOCI = 0  # TODO: add pysim call
        value_AD = 0  # TODO: add pysim call
        value_Phase = 0  # TODO: add pysim call

        label_ICCID = tk.Label(self, text="ICCID: " + str(value_ICCID))
        label_ICCID.pack()

        label_LP = tk.Label(self, text="LP: " + str(value_LP))
        label_LP.pack()

        label_IMSI = tk.Label(self, text="IMSI: " + str(value_IMSI))
        label_IMSI.pack()

        label_KC = tk.Label(self, text="KC: " + str(value_KC))
        label_KC.pack()

        label_HPLMN = tk.Label(self, text="HPLMN: " + str(value_HPLMN))
        label_HPLMN.pack()

        label_SST = tk.Label(self, text="SST: " + str(value_SST))
        label_SST.pack()

        label_BCCH = tk.Label(self, text="BCCH: " + str(value_BCCH))
        label_BCCH.pack()

        label_ACC = tk.Label(self, text="ACC: " + str(value_ACC))
        label_ACC.pack()

        label_FPPLMN = tk.Label(self, text="FPPLMN: " + str(value_FPPLMN))
        label_FPPLMN.pack()

        label_LOCI = tk.Label(self, text="FPPLMN: " + str(value_LOCI))
        label_LOCI.pack()

        label_AD = tk.Label(self, text="AD: " + str(value_AD))
        label_AD.pack()

        label_Phase = tk.Label(self, text="Phase: " + str(value_Phase))
        label_Phase.pack()

        button = tk.Button(self, text="Back to main panel",
                           command=self.controller.returnToMainPanel)
        button.pack()


class MainPanel(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Choose operation")
        label.pack(side="top", fill="x", pady=10)

        pin_information_button = tk.Button(self, text="View PIN information",
                                           command=lambda: controller.show_frame("PINInformationPanel"))
        pin_information_button.pack()

        pin_information_button = tk.Button(self, text="View mandatory fields information",
                                           command=lambda: controller.show_frame("MandatoryFieldsPanel"))
        pin_information_button.pack()

        reconnect_button = tk.Button(self, text="Connect to different serial port",
                                     command=lambda: controller.show_frame("SIMConnectorPanel"))
        reconnect_button.pack(pady=20)


if __name__ == "__main__":
    app = PySIMGUI()
    app.mainloop()
