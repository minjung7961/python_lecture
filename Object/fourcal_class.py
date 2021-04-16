class FourCal:
    def set_data(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result set_data.first + self.second
a = FourCal()
a.set_data(4,2)
b = a.add()
print(b)
