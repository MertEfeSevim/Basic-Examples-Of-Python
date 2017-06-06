def cryptLetters(letter):
    if letter == "A":
        print(".-")
    if letter == "B":
        print("-...")
    if letter == "C":
        print("-.-.")
    if letter == "D":
        print("-..")
    if letter == "E":
        print(".")
    if letter == "F":
        print("..-.")
    if letter == "G":
        print("--.")
    if letter == "H":
        print("....")
    if letter == "I":
        print("..")
    if letter == "J":
        print(".---")
    if letter == "K":
        print("-.-")
    if letter == "L":
        print(".-..")
    if letter == "M":
        print("--")
    if letter == "N":
        print("-.")
    if letter == "O":
        print("---")
    if letter == "P":
        print(".--.")
    if letter == "Q":
        print("--.-")
    if letter == "R":
        print(".-.")
    if letter == "S":
        print("...")
    if letter == "T":
        print("-")
    if letter == "U":
        print("..-")
    if letter == "V":
        print("...-")
    if letter == "W":
        print(".--")
    if letter == "X":
        print("-..-")
    if letter == "Y":
        print("-.--")
    if letter == "Z":
        print("--..")

code = str(input("Enter"))

for letter in code:
    letter = letter.upper()
    cryptLetters(letter)
