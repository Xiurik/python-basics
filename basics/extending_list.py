# We make a SuperList class that behaves like a list, to achieve it we just need to use inheritance with list
# with this our class can behave like a list because of inheritance
class SuperList(list):

    def __len__(self):
        return 1000


sl1 = SuperList()
sl1.append(3)

print(len(sl1))
print(sl1)

# issubclass to verify
print(issubclass(SuperList, list))
