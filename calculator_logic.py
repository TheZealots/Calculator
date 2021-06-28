## calc logic


    def add_to_expression(self, value):
        self.equation += str(value)
        self.update_equation_label()

    def append_operator(self, operator):
        self.equation += str(operator)
        self.update_equation_label()
    
    def create_special_buttons(self):
        self.create_clear_button()
        self.create_delete_button()
        self.create_equal_button()
        self.create_ans_button()

    def clear(self):
        self.equation = ""
        self.ans = self.answer
        self.answer = ""
        self.update_equation_label()
        self.update_answer_label()

  	def evaluate(self):   
        try:
            self.answer = str(eval(self.equation))
            self.ans = self.answer
        except Exception as e:
            self.answer = "Syntax Error!"
        finally:
            self.update_answer_label()
            
  
          
  
