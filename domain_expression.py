class Expression:
    def __init__(self, equation):
        self.equation = equation

    def solve(self):

        if self.equation.count('=')!= 1:
            return "La ecuacion debe incluir un ="
        if self.equation.count('x')!=1:
            return "La ecuacion debe incluir solo una x"

        left_side, right_side= self.equation.split('=')
        
        left_values= left_side.split()       
        right_values= int(right_side.strip())
        x_coefficient=0
        constant=0

        for value in left_values:
            if 'x' in value:
                if value=='x':
                    x_coefficient +=1
                elif value =='-x':
                    x_coefficient-=1
                else:
                    x_coefficient+= int(value.replace('x',''))
            elif value.isdigit() or (value.startswith('-') and value [1:].isdigit()):
                constant+= int(value)
        return (right_values-constant)/x_coefficient
# class Side:
#     def __init__(self, value, variable):
#         self.value = value
#         self.variable = variable
