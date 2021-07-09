from calc_final import Kalkyu

import unittest


class CalculatorTest(unittest.TestCase):
    def setUp(self):
        self.calc = Kalkyu()

    def test_clear(self):
        self.calc = Kalkyu()
        self.calc.equation = "690452352"
        a = self.calc.clear()
        self.assertEqual(self.calc.equation, "")


    def test_delete1(self):
        self.calc = Kalkyu()
        self.calc.equation = "690452352"
        a = self.calc.delete()
        self.assertEqual(self.calc.equation, "69045235")

    def test_delete2(self):
        self.calc = Kalkyu()
        self.calc.equation = "690452352"
        a = self.calc.delete()
        self.calc.equation = self.calc.equation + "* 9 * 4 + 7498"
        a = self.calc.evaluate()
        self.assertEqual(self.calc.answer, "2485635958")


    def test_ans1(self):
        self.calc = Kalkyu()
        self.calc.equation = "4 + 2"
        a = self.calc.evaluate()
        a = self.calc.clear()
        self.assertEqual(self.calc.ans, "6")

    def test_ans2(self):
        self.calc = Kalkyu()
        self.calc.equation = "4 + 2"
        a = self.calc.evaluate()
        a = self.calc.clear()
        self.calc.equation  = self.calc.ans + "* 8"
        a = self.calc.evaluate()
        self.assertEqual(self.calc.answer, "48")


    def test_ans3(self):
        self.calc = Kalkyu()
        self.calc.equation = "4 + 2"
        a = self.calc.evaluate()
        a = self.calc.delete()
        a = self.calc.delete()
        a = self.calc.delete()
        self.calc.equation  = self.calc.ans + "* 8"
        a = self.calc.evaluate()
        self.assertEqual(self.calc.answer, "48")


    def test_append_operator1(self):
        self.calc = Kalkyu()
        operator = " * "
        self.calc.equation = "77"
        a = self.calc.append_operator(operator)
        self.assertEqual(self.calc.equation, "77 * ")

    def test_append_operator2(self):
        self.calc = Kalkyu()
        operator = " * "
        self.calc.equation = "77"
        a = self.calc.append_operator(operator)
        a = self.calc.evaluate()
        self.assertEqual(self.calc.answer, "Syntax Error!")
    
    def test_evaluate1(self):
        self.calc = Kalkyu()
        self.calc.answer = ""
        self.calc.equation = "1 + 2 + 3 + 4 + 5"
        a = self.calc.evaluate()
        self.assertEqual(self.calc.answer, "15")        

    def test_evaluate2(self):
        self.calc = Kalkyu()
        self.calc.answer = ""
        self.calc.equation = "1 + 2 + 3 + 4 + "
        a = self.calc.evaluate()
        self.assertEqual(self.calc.answer, "Syntax Error!")


    def test_evaluate3(self):
        self.calc = Kalkyu()
        self.calc.answer = ""
        self.calc.equation = "1 * 5 * 89 * 35 * 46"
        a = self.calc.evaluate()
        self.assertEqual(self.calc.answer, "716450")

    def test_evaluate4(self):
        self.calc = Kalkyu()
        self.calc.answer = ""
        self.calc.equation = "1 *- 5 * 89 */ 35 * 46"
        a = self.calc.evaluate()
        self.assertEqual(self.calc.answer, "Syntax Error!")

    def test_evaluate5(self):
        self.calc = Kalkyu()
        self.calc.answer = ""
        self.calc.equation = "+-//*"
        a = self.calc.evaluate()
        self.assertEqual(self.calc.answer, "Syntax Error!")

if __name__ == "__main__":
    unittest.main()                        



    
