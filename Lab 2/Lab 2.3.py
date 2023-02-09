#program to read the marks and calculate and display the total marks and average mark of each student
marks_list=[]   # to define en empty list to store marks of each students seperately
termination_point=0#to define termination point to make program only flow only if it meets with necessary conditions
for counting_1 in range(3): #to get inputs 4 times for the 4 students
    marks_per_student_list=list(map(int,input().split()))   #to get the input marks seperated by white spaces
    marks_list.append(marks_per_student_list)   #to assign input marks of each students to marks_list seperately
for counting_2 in range(3): #to make sure that no more than marks of 3 subjects have input
    if len(marks_list[counting_2])<=3:  #to check the number of mark elements entered for each student
        continue
    else:   #inorder to terminate the program since at least for one student more than 3 marks have entered
        termination_point=1
        break
if termination_point!=1:    #to make sure that to proceed with marks inputs only for 3 subjects for each student
    for counting_3 in range(3): #to make sure input marks are between 0 and 100
        for counting_4 in range(3):
            if (marks_list[counting_3][counting_4]>=0) and (marks_list[counting_3][counting_4]<=100):
                continue
            else:   #since marks out of range (0 to 100) have been enetered, the program is made to be terminated 
                termination_point=1
                break
if termination_point!=1:    #to make sure that to proceed with marks which are correctly inbetween the range          
    for counting_5 in range(4): #to calculate total and average for each studenet seperately in 4 times
        total_marks_of_a_student = sum(marks_list[counting_5])  #to calculate the sum for each student
        average_mark_of_a_student = total_marks_of_a_student/4 #to calculate the average mark of each student
        print("Total: ",total_marks_of_a_student,"","Average: ","%.1f"%average_mark_of_a_student)  #to print the total and average of each student  
    


