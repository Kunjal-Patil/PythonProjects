"""
Write a program in Python to accept from user the number of Fibonacci numbers to be generated and print the Fibonacci series.
"""

# accept the number of fibonacci number to calculated from the user
print("""Welcome user!
 This program lets you find the fibonacci numbers
 Enter the the number of fibonacci numbers required""")
count = int(input(">"))

# initialize the first two  number of fibonacci series as zero and one
first_number = 0
second_number = 1

# create an empty  list to store the fibonacci series
fibonacci_list = list()

# add the first two number to the list
fibonacci_list.append(first_number)
fibonacci_list.append(second_number)

# calculate the fibonacci series
for turn in range(count - 2):
    number = first_number + second_number
    fibonacci_list.append(number)
    first_number = second_number
    second_number = number

# print the calculate fibonacci series

if count <= 0:
    print("Enter a number greater than zero")
elif count == 1:
    print(fibonacci_list[0])
else:
    print(*fibonacci_list)
print("Thank you for using my program!!")
