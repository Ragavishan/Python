def sum_of_square_series(number):
    if number == 0:
        return 0
    else:
        return (number * number) + sum_of_square_series(number - 1)

num = int(input("Please enter any positive number: "))
total = sum_of_square_series(num)
print("The sum of series up to {0} = {1}".format(num, total))
