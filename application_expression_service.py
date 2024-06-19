from domain_expression import Expression, Side

class ExpressionService:
    def solve_linear_equation(self, left_value, right_value):
        left_side = Side(left_value, 'x')
        right_side = Side(right_value, 'c')
        expression = Expression(left_side, right_side)
        return expression.solve()
