#program to input a matrix with any dimension and output the transpose of that matrix
matrix_as_a_list=[] #define an empty list to store row eleemnts in sublists per each
loop_point_1=1      #to define values for infinity loops
loop_point_2=1
termination_point=1 # to define a termination point tomake the program only flow when necessary conditions have satisfied
while loop_point_1>0:# to define an outer loop, since value error exception in a loop is to be handled  
    try:
        while loop_point_2>0: #to have input values of matrixes in any dimension
            input_elements_in_matrix_list=list(map(int,input().split()))    #to get the input numbers of a row in matrix
            if -1 in input_elements_in_matrix_list :    #to terminate from getting inputs when -1 is entered
                break
            else:
                matrix_as_a_list.append(input_elements_in_matrix_list)
    except ValueError:  #to handle exception error and terminate the program properly by indicating the error
        print("Error")  #to output Error in inputs entered
        matrix_as_a_list=[] #to clear the matrix_as_a_list list
        break
    for a_row_of_the_matrix in range(len(matrix_as_a_list)-1):  #to check the each subsequent row in matrix does conatain same number of number values
        if len(matrix_as_a_list[a_row_of_the_matrix])==len(matrix_as_a_list[a_row_of_the_matrix+1]):    
            continue    #continuously check te each subsequent row , if two checked are with same number of elements
        else:
            termination_point=0   #to set termination point , inorder to make invalid inputs not to go thorugh process of transposing 
            print("Invalid matrix") #to indicate that number of elements in rows are not equal
            break
    if termination_point == 1:  #only to get valid inputs for transposing process
        number_of_rows = len(matrix_as_a_list)  #number of rows =number of sublists in the matrix whixh is there as a list
        number_of_elements_in_a_row = len(matrix_as_a_list[0])  #number of elements in a row =number of eleements in a sublist
        for element_index in range(number_of_elements_in_a_row):    #to carryout itereation to do the transposing process #the value with same index in each sublist indicates the elements in a column, so these values would be now written as a row in transposing
            for row_index in range(number_of_rows):
                if row_index == number_of_rows-1:   #to have the new line character at the end of each row in matrix which is transposing
                    print(matrix_as_a_list[row_index][element_index])
                else:
                    print(matrix_as_a_list[row_index][element_index],"",end="") #to remove the newline character while having a space between each 2 numbers in a row in transposed matrix
        matrix_as_a_list=[] #to clear the matrix_as_a_list list
    loop_point_1=-1     #to make the infifnity loop end since transposed matrix is printed
    
        
    
