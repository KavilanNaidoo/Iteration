#Kavilan Naidoo
#13-10-2014
#Addition iteration

# program to prompt for 8 numbers and report the total to the user
num1 = int(input('Enter number 1 : ' ))
num2 = int(input('Enter number 2 : ' ))
num3 = int(input('Enter number 3 : ' ))
num4 = int(input('Enter number 4 : ' ))
num5 = int(input('Enter number 5 : ' ))
num6 = int(input('Enter number 6 : ' ))
num7 = int(input('Enter number 7 : ' ))
num8 = int(input('Enter number 8 : ' ))
total = num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8
print('The total is {0}'.format(total))


#improvement

total=0

for counter in range(1,9):
    num=int(input("Enter number {0}:".format(counter)))
    total= total + num
print("The total is: {0}".format(total))

    
    
