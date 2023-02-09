#program to find and display the minimum and the maximum among 10 numbers separated by white spaces
input_numbers_list=list(map(float,input().split()))#[:10]    #To get the input numbers seperated by white spaces as floats
if len(input_numbers)==10:  #Only to get proceed with if only 10 numbers have input
    maximum_float = max(input_numbers_list)  #To select the maximum floating number in input_numbers list
    minimum_float = min(input_numbers_list)  #To select the minimum floating number in input_numbers list
    import math     
    tuple_containing_seperated_integer_and_floating_part_of_maximum_float=math.modf(maximum_float)  #To seperate floating and integer parts of maximum_float selected 
    if tuple_containing_seperated_integer_and_floating_part_of_maximum_float[0] == 0:   #To identify whether the maximum_float can be written as an integer
        print("Maximum = ",int(maximum_float))  #if can, print it as an integer
    else:
        print("Maximum = ",maximum_float)   #if cannot, print it as a float
    tuple_containing_seperated_integer_and_floating_part_of_minimum_float=math.modf(minimum_float)  #To seperate floating and integer parts of minimum_float selected
    if tuple_containing_seperated_integer_and_floating_part_of_minimum_float[0] == 0:   #To identify whether the maximum_float can be written as an integer
        print("Minimum = ",int(minimum_float))  #if can, print it as an integer
    else:
        print("Minimum = ",minimum_float)   #if cannot, print it as a float


