# square a list
list_square = [1, 2, 3, 4, 5, 6]
print('Squared list: ', list(map(lambda item: item ** 2, list_square)))

# sort a list based on the second value of the tuple
list_sorting = [(4, 5), (0, 1), (6, 6), (2, 3), (8, -1)]
list_sorting.sort(key=lambda item: item[1])
print(list_sorting)
