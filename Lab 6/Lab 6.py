#An empty stack is defined for storing the values entered to tree nodes
stack_of_tree_node_values =[]
#An empty is defined for storing the main operators within the expression except the one in sub expression(if available)
stack_of_main_operators=[]
#An empty stack is defined for storing the all operands plus the operator of sub expression if available
stack_of_rest_of_values = []

#An empty object is defined as an identifier of the position of start of the right branch values in stack_of_tree_node_values
position_of_start_of_the_right_branch= 0
#An empty object is defined as an identifier of the position of the left number of sub expression( bracketed part)in stack_of_rest_of_values
position_of_the_left_value_of_sub_evaluation = 0
#An empty object is defined as an identifier of the position of the right number of sub expression( bracketed part)in stack_of_rest_of_values
position_of_the_right_value_of_sub_evaluation =0


#An empty object is defined to store the left number for evaluating each sub part of the process
left_value = 0
#An empty object is defined to store the right number for evaluating each sub part of the process
right_value = 0
#An empty object is defined to store the operator symbol for evaluating each sub part of the process
operation_symbol = None

#An empty object is defined to store the accumulated value of evaluating process which is to be done in a recursive manner
accumulated_value = 0



class Node:
    def __init__(self,key):
        self.right = None
        self.left = None
        self.val = key


    def get_output(self):
        value = self.evaluate()
        if value > 999:
            print('OVERFLOW')
        elif value < 0:
            print('UNDERFLOW')
        else:
            print(value)


    #A predefined function inside the Node to store input values in a binary tree in an accessible and meaningful manner 
    def insert(self,data,bracketed):

        '''The all operands and that operator (if available) which is deemed to be carry out an sub operation within
        the brackets are supposed to stored in the righthand side branches of the tree.'''
        '''The rest of the main operators which are not supposed to evaluate any sub expression, is to be stored in the
        lefthand side of the tree'''

        #to define the selection conditions to seperate the inputs values which are to be stored in the suitable side of the tree as per the standard defined
        if (bracketed is False and data[0] == "OPERAND") or (bracketed is True and data[0]== "OPERATOR"):
            #storing suitable values in the right hand side will be done in a recursive manner
            if self.right == None:
                self.right= Node(data)
            else:
                self.right.insert(data,bracketed)
        else:
            #storing suitable values in the left hand side will also be done in a recursive manner
            if self.left == None:
                self.left = Node(data)
            else:
                self.left.insert(data,bracketed)
        return self



    #A predefined function inside the Node to evaluate the values of the expression enetered which is already stored in the tree
    def evaluate(self):
        #A predefined function will be called to read the values stored in branches (to traverse the tree)
        traverse_preorder(self)

        '''After traversing the tree, the focus is to seperately store the main_operators and operands together with that operator for sub expression's
        evaluation in seperate 2 stacks. The aim of storing sub expression's operator together with operands is to do that required sub evaluation
        within the stack ,it is stored'''

        #Making the globally defined variables are ok to change as per the changes done within the function's local frame
        global stack_of_tree_node_values
        global stack_of_main_operators
        global stack_of_rest_of_values

        '''first operand will be seperately moved to the stack_of_rest_of_values'''
        #the first operand will be seperately assigned to a variable
        first_operand = stack_of_tree_node_values[0]
        
        #seperated first operand will be added to the stack_of_rest_of_values
        stack_of_rest_of_values.append(first_operand[1])
        #first operand will be deleted from the stack_of_tree_node_values
        del stack_of_tree_node_values[0]
        
        '''the next half of the values remain in the stack is main operators and they are to be stored in stack_of_main_operators in an iterative manner'''
        for count_1 in range(len(stack_of_tree_node_values)):
            #conditions are placed to iterate the stack_of_tree_node_values untill the last value in bulk with "OPERATOR" to be stored in stack_of_main_operators.
            if stack_of_tree_node_values[count_1][0] == 'OPERATOR':
                stack_of_main_operators.append(stack_of_tree_node_values[count_1][1])
            #once the first element with "OPERAND" is iterated, it's position within the stack_of_tree_nodes will get noticed and the iteration will be terminated. 
            elif stack_of_tree_node_values[count_1][0] == 'OPERAND':
                position_of_start_of_the_right_branch = count_1
                break
        #the moved values to stack_of_main_operators will be deleted from the stack_of_tree_node_values with the reference of position_of_start_of_the_right_branch 
        del stack_of_tree_node_values[:(position_of_start_of_the_right_branch)]

        '''the remaining values would be appened to the stack_of_rest_of_values'''
        for count_2 in range(len(stack_of_tree_node_values)):
            stack_of_rest_of_values.append(stack_of_tree_node_values[count_2][1])
        
        '''the next focus is to carry out the evaluation of sub expression is availabe '''
        #iteration would be carried out to identify if there any operator presented in stack_of_rest_of_values together with operands
        for count_3 in range(len(stack_of_rest_of_values)):

            #conditions are set to identify any operator present in the stack
            if type(stack_of_rest_of_values[count_3]) is str:

                #some of gloabally defined variables are set to be changed as per the processes done within the function
                global left_value
                global right_value
                global operation_symbol
                global position_of_the_left_value_of_sub_evaluation
                global position_of_the_right_value_of_sub_evaluation

                #the left value of sub expression is identified as the element with one before the index of operator in the stack
                left_value = stack_of_rest_of_values[count_3-1]
                #the right value of sub expression is identified as the element with one after the index of operator in the stack
                right_value = stack_of_rest_of_values[count_3+1]
                
                #operation symbol would be the operator itself which is identified
                operation_symbol = stack_of_rest_of_values[count_3]

                #operation function will be called with the 3 parameter assigned above
                #answer will be assigned to a variable called answer_of_sub_expression
                answer_of_sub_expression = operation(left_value,operation_symbol,right_value)
                #print(answer)
                
                ''' the next focus is to replace the 2 values and the operator of sub expression with the answer of it'''
                #operator in the stack will be changed to the answer_of_subexpression
                stack_of_rest_of_values[count_3] = answer_of_sub_expression
                
                #the position of the left value of sub expression is noticed as the one before index of operator in the stack
                position_of_the_left_value_of_sub_evaluation = count_3 -1
                #the position of the right value of sub expression is identified as the one after index of operator in the stack
                position_of_the_right_value_of_sub_evaluation = count_3+1
            else:
                continue
        #the conditions are set for inputs with no sub expressions are present to by pass the elements changing process in the stack_of_rest_of_values 
        if (position_of_the_right_value_of_sub_evaluation == 0) and (position_of_the_left_value_of_sub_evaluation == 0):
            pass
        else:
            #if sub expressions were present, the left value and the right value of operator's will be deleted from the stack
            del stack_of_rest_of_values[position_of_the_right_value_of_sub_evaluation]
            del stack_of_rest_of_values[position_of_the_left_value_of_sub_evaluation]
        #print(values_stack)
        #print(stack)
        #print(main_operator_stack)
        #print(values_stack)

        '''the next focus is to evaluate the sole expression present or which is made into'''

        #globally defined accumulated_value variable is set to be change as per the changes to be done within the function
        global accumulated_value

        #accumulated_value will be setted to the value of the first operand 
        accumulated_value = stack_of_rest_of_values[0]
        #first operand will get removed from the stack
        del stack_of_rest_of_values[0]
        #A function will be called to get the answer of evaluated expression to be output
        return finalevaluation(accumulated_value,stack_of_main_operators,stack_of_rest_of_values)
        
