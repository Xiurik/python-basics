# Walrus Operator (:=): It assigns values to variables as part of a larger expression, so usually it is
# used is an expression when something is being valuated like an if, while.
a = 'helllllloooooooooo'

# Here we calculate in the if the len of a and then inside the print we calculate again the len of a
if len(a) > 10:
    print(f'too long {len(a)} elements')
    print()

# Now using the walrus operator, we dont need the len in the print
if (x := len(a)) > 10:
    print(f'too long {x} elements')
    print()

while (y := len(a)) > 1:
    print(y)
    a = a[:-1]  # Remove the last one

print(y)
