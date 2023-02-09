#program to compute product of a matrix and a transpose of another matrix

#A pre-defined function to read the matrix
def reading_matrix():   
    global matrix_as_a_list   #set an empty list to store elements in matrix in row vice and define it in global frame 
    matrix_as_a_list=[] 
    loop_point_1=1  #define loop_points to ensure that program only flows when matrices have entered as per the dimensions given     
    loop_point_2=1
    while loop_point_1>0: #to set a trigger to get many number of input lines
        try:     #to terminate program properly if irrelevant inputs have entered
            while loop_point_2>0: 
                input_elements_in_matrix_list=list(map(int,input().split()))    #to get the numbers for a row of matrix seperated by white spaces
                if dimensions_rows_columns[1]!= len(input_elements_in_matrix_list) :   #to check whether the number of elements in the row enetered is align with column dimension entered  
                    print("Invalid Matrix") #to terminate program properly when number of elements input for the row contradicts with the dimension specified
                    loop_point_2=-1
                    loop_point_1=-1
                    break
                else:   #since input row align with column diemnsion, it is get input to matrix_as_a_list as a seperate sublist for the row
                    matrix_as_a_list.append(input_elements_in_matrix_list)
                    if dimensions_rows_columns[0]==len(matrix_as_a_list):   #to put a condition to exit the loop of getting inputs , if number of rows input to matrix_as_a_list equals to number of rows specified in dimensions
                        break
        except ValueError:  #when value error occurred , program is to be set to exit loops properly
            print("Invalid Matrix")  #to indicate there is an error in entering inputs
            matrix_as_a_list=[]     #to set matrix_as_a_list empty for making the function ready for next use
            break
        return(matrix_as_a_list)    #to return the value of matrix_as_a list at the end of the function

#A pre-defined function for transposing the given matrix
def transposing(matrix_B):      
    global transposed_matrix    #to set an empty list to store rows of transposed matrix and define it in global frame 
    transposed_matrix=[]
    transposed_row=[]   #to set an empty list to store elements in transposed matrix in row vice  
    number_of_rows = len(matrix_B)  #to get the number of rows in the matrix given
    number_of_elements_in_a_row = len(matrix_B[0])  #to get the number of elements in a row of the matrix given
    for element_index in range(number_of_elements_in_a_row):    #to set a loop to get the elements with same index in sublists to ensure that a column of the given matrix have made into a seperate sublists
        for row_index in range(number_of_rows):
            transposed_row.append(matrix_B[row_index][element_index])#to eneter elements of the same column into transposed_row list to ensure that a column has made into to a seperate list
            if len(transposed_row)==dimensions_rows_columns[1]: #to enter the transposed column as a seperate row in tranposed_matrix once the number of elements in transposed_row matrix complies with the number of elemets which should be there in a row of transposed matrix 
                transposed_matrix.append(transposed_row)
                transposed_row=[]   #to set the transposed_row list as empty for making it ready to get the values for the next row in transposed_matrix
    return(transposed_matrix)   #to return the value of transposed_matrix


#A pre-defined function to calculate the product of given two matrices
def product_of_matrix(matrix_A,transposed_matrix):
    sum_of_row_column_multiples=0  #to define a variable to get the sum of multiples of corresponding elements in a row and column
    element_list=[] #to define an empty set to store the elements of a row in product_matrix
    row_list=[] #to define a list to contain the rows of product_matrix in seperate sublists
    for ele_4 in range(dimensions_rows_columns[0]): #to set a loop to get the corresponding elements form row of a matrix and column of another matrix for multiplying
        for ele_5 in range(dimensions_rows_columns[0]):
            for ele_6 in range(dimensions_rows_columns[1]): #to set a loop to carry out multiplying process and to add the the values of multiples  
                element_from_row=matrix_A[ele_4] #to get the relevant row element for multiplying
                element_from_column=matrix_B[ele_5] #to get the relevant column element for multiplying
                an_element_multiple=element_from_row[ele_6]*element_from_column[ele_6] #to calculate multiples
                sum_of_row_column_multiples+=an_element_multiple #to add the multiples for a certain element in product_matrix
            element_list.append(sum_of_row_column_multiples) #to add a value of element in product_matrix
            sum_of_row_column_multiples=0 #to set the variable to get the sum of multiples zero for the next iteration to get the next element
        row_list.append(element_list) #to seperately store rows of product_matrix for easy iteration in printing
        element_list=[] #to set elemnt_list zero to store elements of next row in product_matrix
    for count_to_print_1 in range(dimensions_rows_columns[0]):  #to carry out iteration process for printing the row_list in standard matrix form
        for count_to_print_2 in range(dimensions_rows_columns[0]):
            if count_to_print_2 == (dimensions_rows_columns[0]-1):  #to ensure the newline character at the end of each row for the next row to be in next line
                print(row_list[count_to_print_1][count_to_print_2])
            else:
                print(row_list[count_to_print_1][count_to_print_2],"",end="") #to ensure there is a white space between subsequent elements in the same row while eliminating the new line character 
    return()
        
  
#The main program
dimensions_rows_columns=list(map(int,input("Enter the dimensions: ").split(','))) #to get the inputs for dimension of matrices to be entered
print("Enter Matrix A: ") #to print and indicate to enter the values for matrix_A
reading_matrix()    #to call the function for reading the matrix entered 
matrix_A=matrix_as_a_list  #to assign the output from reading matrix function as matrix_A variable
matrix_as_a_list=[] #to set the matrix_as_a_list empty for another use of the function since the list is globally defined 

if (len(matrix_A)==dimensions_rows_columns[0]):  #to make sure program flows when only matrix_A have been enetered in correct dimensions as per given
    print("Enter Matrix B: ")  #to print and indicate to enter the values for matrix_B
    reading_matrix()   #to call the function for reading the matrix entered
    matrix_B=matrix_as_a_list  #to assign the output from reading matrix function as matrix_B variable
    matrix_as_a_list=[]   #to set the matrix_as_a_list empty for another use of the function since the list is globally defined
    transposing(matrix_B)    #to call the transposing function to transpose matrix_B
    product_of_matrix(matrix_A,transposed_matrix)   #to call the product_of_matrix function to process the product matrix of matrix_A and transposed matrix and output the result
