# Dunder methods: Are all the methods that we have available from default with __, this methods can be overrided to
# behave with in a special way, but we should only do that in special cases and in classes

class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.dict = {
            'name': 'Xiurik',
            'has_pets': False
        }
        self.data = ['Hello', 'str', 'dunder']

    # Here we modify the dunder str method, but only applies on Toy class
    def __str__(self):
        return f'{self.color}'

    # Adding this dunder to a class, allow us to call the class like a method, for example action()
    def __call__(self):
        return 'Hello, thanks for calling!'

    # Adding this dunder to a class, allow us to call the class like an array, for example action['name'] from dict
    # or action[1] if we make reference to a list
    def __getitem__(self, i):
        if type(i) == str:
            return self.dict[i]
        else:
            return self.data[i]


action = Toy('red', 12)
# print(action.__str__())
# print(str('Hello'))

# Here we call the class after adding __call__ dunder method
# print(action())

# Here we call the class after adding __getitem__ dunder method
print(action['name'])
