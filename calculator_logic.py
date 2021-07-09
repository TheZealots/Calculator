## calc logic

    # kani nga function kay kanang taga pindot ug button sa user kay madagdag siya didtos eqaution
    def add_to_expression(self, value):
        self.equation += str(value)
        self.update_equation_label()
    # kani same sa anang sa babaw pero para sa operators (+, -, /, *)
    def append_operator(self, operator):
        self.equation += str(operator)
        self.update_equation_label()
    # kini kay kanang pang delete pero as a whole, like limpyo jud ang whole calcu pero i-remember niya tung last nga answer nimo
    def clear(self):
        self.equation = ""
        self.ans = self.answer
        self.answer = ""
        self.update_equation_label()
        self.update_answer_label()
    # kani kay pang delete isa-isa, pero if gamiton nimo ni parehas sa clear (kanang para madelete tanan naas expression), i-remember pud niya imong last answer
    def delete(self):
        if len(self.equation) != 0:
            self.list1 = []
            self.list1[:0] = self.equation
            self.equation = "".join(self.list1[:-1])
            self.update_equation_label()
        else:
            self.ans = self.answer

    # kini kay tung pang solve na sa equation         
    def evaluate(self):   
        try:
            self.answer = str(eval(self.equation))
            self.ans = self.answer
        except Exception as e:
            self.answer = "Syntax Error!"
        finally:
            self.update_answer_label()
    # kini katong ibalik niya imong last answer para magamit nimo siya sa equation
    def ans(self):
        self.equation = self.equation + self.ans
        self.update_answer_label()
        self.update_equation_label()
    # pang - update sa answer
    def update_answer_label(self):
        self.answer_label.config(text=self.answer[:])
    # pang - update sa equation
    def update_equation_label(self):
        equation = self.equation
        for operator, symbol in self.operations.items():
            equation = equation.replace(operator, f' {symbol} ')
        self.equation_label.config(text = equation)
    # para mag run <33    
    def run(self):
        self.window.mainloop()

        
if __name__ == "__main__":
    calc = Kalkyu()
    calc.run()   
           
            
  
          
  
