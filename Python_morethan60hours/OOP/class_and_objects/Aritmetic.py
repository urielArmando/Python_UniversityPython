class Arithmetic:
    """ <= docString
    Sum, Rest, Mult, Div
    """

    def __init__(self, operatorA, operatorB):
        self.operatorA = operatorA
        self.operatorB = operatorB

    def sum(self):
        return self.operatorA + self.operatorB

    def rest(self):
        return self.operatorA - self.operatorB

    def mult(self):
        return self.operatorA * self.operatorB

    def div(self):
        return self.operatorA / self.operatorB


arithmetic1 = Arithmetic(5, 3)
print(f'Sum: {arithmetic1.sum()}')
print(f'Rest: {arithmetic1.rest()}')
print(f'Mult: {arithmetic1.mult()}')
print(f'Div: {arithmetic1.div():.2f}')


# Exercise area of rectangle
class Calculate:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return self.base * self.height


base = int(input('Give a base of rectangle: '))
height = int(input('Give a height of rectangle: '))
area1 = Calculate(base, height)

print(f'Area of rectangle: {area1.calculate_area()}')

