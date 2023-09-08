# unlimited number of arguments/Keyworded arguments
# *makes the args to be a tuple.
# ** makes the kwargs to be a dictionary.
def add(*args):
    num = 0
    for n in args:
        num += n
    return num


def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    return n


number_a = add(2, 3, 4, 5)
print(number_a)
number_c = calculate(2, add=3, multiply=5)
print(number_c)


class Car:

    def __init__(self, **kwargs):
        # self.make = kwargs["make"]
        # self.model = kwargs["model"]
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        # get method will at least give me an None instead Error.

my_car = Car(make="Nissan")
print(my_car.model)
