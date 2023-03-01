# Lambda expressions:
# Lambda expressions: is a small anonymous function. A lambda function can take any number of arguments,
# but can only have one expression (can be used just once). The power of lambda is better shown when
# you use them as an anonymous function inside another function, mostly used in MAP, ZIP, FILTER, REDUCE
# lambda ITEM: ACTION

numbers = [1, 2, 3, 4, 5, 6]
names = ["xiurik", "jhon", "fred", "aaron", "elena", "ana", "kate"]


def multiply_map(item):
    # This is a normal function and it will be turned into a lambda function
    return item * 2


mapped_lamb = list(map(lambda item: item * 2, numbers))
mapped_lamb_upper = list(map(lambda item: item.upper(), names))
print("MAP:", mapped_lamb)
print("MAP:", mapped_lamb_upper)
