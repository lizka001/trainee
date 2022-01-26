class MagicClass:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        return str(self.val) + str(other.val)

    def __sub__(self, other):
        return self.val - other.val

    def __mul__(self, other):
        return self.val * other.val

    def __eq__(self, other):
        return self.val == other

    def __truediv__(self, other):
        return '{first}/{second}'.format(first=self.val, second=other.val)

    def __pow__(self, power, modulo=None):
        return self.val ** power

    def __str__(self):
        return 'object - {value}'.format(value=self.val)

    def __lt__(self, other):
        return self.val > other.val

# tests
obj_27 = MagicClass(27)
obj_3 = MagicClass(3)
obj_9 = MagicClass(9)


assert obj_27 + obj_3 == '273'
assert obj_27 - obj_3 == 24
assert obj_27 == obj_3 * obj_9
assert obj_27 / obj_3 == '27/3'
assert obj_3 ** 2 == 9
assert str(obj_27) == 'object - 27'
assert str(obj_3) == 'object - 3'
# The test doesn't pass, because 27 is bigger than 3
assert obj_27 < obj_3
