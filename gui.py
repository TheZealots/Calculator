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
    
    def create_special_buttons(self):
        self.create_clear_button()
        self.create_delete_button()
        self.create_equal_button()
        self.create_ans_button()
        
    def create_display_labels(self):
        self.equation_label = tk.Label(self.display_frame, text=self.equation, anchor = tk.NW, bg = "#B4D6C1", fg = "#000000", padx = 10, font = ("Verdana", 15))
        self.equation_label.pack(expand=True, fill='both')

        self.answer_label = tk.Label(self.display_frame, text=self.answer, anchor = tk.E, bg = "#B4D6C1", fg = "#000000", padx = 10, font = ("Verdana", 25, 'bold'))
        self.answer_label.pack(expand=True, fill='both')

        return self.equation_label, self.answer_label

    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221, bg="#FFFFFF")
        frame.pack(expand=True, fill="both")
        return frame

    def create_operator_buttons(self):
        index = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text = symbol, bg = "#4E9C81", fg = "#FFEBD2", font = ("Verdana", 15, "bold"), borderwidth=0, command=lambda x=operator: self.append_operator(x))
            button.grid(row=index, column=4, sticky=tk.NSEW)
            index += 1

    def create_number_buttons(self):
        for number, coordinate in self.numbers.items():
            button = tk.Button(self.buttons_frame, text = number, bg= "#358873", fg= "#FFEBD2", font = ("Verdana", 10, "bold"), borderwidth=0, command=lambda x=number: self.append_operator(x)) 
            button.grid(row=coordinate[0], column=coordinate[1], sticky=tk.NSEW)

    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame
    
    def bind_keys(self):
        self.window.bind("<Return>", lambda event: self.evaluate())
        for key in self.numbers:
            self.window.bind(str(key), lambda event, digit=key: self.add_to_expression(digit))

        for key in self.operations:
            self.window.bind(key, lambda event, operator=key: self.append_operator(operator))
   
    def create_clear_button(self):
        button = tk.Button(self.buttons_frame, text = "C", bg = "#4E9C81", fg = "#FFEBD2", font = ("Verdana", 15, "bold"), borderwidth=0, command=self.clear)
        button.grid(row=0, column=1, sticky=tk.NSEW)

    def create_delete_button(self):
        button = tk.Button(self.buttons_frame, text = "DEL", bg = "#4E9C81", fg = "#FFEBD2", font = ("Verdana", 15, "bold"), borderwidth=0, command=self.delete)
        button.grid(row=0, column=2, sticky=tk.NSEW)

    def create_equal_button(self):
        button = tk.Button(self.buttons_frame, text = "=", bg = "#207567", fg = "#FFEBD2", font = ("Verdana", 15, "bold"), borderwidth=0, command=self.evaluate)
        button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)

    def create_ans_button(self):
        button = tk.Button(self.buttons_frame, text = "ANS", bg = "#4E9C81", fg = "#FFEBD2", font = ("Verdana", 15, "bold"), borderwidth=0, command=self.ans)
        button.grid(row=0, column=3, sticky=tk.NSEW)
