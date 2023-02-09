#predefined function to read the input from input file and check it's validity
def getNum():
    with open (input_file) as file:
        file=open(input_file,"r")   #input_file is opened in reading mode 
        number=file.readline()  #to read the input number in file
        if (int(number)>=0 and int(number)<=20):    #to assign only the numbers within the range of 0 to 20 to be suitable for further processing to calculate fibonacci value 
            global valid_integer    #to assign the valid input number in global frame for the use of other predefined functions 
            valid_integer=int(number)
            global termination_point
            termination_point=1
        else:
            print("Invalid input.")
        file.close()
        return

#predefined function to calculate fibonacci value for the given number
def show(valid_integer):
    if valid_integer==0:    #to directly assign value 0 when valid_integer is equal to 0
        return 0
    elif valid_integer==1:  #to directly assign value 1 when valid_integer is equal to 1
        return 1
    else:       #otherwise the formula will be applied in a recursive manner to get the addition of each 2 subsequent additive outcomes
        return(show(valid_integer-1)+show(valid_integer-2))

#predefined function to write the output phrase in a seperate text file
def saveFile():
    output_file=open("result.txt","w")  #to create a file called result.txt to write the output phrase
    output_file.write(output_phrase)    
    output_file.close()
    return

#main program

termination_point=0
#to get the input file containing the number 
input_file=input()
#calling predefined function to read the input from input file and check it's validity 
getNum()
if termination_point==1:
    #calling the predefined function to calculate fibonacci value and assign the output of the function as a seperate object
    fibonacci_value=show(valid_integer)
    #to assign the phrase to be output as a seperate object since it has to be printed on the screen and also written in a text file
    output_phrase=("Fibonacci(" +str(valid_integer)+ ") = " +str(fibonacci_value))
    #printing the output_phrase
    print(output_phrase)
    #calling the predefined function to write the output phrase in a seperate text file called result.txt
    saveFile()







