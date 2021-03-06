# Methods vs Functions

# Method
class Ship:
    def __init__(self, name, capacity, cargo):
        self.name = name
        self.capacity = capacity
        self.cargo = int(cargo)

    def sail(self):
        print("{} has sailed!".format(self.name))

    def cap(self):
        print("{} passengers".format(self.capacity))

    def convert_cargo(self):
        return self.cargo * 1000


# function
def sail_function(name):
    print("{} has sailed!".format(name))


def set_cap(capacity):
    print("{} has sailed!".format(capacity))


# creating an instance of the class Ship
# and calling the method sail
black_pearl = Ship("Black Pearl", 800, 2)
black_pearl.sail()
black_pearl.cap()
black_pearl.convert_cargo()
print(black_pearl.convert_cargo())
# calling the function sail_function
sail_function(black_pearl.name)
set_cap(black_pearl.capacity)
# also prints "Black Pearl has sailed!"
