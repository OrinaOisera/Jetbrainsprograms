# Methods vs Functions

# Method
class Ship:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.cargo = 0

    def sail(self):
        print("{} has sailed!".format(self.name))

    def cap(self):
        print("{} passengers".format(self.capacity))


# function
def sail_function(name):
    print("{} has sailed!".format(name))


def set_cap(capacity):
    print("{} has sailed!".format(capacity))


# creating an instance of the class Ship
# and calling the method sail
black_pearl = Ship("Black Pearl", 800)
black_pearl.sail()
black_pearl.cap()

# calling the function sail_function
sail_function(black_pearl.name)
set_cap(black_pearl.capacity)
# also prints "Black Pearl has sailed!"
