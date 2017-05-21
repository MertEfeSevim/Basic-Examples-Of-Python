listN = str(input("Please Enter a word"))

def listMethod(listN):
    listN.split(" ")
    if (listN == listN[::-1]):
        return True
    else:
        return  False


print("Your word", listN,"\nAfter my operation gives us:",listMethod(listN))