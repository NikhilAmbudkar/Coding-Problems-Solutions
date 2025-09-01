class Calculator:
    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation.lower()
    def calculate(self):
        if self.operation == "addition":
            return self.a + self.b
        elif self.operation == "subtraction":
            return self.a - self.b
        elif self.operation == "multiplication":
            return self.a * self.b
        elif self.operation == "division":
            if self.b == 0:
                return "Error: Division by zero is not allowed."
            return self.a / self.b
        else:
            return "Invalid operation! Please choose addition, subtraction, multiplication, or division."
a = float(input("Enter first number (a): "))
b = float(input("Enter second number (b): "))
op = input("Enter operation (addition, subtraction, multiplication, division): ")
calc = Calculator(a, b, op)
result = calc.calculate()
print("Result:", result)
