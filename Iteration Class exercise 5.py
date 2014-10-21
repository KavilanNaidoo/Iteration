#Kavilan Naidoo
#21-10-2014
#Iteration Class exercise 5


result = 0
number = 0
count = 0
while number >= 0:
    number = int(input("Please enter a series of numbers: "))
    if number >=0:
        result = result + number
        count = count + 1
average = result / count
print("Your average for your series of numbers is: {0}".format(average))
