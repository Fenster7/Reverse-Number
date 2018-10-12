
number = int(input("Please type in a positive number without commas.  "))

reverse = 0

while(number > 0):
 reminder = number %10
 reverse = (reverse *10) + reminder
 number = number //10
 
print("\n Reverse of entered number is = %d" %reverse)


    
