## calc logic

  
  def add_to_expression(self, value):
        self.equation += str(value)
        self.update_equation_label()

    def append_operator(self, operator):
        self.equation += str(operator)
        self.update_equation_label()
  
  def evaluate(self):   
        try:
            self.answer = str(eval(self.equation))
            self.ans = self.answer
        except Exception as e:
            self.answer = "Syntax Error!"
        finally:
            self.update_answer_label()
            
  
          
  
