# Program contains a file that checks if the number entered is an odd number.
# If yes the program prints the pattern with the stars from 1-5.
# Since a range of 5 was used, (5 + i) will not be executed.
# Any odd number greater than 5 will also not produce the pattern.

# Program contains a file that checks if the number entered is an odd number.
# If yes the program prints the pattern with the stars from 1-5.
# Since a range of 5 was used (5 + i) will not be executed in the loop.
# Any odd number greater than the range of 5 will also not produce the pattern.
while True:
    try:
        number = int(input("Enter a odd number between 1 and 5: "))
        if number % 2 != 0 and number <= 5:
            stars = "*****"
            for i in range(5):
                index = i + 1
                print(stars[0:index])
            break

        elif number > 5:
            print("\nYou entered a number greater than 5")

        else:
            print("\nYou entered an even number between 1 and 5")
        continue

    except ValueError:
        print("\nPlease enter an integer/number!!!")