class Calculator:
    # The class represents a calculator that performs basic arithmetic operations

    a = 0
    b = 0

    def addition(self):
        return self.a + self.b

    def subtraction(self):
        return self.a - self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        return self.a / self.b

# Creating an instance
calculator = Calculator()
print("Enter the 1st number: ", end="")
a = float(input())
calculator.a = a
print("Enter the 2nd number: ", end="")
b = float(input())
calculator.b = b

# Output
print(f"Sum: {calculator.addition()}")
print(f"Difference: {calculator.subtraction()}")
print(f"Product: {calculator.multiplication()}")
print(f"Quotient: {calculator.division()}")