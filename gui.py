# gui code
import tkinter as tk



class Kalkyu:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x500") # calculator window size
        self.window.resizable(True, True) # resizability of width and length of calculator
        self.window.title("Zealot Calculator") # calculator name


        self.equation = ""
        self.answer = ""
        self.display_frame = self.create_display_frame()

        self.label = self.create_display_labels()
        
        self.numbers = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 2), '.': (4, 1)
        }
        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": " - ", "+": "+"}
        self.buttons_frame = self.create_buttons_frame()
        self.buttons_frame.rowconfigure(0, weight=2)
        for x in range(1, 5):
            self.buttons_frame.rowconfigure(x, weight=2)
            self.buttons_frame.columnconfigure(x, weight=2)
        self.create_number_buttons()
        self.create_operator_buttons()
        self.create_special_buttons()
        self.bind_keys()
