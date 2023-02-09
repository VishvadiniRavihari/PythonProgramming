#program to evaluate whether a given number prime or non prime until 0 or negative to be taken as input
termination_point=1            #to define a termination trigger
while termination_point>0:         #to repeat the process for many number of times
    number=int(input("Enter your number: ")) #to get the input
    if number>0:        # putting a condition to avoid negative inputs for processing
        if number == 1: #to initially seperate input 1 as a non prime 
            print("non prime")
        else:
            for divisor in range(2,number):#to obtain possible divisors of number except 1 and number itself
                if number % divisor == 0: 
                    print("non prime")
                    break      #to break the loop since many more divisors with zero end remainder available means non prime
            else:
                print("prime") #to indicate as prime since no more divisors with zero end remiander

        termination_point+=1 
    else:
        termination_point=-1 #to terminate the program immediately if the input is negative
        
        
    
        
            
        
