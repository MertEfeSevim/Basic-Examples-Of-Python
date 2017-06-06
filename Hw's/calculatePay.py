"""
Firstly, ask for the hours, then ask for the rate. Both of these need to be gotten from the user
Next, calculate the pay for that user and print it out.
This program calculates the pay with two inputs,
which are hours and rate.
Multiplication of these inputs, gives the pay,
which is result.
"""

hours = float(input("Enter Hours : ")) #Askıng ınputs
rate = float(input("Enter rate: "))

print("You have worked for " , hours , "hours", '\n',
      "and your rate is " , rate)

pay = hours * rate;                    #Multiplication of inputs
print("Pay : ",pay)                    #Printing the result
