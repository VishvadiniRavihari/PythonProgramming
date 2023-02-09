#program for encryption 
remainder_sequence_list=[]       #to define an empty list to get remainder sequence
message=input("Enter message: ")    #getting the inputs
base=int(input("Enter base: "))
if (base>=1) and (base<=10):    #to apply the condition for base
    character_sequence = list(message) #Get the input message into a list of characters
    for ele_1 in character_sequence:
        ascii_value=(ord(ele_1))   # to read the ascii value of each element_1 in the character_sequence_list 
        while ascii_value>= (base-1):  #conversion process to given base
            quotient = ascii_value // base  #obtaining the quotient 
            remainder = ascii_value % base   # obtaining the remainder 
            remainder_sequence_list.append(remainder)    #adding each remainder to remainder_sequence_list
            ascii_value = quotient   #to continue the process
            if (ascii_value >=0) and (ascii_value<=(base-1)):
                remainder_sequence_list.append(ascii_value)  # to add the end qoutient to the remainder_sequence_list

        #print(list_1)
        remainder_sequence_list.reverse() #to reverse the remainders obtained
        #print(list_1)
        for ele_2 in remainder_sequence_list:    #to print remainder_sequence_list as an unseperated string
            print(ele_2,end="")
        remainder_sequence_list=[]   #set the remainder_sequence_list to zero for next loop of element_1 in character_sequence_list
            


    
                
            
        
            
         
    
    
