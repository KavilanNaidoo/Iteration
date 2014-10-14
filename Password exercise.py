#Kavilan Naidoo
#10-10-2014
#Password exercise

length=int(input("Please enter the number of characters you want as a password: "))
if length >0:
    import random
    import string
    list1 = ""
    while length >0:
        choice = random.choice(string.ascii_letters + string.digits)
        list1= list1 + choice
        length = length - 1

    print(list1)
                        
    

    
