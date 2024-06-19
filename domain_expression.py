class Expression:
    def __init__(self, left_side, right_side):
        self.left_side = left_side
        self.right_side = right_side

    def solve(self):
        if self.left_side.variable == 'x':
            return self.right_side.value
        elif self.right_side.variable == 'x':
            return self.left_side.value
        else:
            raise ValueError("No es una ecuación lineal de primer grado.")

class Side:
    def __init__(self, value, variable):
        self.value = value
        self.variable = variable
