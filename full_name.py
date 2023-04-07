#In this file the code written below takes a user input "full name of User" and the if,elif and else 
# control structure were used to ensure the user enters the right input.

#Variable full_name is used to store the value entered by the user.
full_name = input("Enter Your Full Names: ")

#The len() is used to the know the length of the string entered by the user.
if len(full_name) == 0:
#The message in the print() will be printed if there is no input from the user.
    print("You haven't entered anything. Please enter your full name.")
elif len(full_name) < 4:
#The message in the print() will be printed if the user enter a string that is less than 4.
    print("You have entered less than 4 characters. Please make sure that you have entered your name and surname.")
elif len(full_name) > 25:
#The message in the print() will be printed if the user enter a string that is more than 25 characters.
    print("You have entered more than 25 characters. Please make sure that you have only entered your full name.")
else:
#The message in the print() will be printed if all the conditions above were not met.
    print("Thank you for entering your name.")