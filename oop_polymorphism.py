# Polymorphism: is the ability of an object to take on many forms. The most common use of polymorphism in OOP
# occurs when a parent class reference is used to refer to a child class object, sharing method names.
class User(object):
    def __init__(self, email):
        self.email = email

    def sing_in(self):
        print('User logged In')


class Wizard(User):
    def __init__(self, name, power, email):
        # Here we call the parent init using its name
        # User.__init__(self, email)
        # Here we call the parent init using Super (best peactice) and doesnt need the self
        super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        print(f'Wizard {self.name}, Attaching with power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(
            f'Archer {self.name}, Attacking with arrows: arrows left = {self.num_arrows}')


merlin = Wizard('Elena', 100, 'elena@gmail.com')
robin = Archer('Xiurik', 100)


def player_attack(char):
    # Here we call the method attack from different characters, this polymorphism
    char.attack()


player_attack(merlin)
player_attack(robin)
print(merlin.email)

# Instrospection: Allow us to inspect an object more detailed, to see what we have access too
print(dir(merlin))