#A predefined function to evaluate the value of the expression entered
def finalevaluation(total,stack_of_main_operators,stack_of_rest_of_values):
    #globally defined accumulated_value variable is set to be change as per the changes done within the function
    global accumulated_value

    '''this evaluation process is suppose to be done in a recursive manner where at the first , accumulated_value is to get accumulated through the
    operation function as per the first elements available in stack_of_main_operators and stack_of_rest_of_value . Then the first elements in each stack
    will get read and deleted recursively while processing the accumulated value as the final answer ''' 

    #operation function is called to change the accumulated value as per the first elements present in both stacks
    accumulated_value = operation(total,stack_of_main_operators[0],stack_of_rest_of_values[0])
    #base case is set to return the accumulated_value as the final value when there' s only one element left in the stacks (which is already read)
    if (len(stack_of_main_operators) == 1) and (len(stack_of_rest_of_values) ==1):
        return accumulated_value
    else:
        #recursive case is set to process the accumulated_value by reading and then deleting the first values availabe in stacks 
        del stack_of_main_operators[0]
        del stack_of_rest_of_values[0]
        return finalevaluation(accumulated_value,stack_of_main_operators,stack_of_rest_of_values)

        
        

#A predefined function to do the mathematical operation process
def operation(left_value,operation_symbol,right_value):
    '''since operartors have given in string form, the selection cases have placed to identify the operator as to it's symbol  and perform
    the calculation'''
    if operation_symbol == '+':
        return left_value + right_value
    elif operation_symbol == '-':
        return left_value - right_value
    elif operation_symbol == '*':
        return left_value * right_value
    elif operation_symbol == "/":
        return left_value / right_value
    elif operation_symbol == '^':
        return left_value ** right_value        

