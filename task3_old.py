# This file contains a program that determines the award a person competing in a triathlon will receive.
print("TRIATHLON COMPETITION")
#variable_swimming is used to store the swimming time
#variable_cycling is used to store the cycling time
#variable_running is used to store the running time

variable_swimming = int(input("Enter Swimming time in Minutes: "))
variable_cycling = int(input("Enter Cycling time in Minutes: "))
variable_running = int(input("Enter Running time in Minutes: "))

#Qualifying time which is 100 minutes is stored in the variable below.
qualifying_time = 100

#The total time is gotten by suming the values inputed (from Swimming, Cycling and Running)
total_time = variable_swimming + variable_cycling + variable_running

#The print below display the total time it took to complete the triathlon.
print("\nTotal time taken to complete the triathlon is " + str(total_time) + " Minutes")

print("\nPARTICIPANT WILL RECEIVE:")
#Using if,elif and else statement with logical operators. 
#The total time is compared with the qualifying time to determine the awards that each participant will receive.

if total_time < 100:
    print("Provincial Colours")
elif total_time > 100 and total_time <= 105:
    print("Provincial Half Colours")
elif total_time > 105 and total_time <= 110:
    print("Provincial Scroll")
else:
    print("No award")