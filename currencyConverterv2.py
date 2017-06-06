
def fromTlConverter(amountOfMoney, convertTo):

    """
    This method is created to convert from TL to other currencies.
    It multiplies amount of TL with desired currency's value.
    """

    if   convertTo == 'EUR':
        return amountOfMoney*0.29859
    elif convertTo == 'USD':
        return amountOfMoney*0.32468
    elif convertTo == 'GBP':
        return amountOfMoney*0.26592
    elif convertTo == 'RUB':
        return amountOfMoney*20.3115
    elif convertTo == 'AUD':
        return amountOfMoney*0.42604
    elif convertTo == 'AED':
        return amountOfMoney*1.19261
    elif convertTo == 'CNY':
        return amountOfMoney*2.19826
    elif convertTo == 'AZN':
        return amountOfMoney*0.52597
    else :
        return amountOfMoney*1.21797

def toTlConverter(amountOfMoney, chosenCurrency):

    """
    This method is created to convert to TL from other currencies.
    It multiplies amount of other currencies with their specified value.
    """

    if chosenCurrency == 'EUR' :
        return amountOfMoney*3.34903
    elif chosenCurrency == 'USD':
        return amountOfMoney*3.07993
    elif chosenCurrency == 'GBP':
        return amountOfMoney*3.76052
    elif chosenCurrency == 'RUB':
        return amountOfMoney*0.04923
    elif chosenCurrency == 'AUD':
        return amountOfMoney*2.34720
    elif chosenCurrency == 'AED':
        return amountOfMoney*0.83850
    elif chosenCurrency == 'CNY':
        return amountOfMoney*0.45490
    elif chosenCurrency == 'AZN':
        return amountOfMoney*1.90126
    else :
        return amountOfMoney*0.82104

def confirmTransaction(userName , amountOfMoney , chosenCurrency , convertTo):

    """"
    This method explains what user have entered to the program from beginning.
    Also method asks for a confirmation.
    """

    print(userName , "you want to convert" , amountOfMoney, chosenCurrency, "amount of money", "to" , convertTo,".\n Are you confirm the transaction ? ")

userName = str(input("What is your name ? "))

print("Welcome to the program" ,userName ,"\nThis program is a currency converter."
                                          "\nThis program is able to convert TL to"
                                          "\nEUR, USD, GBP, RUB, AUD, AED, CNY, AZN, SAR currencies "
                                          "\nand able to convert to the TL from other currencies. ")
#After asking user's name, program explains itself to user.

failSafe = True
while failSafe:

    """
    While failSafe is True, it means that there is a problem about input/s.
    In this failsafe inner loop checks if user enter one of the currency that program is able to handle.
    If input is acceptable, then outer loop confirms.
    If not, it reminds to user options and asks again.
    """

    print("\nYou can choose TL, EUR, USD, GBP, RUB, AUD, AED, CNY, AZN, SAR currencies.")

    failSafe3 = True
    while failSafe3:

        chosenCurrency = str(input("Which currency you want to chose? "))

        if         chosenCurrency == 'EUR' \
                or chosenCurrency == 'USD'\
                or chosenCurrency == 'GBP'\
                or chosenCurrency == 'RUB'\
                or chosenCurrency == 'AUD'\
                or chosenCurrency == 'AED'\
                or chosenCurrency == 'CNY'\
                or chosenCurrency == 'AZN'\
                or chosenCurrency == 'SAR'\
                or chosenCurrency == 'TL':
            failSafe3 = False
            #If input is acceptable, it breaks the loop by substract one.

        else:
            print("You have entered wrong. \nYou can choose TL, EUR, USD, GBP, RUB, AUD, AED, CNY, AZN, SAR currencies.")

    confirmedCurrency = str(input("Could you confirm your currency. "))

    if chosenCurrency == confirmedCurrency :
        failSafe = False
    else :
        print("You have entered wrong.")

failSafe4 = True
while failSafe4:
    #This failsafe checks if the input is float or not.

    amountOfMoney = float(input("What amount of money you want to convert ? "))

    if isinstance(amountOfMoney,float) :
        failSafe4 = False
    else :
        print("You have entered wrong. You should enter integer or float.")

failSafe1 = True
while failSafe1:

    #In this failsafe loop checks if user enter one of the currency that program is able to convert to.
    #If not loop asks again.

    convertTo = str(input("Which currency you want to convert ?"))

    if         convertTo == 'TL' \
            or convertTo == 'EUR'\
            or convertTo == 'USD'\
            or convertTo == 'GBP'\
            or convertTo == 'RUB'\
            or convertTo == 'AUD'\
            or convertTo == 'AED'\
            or convertTo == 'CNY'\
            or convertTo == 'AZN'\
            or convertTo == 'SAR':
        confirmTransaction(userName , amountOfMoney , chosenCurrency , convertTo)
        failSafe1 = False
    else :
        print("You have entered wrong.")

failSafe2 = True
while failSafe2:

    """
    In this failsafe outer loop checks either user confirm or cancel the transaction.
    If user cancels, then loop breaks and program finishes after print message.
    Inner loop determines which method is going to be used.
    """

    confirmationOfUser = str(input("You can either cancel transaction or confirm by entering Yes or No."))

    if         confirmationOfUser == 'YES'\
            or confirmationOfUser == 'yes'\
            or confirmationOfUser == 'Yes'\
            or confirmationOfUser == 'y'  \
            or confirmationOfUser == 'Y':
        failSafe2 = False

        if chosenCurrency == 'TL' and convertTo != 'TL' :
            print(userName, amountOfMoney, chosenCurrency, " is converted to ", fromTlConverter(amountOfMoney, convertTo), convertTo)
        else :
            print(userName, amountOfMoney, chosenCurrency, "is converted to ", toTlConverter(amountOfMoney, chosenCurrency), convertTo)

    elif       confirmationOfUser == 'NO'\
            or confirmationOfUser == 'No'\
            or confirmationOfUser == 'no'\
            or confirmationOfUser == 'n' \
            or confirmationOfUser == 'N':
        print("Your transaction has been cancelled ", userName ," Thanks for your time, goodbye.")
        break
    else :
        print("You have entered wrong.")
