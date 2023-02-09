#Program to write number of abundant numbers exists within the given range
list_of_proper_divisors=[]  #to define an empty list for proper divisors
list_of_abundant_numbers=[] #to define an empty list for abundant numbers
sum_of_proper_divisors=0    #to define an object to get sum of proper divisors 
input_number_for_counting=int(input("Input Number: "))
if input_number_for_counting<=2:     #to avoid negative inputs for processing
    print("Invalid input")
else:
    for number in range(2,input_number_for_counting+1):  #to get the range of numbers to be considered
        for divisor in range(1,number):     #to get the range of divisors applicable
            if number%divisor == 0:         #to identify proper divisors and get them to the list_of_proper_divisors
                list_of_proper_divisors.append(divisor)
            else:
                continue
        #print(list_of_proper_divisors)
        sum_of_proper_divisors=sum(list_of_proper_divisors)     #to get the total of proper divisors
        if sum_of_proper_divisors > number:     #to identify abundant numbers and assign them to the list_of_abundant_numbers
            list_of_abundant_numbers.append(number)
        list_of_proper_divisors=[]      #to set the list of proper divisors zero for next "number" elemnt in range to be processed
print(list_of_abundant_numbers)
print("Number of abundant numbers from 1 to",input_number_for_counting,"is",len(list_of_abundant_numbers))
                       
