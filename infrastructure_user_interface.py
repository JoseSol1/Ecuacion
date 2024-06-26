from application_expression_service import ExpressionService

class UserInterface:
    def __init__(self):
        self.expression_service = ExpressionService()

    def run(self):
        while True:
            equation = input("Ingrese una ecuacion en la forma 'ax + b = c', incluyendo los espacios: ")
            if equation=='':
                break
            try:
                result = self.expression_service.solve_linear_equation(equation)
                print(f"El valor de 'x' es: {result}")
            except ValueError as e:
                print(e)

if __name__ == "__main__":
    ui = UserInterface()
    ui.run()
