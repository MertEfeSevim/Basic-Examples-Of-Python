def calculateArea(radius):
    PI = 3.142
    area = PI*radius**2
    print("The area of your circle is", str(area))

radius = int(input("Enter radius : "))
calculateArea(radius)