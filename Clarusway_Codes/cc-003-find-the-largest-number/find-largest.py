def the_biggest(numberslist):
    maximum=0
    for i in numberslist :
        try:
            number=int(i)
        except ValueError:
            continue
        
        if maximum < number :
            maximum=number
    return maximum



given_list=input("Please enter 5 numbers : ").split(" ")


print("The biggest number in your numbers is : {}" .format( the_biggest(given_list)))