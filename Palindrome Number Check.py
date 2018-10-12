
original_number = int(input("Please type in a positive number without commas.  "))

number = original_number
reverse = 0

while(number > 0):
 reminder = number %10
 reverse = (reverse *10) + reminder
 number = number //10
 
print("\n Reverse of entered number is = %d" %reverse)

if reverse == original_number:
    print(original_number, "is a palindrome.")
else:
    print(original_number, "is not a palindrome.")
    
