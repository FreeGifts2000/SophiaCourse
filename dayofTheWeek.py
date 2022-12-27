class dayofTheWeek:
    #Create a class variable to store the total number of days in each month.
    eachMonth = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    #Calculate if it is a leap year.
    def queryYear(self, x):
        condition1 = x % 400 == 0
        condition2 = x % 100 != 0 and x % 4 == 0
        leapYear = condition1 or condition2
        if leapYear == True: self.eachMonth[1] = 29
        else: self.eachMonth[1] = 28

    #Whether the calculation date is legal.
    def queryMonthandDay(self, x, y):
        #Check if the date is legal with multiple conditions.
        if x < 1 or x > 12 or y < 1: return False
        elif y > self.eachMonth[x-1]: return False
        elif y <= 0: return False
        else: return True
        
    #Calculate the day of the week for the date entered by the user
    def dayofWeek(self, x, y, firstDay):
        #Initialize variables
        totalDays = 0
        i = 0
        #Iterate through each month and count the number of days.
        #The x variable represents the month entered by the user, 
        #and it is subtracted by 1 because only the completed months are counted.
        while (i < x - 1):
            totalDays += self.eachMonth[i]
            i += 1
        #Add the number of days that have passed in the month.
        totalDays += y

        #Use the remainder of the total number of days to find the day of the week.
        dayofWeek = totalDays % 7
        #Minus Jan. 1.
        dayofWeek += (firstDay - 1)
        #If the result is not legal, 
        #subtract/add the number of days in a week to make it legal.
        if dayofWeek > 6: dayofWeek -= 7
        elif dayofWeek < 0: dayofWeek += 7
        return dayofWeek
    
    #Use the constructor as the main function.
    def __init__(self):
        while True:
            #User input
            year = int(input("Please input a year, Enter 0000 to exit the program. "))
            #If user enter 0000, break this loop and whole program will end. 
            if year == 0000: break
            firstDay = int(input("Please input the week of the first day of this year, use the number 0 to represent Sunday."))
            #Check if leapyear
            self.queryYear(year)
            month = int(input("Please input a month. "))
            day = int(input("Please input a day. "))
            #Check the date, prompt the user if it is not legal 
            #and skip the rest of the code and go back to the beginning of this loop.
            if self.queryMonthandDay(month, day) == False: 
                print("Your input is incorrect, please try again.\n")
                continue
            #Calculate the day of the week.
            dayofWeek = self.dayofWeek(month, day, firstDay)
            
            #Output the results.
            match dayofWeek:
                case 0: print("This day is Sunday.")
                case 1: print("This day is Monday.")
                case 2: print("This day is Tuesday.")
                case 3: print("This day is Wednesday.")
                case 4: print("This day is Thursday.")
                case 5: print("This day is Friday.")
                case 6: print("This day is Saturday.")

dayofTheWeek()

