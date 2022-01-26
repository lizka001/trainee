# implement generator which count fibonacci numbers


def fibon_generator(count: int):
    first_number, second_number = 0, 1
    for i in range(count):
        yield first_number
        first_number, second_number = second_number, first_number + second_number


assert list(fibon_generator(8)) == [0, 1, 1, 2, 3, 5, 8, 13]

print('Success')
