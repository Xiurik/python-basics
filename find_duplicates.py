# Check for duplicates in list:
the_list = ['a', 'b', 'c', 'b', 'd', 'e', 'f', 'c']
duplicates = []
the_list.sort()

for i in range(0, len(the_list)):
    if the_list[i] == the_list[i - 1]:
        duplicates.append(the_list[i])

print(duplicates)

# Teacher solution
duplicates.clear()
for value in the_list:
    if the_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)
