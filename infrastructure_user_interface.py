from application_expression_service import ExpressionService

class UserInterface:
    def __init__(self):
        self.expression_service = ExpressionService()

    def run(self):
        while True:
            left_value = input("Ingrese el valor del lado izquierdo (deje en blanco para salir): ")
            if left_value == '':
                break
            right_value = input("Ingrese el valor del lado derecho: ")

            try:
                result = self.expression_service.solve_linear_equation(int(left_value), int(right_value))
                print(f"El valor de 'x' es: {result}")
            except ValueError as e:
                print(e)

if __name__ == "__main__":
    ui = UserInterface()
    ui.run()
