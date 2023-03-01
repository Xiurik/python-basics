# Abstraction: hides information and you get access to only what is necesary


class PlayerCharacter:
    # Class Object Attribute
    membership = True

    # self refers to the Class, in this case the __init__ is a constructor
    def __init__(self, name, age, isVIP=False):
        self.membership = isVIP
        self.name = name
        self.age = age
        self.run()

    def run(self):
        if self.membership:
            print("Run my loved VIP")
        else:
            print(f"Run dude, you are {self.age}")

    @classmethod  # This is a decorator
    def adding_things(cls, n1, n2, isVIP=False):
        # cls work as self in the above code and is mandatory and have access to class attributes,
        # it refers to class PlayerCharacter, but @classmethod can be called without instanciating the whole class,
        # we can do PlayerCharacter.adding_things(2,3) and it will return 5
        return cls("Tom", n1 + n2, isVIP)

    @staticmethod  # This is a decorator
    # This is a static method and doesnt have access to the cls (class attributes), it can be used like classmethod
    def adding_method(n1, n2):
        return (n1 + n2,)


# player1 = PlayerCharacter('Xiurik', 30, True)  # Normal way
player2 = PlayerCharacter.adding_things(2, 3)  # Using classmethod


# Exercise
# Given the below class:
class Cat:
    species = "mammal"

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat("Jhon", 12)
cat2 = Cat("Carol", 16)
cat3 = Cat("Xah", 22)

# Part of my solution
cats = [cat1, cat2, cat3]
ages = []

# 2 Create a function that finds the oldest cat


def find_oldest_cat():  # My method (Noob Method)
    for item in cats:
        ages.append(item.age)

    ages.sort()
    return f"The oldest cat is {ages[-1]} years old."


def get_oldest_cat(*args):  # Teachers Method (Pro Method)
    return max(args)


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
# print(find_oldest_cat())
# print( f"The oldest cat is {get_oldest_cat(cat1.age, cat2.age, cat3.age)} years old.")
