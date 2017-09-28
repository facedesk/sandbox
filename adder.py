equation = input("enter addition equation with two numbers>")
operands = equation.split("+")
print(float(operands[0].strip()) + float(operands[1].strip()))
