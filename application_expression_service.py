from domain_expression import Expression

class ExpressionService:
    def solve_linear_equation(self, equation):
        expression = Expression(equation)
        return expression.solve()
