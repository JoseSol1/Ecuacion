import unittest
from application_expression_service import ExpressionService

class TestExpressionTree(unittest.TestCase):
    def test_simple_equation(self):
        service = ExpressionService()
        result = service.solve_linear_equation(0, 5)
        self.assertEqual(result, 5)

if __name__ == "__main__":
    unittest.main()
