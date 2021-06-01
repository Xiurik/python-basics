class User():
    def sing_in(self):
        print('User logged In')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'Wizard {self.name}, Attaching with power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    # def attack(self):
    #     print(
    #         f'Archer {self.name}, Attacking with arrows: arrows left = {self.num_arrows}')

    def run(self):
        print(f'Archer {self.name} is running')

    def check_arrows(self):
        print(f'{self.num_arrows} arrows left')


class HybridBorg(Wizard, Archer):
    # Implementing multiple Inheritance
    def __init__(self, name, power, arrows):
        Wizard.__init__(self, name, power)
        Archer.__init__(self, name, arrows)


merlin = Wizard('Elena', 100)
robin = Archer('Xiurik', 100)
hybrid = HybridBorg('Khale', 50, 30)

hybrid.check_arrows()
hybrid.attack()
hybrid.sing_in()
# merlin.attack()
# merlin.sing_in()

# robin.attack()
# robin.sing_in()

# Here we check if a class is instanciated
# print(isinstance(merlin, Wizard))
# print(isinstance(merlin, User))

# Here will say True cause everything is an instance of an object
# print(isinstance(merlin, object))
