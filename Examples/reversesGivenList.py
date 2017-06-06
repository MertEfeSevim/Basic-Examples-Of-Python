listN = str(input("Please Enter a list of things"))

def listMethod(listN):
    listN2 = listN.split(" ")
    listN2=listN2[::-1]
    listN3=' '.join(listN2)
    return listN3


print("Your list", listN, "\nAfter my operation gives us:",listMethod(listN))