startNumber = int(input("What is your start number   : "))
endNumber   = int(input("What is your end number     : "))
stepNumber  = int(input("What is your step number    : "))

while True:
    if  (endNumber > startNumber):
        while  True:
            if (startNumber <= endNumber):
                print(startNumber)
                startNumber += stepNumber
    else :
        print(startNumber)
        break

