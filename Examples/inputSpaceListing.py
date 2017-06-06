listN = str(input("Please Enter a list of things"))

def listMethod(listN):
    return listN.split(" ")


print("Your list", listN,"\nAfter my operation gives us:",listMethod(listN))