import unittest
from application_expression_service import ExpressionService

class TestExpressionTree(unittest.TestCase):

    # def test_solve_equation(self):
    #     service= ExpressionService()
    #     result= service.solve_linear_equation("x + 3 = 0")
    #     self.assertEqual(result, "x = -3")
    
    # def test_invalid_equation(self):
    #     service= ExpressionService()
    #     result= service.solve_linear_equation("x + 3")
    #     self.assertEqual(result, "La ecuacion debe incluir un =")

    # def test_missing_x(self):
    #     service= ExpressionService()
    #     result= service.solve_linear_equation("3 = 0")
    #     self.assertEqual(result, "La ecuacion debe incluir solo una incognita x")

    # def test_invalid_variable(self):
    #     service= ExpressionService()
    #     result= service.solve_linear_equation("x + 2 - 3 = 0")
    #     self.assertEqual(result, "La expresion no cumple con el formato correcto")

    # def test_complex_equation(self):
    #     service= ExpressionService()
    #     result= service.solve_linear_equation("(x + 3) * 2 =0")
    #     self.assertEqual(result, "La expresion no cumple con el formato correcto")   
    def test_simple_equation(self):
        service = ExpressionService()
        result = service.solve_linear_equation("x = 0")
        self.assertEqual(result, 0)

    def test_equation(self):
        service=ExpressionService()
        result= service.solve_linear_equation("x + 2 = 0")
        self.assertEqual(result, -2)
    
    def test_equation_no_equal(self):
        service=ExpressionService()
        result= service.solve_linear_equation("x + 2  5")
        self.assertEqual(result, "La ecuacion debe incluir un =")

    def test_equation_two_equal(self):
        service=ExpressionService()
        result= service.solve_linear_equation("x + 2 = = 5")
        self.assertEqual(result, "La ecuacion debe incluir un =")
    
    def test_equation_negative(self):
        service=ExpressionService()
        result= service.solve_linear_equation("x + 4 = 0")
        self.assertEqual(result, -4)

    def test_equation_coefficient(self):
        service=ExpressionService()
        result= service.solve_linear_equation("2x + 4 = 0")
        self.assertEqual(result, -1)

    def test_equation_two_x(self):
        service=ExpressionService()
        result= service.solve_linear_equation("2x + 4x = 8")
        self.assertEqual(result, "La ecuacion debe incluir solo una x")

    



if __name__ == "__main__":
    unittest.main()
