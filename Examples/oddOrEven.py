def oddOrEven(number):
    result=""
    if number %2 == 0:
        result = "even"
    else :
        result = "odd"
    return result

number = float(input("enter number"))
print("The number ",number, oddOrEven(number), "number")