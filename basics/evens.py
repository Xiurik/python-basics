# Find the highest item in the list, only evens
def highest_even(li):
    even = []
    for i in li:
        if i % 2 == 0:
            even.append(i)
    return max(even)


print(highest_even([10, 2, 3, 4, 8, 11]))
