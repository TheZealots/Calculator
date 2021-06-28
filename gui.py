# gui code
import tkinter as tk



class Kalkyu:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x500") # window size of calculator
        self.window.resizable(True, True) # resizable in width and length
        self.window.title("ZealotsCalc") # calculator name


        self.equation = ""
        self.answer = ""
        self.display_frame = self.create_display_frame()

        self.label = self.create_display_labels()
