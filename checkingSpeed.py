import datetime

def writeToFile(plateNumber, enteringVal, exitingVal, ends,start, speed):

    #This method writes required details to the file such as;
    # Plate Number,Entering and Exiting Time, Time Difference and Speed

    file = open("offenders.txt", "a")   #Opens file
    file.write("Plate Number :")
    file.write(plateNumber)
    file.write(" Entering Time :")      #Writes details
    file.write(enteringVal)
    file.write(" Exiting Time :")
    file.write(exitingVal)
    file.write(" Time Difference : ")
    file.write(str(ends-start))
    file.write(" Calculated Speed :")
    file.write(str(speed))
    file.write("\n")
    file.flush()                        #Flushes and closes file
    file.close()

def calculateSpeed(plateNumber):

    #This function asks inputs from user and calculates either speed is larger than limit or not.

    enteringVal = input("Enter starting time of check as hour, minute, second seperated with ':' ")
    exitingVal = input("Enter ending time of check as hour, minute, second seperated with ':' ")

    start = datetime.datetime.strptime(enteringVal, '%H:%M:%S')     #Entered values are getting seperated to
    ends = datetime.datetime.strptime(exitingVal, '%H:%M:%S')       #hours, minutes and seconds for later calculations.

    timeDifference = (ends - start).total_seconds()                 #Time difference calculating as seconds
    speed = (100 / timeDifference) * 3.6                            #and speed calculating via formula

    if speed > 120:                                                 #If speed is out of the limit, values are send to the other function
        writeToFile(plateNumber, enteringVal, exitingVal, ends,start, speed)
    else:
        print("Thank you for driving safe !")


plateNumber = input("Please enter your car's plate number :")       #Asking for plate number and sending the value to function
calculateSpeed(plateNumber)
