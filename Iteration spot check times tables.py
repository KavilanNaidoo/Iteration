#Kavilan Naidoo
#11-11-2014
#Iteration spot check times tables

number= int(input("Please enter an integer: "))
print("Times tables for {0}".format(number))
count = 0
while count <12:
    count = count + 1
    total = count * number
    print("{0:2} * {1:1} = {2:3}".format(count,number,total))
    
