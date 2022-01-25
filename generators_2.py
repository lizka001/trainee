# implement generator by class which count fibonacci numbers
# be careful here, wrong implementation may cause memory leak

class FibonGenerator:
    def __init__(self, count: int):
        self.count = count
        self.first_number, self.second_number = 0, 1
    def __iter__(self):
        for i in range(self.count):
            yield self.first_number
            self.first_number, self.second_number = self.second_number, self.first_number + self.second_number

# tests
fibon_generator = FibonGenerator(8)

assert list(fibon_generator) == [0, 1, 1, 2, 3, 5, 8, 13]

print('Success')
