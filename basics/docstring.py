# Docstring: Is a way to comment a method so we see information about the method when we use it
def calculate_iva(amount, iva):
    """
    This function will return you the IVA of an amount
    """
    return round((((iva / 100) + 1) * amount) - amount, 2)


print(calculate_iva(345, 15))

# To see the documentation we use
print(calculate_iva.__doc__)
