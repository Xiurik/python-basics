from functools import reduce

# 1 Capitalize all of the pet names and print the list
my_pets = ["sisi", "bibi", "titi", "carla"]


def capitalize(item):
    """
    Capitalize Letters
    """
    return item.upper()


print(list(map(capitalize, my_pets)))

# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ["a", "b", "c", "d", "e"]
my_numbers = [5, 4, 3, 2, 1]

my_numbers.sort()
print(list(zip(my_numbers, my_strings)))

# Teachers solution
print(list(zip(sorted(my_numbers), my_strings)))

# 3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]


def get_score(item):
    """
    Return scores over 50
    """
    if item > 50:
        return True
    else:
        return False


# Teacher Method


def get_score2(score):
    """
    Return scores over 50
    """
    return score > 50


print(list(filter(get_score, scores)))
print(list(filter(get_score2, scores)))

# 4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?


def accumulator(acc, item):
    """
    A function to test REDUCE
    """
    return acc + item


total_numbers = reduce(accumulator, my_numbers, 0)
total_scores = reduce(accumulator, scores, 0)
print(total_numbers + total_scores)

# Teacher solution
print(reduce(accumulator, (my_numbers + scores)))
