"""
my_file = open('file_test.txt', mode='r+')

# Here we read the file
print(my_file.read())

# if we want to read the file again we need to do the seek
my_file.seek(0)
print(my_file.read())

# Here we read line by line
my_file.seek(0)
print(my_file.readline())

# Here we read all the lines
my_file.seek(0)
print(my_file.readlines())

# Close the file
my_file.close()
"""

# Here is the way to work with files and dont worry about closing it
# w : allows us to write to the file
# r : allows us to read from the file
# r+ : allows us to read and write to the file
# a : allows us to append to the file (write at the end)
with open("file_test.txt", mode="a") as mf:
    for i in range(0, 10):
        text = mf.write(f"Hi {i}\n")

with open("./basics/file_test2.txt", mode="r") as mf2:
    print(mf2.read())

try:
    with open("12345.txt", mode="r") as mf:
        print(mf.read())
except FileNotFoundError as e:
    print("File not found")
    raise e
except IOError as e:
    print("IO Error")
    raise e
