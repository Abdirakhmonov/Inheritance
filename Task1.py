import math

class Calculator:
    def __init__(self, n) -> None:
        self.n = n
    def plus(self, x = 1):
        self.n += x
    def minus(self, x = 1):
        self.n -= x
    def multiply(self, x = 1):
        self.n *= x
    def divide(self, x = 1):
        if x != 0:
            self.n /= x
    def sqrt(self):
        if self.n >= 0:
            self.n = math.sqrt(self.n)
    def pow(self, x = 2):
        self.n **= x
    def mod(self, x = 1):
        if x != 0:
            self.n %= x
    def get_answer(self):
        return self.n
    
n = 10
calc = Calculator(n)

calc.plus(5)
print(calc.get_answer())

calc.plus()
print(calc.get_answer())

calc.mod(2)
print(calc.get_answer())

calc.plus()
print(calc.get_answer())

calc.multiply(100)
print(calc.get_answer())

calc.multiply()
print(calc.get_answer())

calc.minus(40)
print(calc.get_answer())

calc.minus()
print(calc.get_answer())

print(calc.get_answer())