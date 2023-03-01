# Error Handling: https://docs.python.org/3/library/exceptions.html

while True:
    try:
        age = int(input("whats your age? "))
        10 / age
    except ValueError:
        print("Please enter a valid age.")
    except ZeroDivisionError:
        print("Please enter a number > 0.")
    else:  # Executes if no exception is raised
        print("Thank you.")
        break
    finally:  # This part of the code will execute at the end no matter what!
        print("This is the end.")

# def sum(n1, n2):
#     try:
#         return n1 + n2
#     # except TypeError as err:
#     except (TypeError, ZeroDivisionError) as err:
#         print(f'Please enter numbers: {err}')
#         return ''

# print(sum(1, 'h'))
