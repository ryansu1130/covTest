#To run the program in the terminal: python3 Ryan_Su_HW1.py
#Enter a year to check whether if it is a leap year or not
#Finished time: Apr 21 2021 @ 9:11:23PM

def isLeapYear(year):
     if year%4 == 0:
         if year%100 == 0:
             if year%400 ==0:
                 return True
                 #print(f"{year} is a leap year")
             else:
                 return False
                 #print(f"{year} is not a leap year")
         else:
             return True
             #print(f"{year} is a leap year")
     else:
         return False
         #print(f"{year} is not a leap year")

     return False