#A predefined function to read the tree left branches first and then the right branches  
def traverse_preorder(root):
        #the gloabally setted varibale of stack_of_tree_node_values is made to be change as per the changes done to it within the function
        global stack_of_tree_node_values
        if root:
            #values of nodes read will get appended to the stack
            stack_of_tree_node_values.append(list(root.val))
            #the left side of the tree will be read first in a recursive manner
            traverse_preorder(root.left)
            #the right side of the tree will be read then after in a recursive manner
            traverse_preorder(root.right)
      
            
       



        
#Test 01
root = Node(('OPERAND', 2))
# Form the rest of the tree by inserting data to the root node.
root = root.insert(('OPERATOR', '+'), False)
root = root.insert(('OPERAND', 4), False)
root = root.insert(('OPERATOR', '*'), False)
root = root.insert(('OPERAND', 6), False)
root = root.insert(('OPERATOR', '+'), False)
root = root.insert(('OPERAND', 3), False)
root = root.insert(('OPERATOR', '^'),True)
root = root.insert(('OPERAND', 2), False)
root.get_output()


'''#Test 02
# Use the insert method to add nodes
# Begin with forming the root node for the tree.
root = Node(('OPERAND', 1))
# Form the rest of the tree by inserting data to the root node.
root = root.insert(('OPERATOR', '+'), False)
root = root.insert(('OPERAND', 2), False)
root = root.insert(('OPERATOR', '*'), True)
root = root.insert(('OPERAND', 3), False)
root = root.insert(('OPERATOR', '+'), False)
root = root.insert(('OPERAND', 3), False)
root = root.insert(('OPERATOR', '^'), False)
root = root.insert(('OPERAND', 2), False)
# Get the output.
root.get_output()
# Should print 100'''

'''#Test 03
root = Node(('OPERAND', 1))
root = root.insert(('OPERATOR', '+'), False)
root = root.insert(('OPERAND', 2), False)
root = root.insert(('OPERATOR', '*'), False)
root = root.insert(('OPERAND', 3), False)
root = root.insert(('OPERATOR', '+'), False)
root = root.insert(('OPERAND', 3), False)
root = root.insert(('OPERATOR', '^'), False)
root = root.insert(('OPERAND', 2), False)
root.get_output()
# Should print 144'''

'''root = Node(('OPERAND',-15))
root = root.insert(('OPERATOR','-'),False)
root = root.insert(('OPERAND',99),False)
root = root.insert(('OPERATOR','*'),True)
root = root.insert(('OPERAND',10),False)
root.get_output()
# Should print UNDERFLOW'''




            
           

