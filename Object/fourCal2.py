class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def add(self):
         result = self.first + self.second
         return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result


x = int(input("첫번째 숫자"))
y = int(input("두번째 숫자"))
a = FourCal(x,y)

print(f'두수의 합은 {a.add()}')
print(f'두수의 곱은 {a.mul()}')
print(f'두수의 차는 {a.sub()}')
print(f'두수의 나눈 값은 {a.div()}')