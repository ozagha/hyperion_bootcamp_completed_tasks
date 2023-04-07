# This file contains a program that sums up all user inputs"
# The user can exit the while loop by entering -1.
# The average of all user inputs is calculated excluding -1.
# I used the URL https://docs.python.org/2/tutorial/errors.html to learn
# Error handling using try and except helped in catching the ValueError.

sum_input = 0
count = 0
while True:
    try:
        user_input = int(input("Enter a number, -1 will exit the loop: "))
        count = count + 1
        sum_input += user_input
        if user_input == -1:
            break

    except ValueError:
        print('You did not enter a number')

total_input = sum_input + 1
total_count = count - 1
average = total_input/total_count
print(f"\nThe average = {average}")