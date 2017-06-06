num = int(input("enter number"))

fac = 1

if num <0:
    print("Cannot calculate.")
elif num ==0:
    print("1")
else:
    for i in range(1,num+1):
        fac=fac*i
    print(fac)