#program to process NIC number as per given credentials
#to define empty lists to include each person's records as seperate sublists and ymd(year, month,day) components seperately for processing
credentials_list=[]
birthday_ymd_components_list=[]
birthday_ymd_components_list_for_calculations=[]
#to open the internal storage file to count how many records are there to get processed
filename=input()
with open(filename) as file:
    record_count = 0
    for character in file:
        if character != "\n":   #put a trigger to seperately indentify each record using newline character
            record_count += 1
#to open the storage file to read data and input for the processing of each digit chunk in NIC
    file = open(filename, "r")
    for count_1 in range(record_count):     #to iterate the process for every person's record
        record_read=file.readline()     #to read data record_vice
        record_split_to_components=record_read.split()  #to split them to components as name,birthday,gender and submission order using the whitespace inbetween each element
        #to seperate each record into a person vice element list
        credentials_list.append(record_split_to_components)
    #Process to output NIC for each person
    submission_list=[]
    for count_2 in range(record_count): #to iterate for every person
        birthday_ymd=credentials_list[count_2][1] #to assign birthday component in credentials_list as a seperate element
        birthday_ymd_components_list=(birthday_ymd.split("-"))  #to seperate ymd components and assign them as seperate elements for easy reference for each element
        #first_4_digits to print
        first_4_digits_to_print=str(birthday_ymd_components_list[0])
        
        for count_3 in range(0,len(birthday_ymd_components_list)):  #to assign the each element in birthday_ymd_components_list convereted to int type to seperate list for easy calculation
            element_for_calculation = int(birthday_ymd_components_list[count_3])
            birthday_ymd_components_list_for_calculations.append(element_for_calculation)
        #subprocess to get second 3 digits, the number of days from January 1st to the birthdate
        month=(birthday_ymd_components_list_for_calculations[1]) #to get the relevant element which indicate the month of birth
        birthdate=birthday_ymd_components_list_for_calculations[2]  #to get the relevant element which indicate the month of birth
        if month ==1:  #to initially address the odd deviation of the pattern for January born   
            odd_months_count= 0
            even_months_count=0
            leap_effect=0
            days_count=birthdate
        else:   #process for rest of people who were not born in January
            #to address the effect of leap year for number of days in February for people who were born Feb and onwards 
            if (birthday_ymd_components_list_for_calculations[0]%4==0):
                leap_effect_for_february=29
            else:
                leap_effect_for_february=28
            #to count the number of odd months and even months till the next month of birthmonth (except february,since seperately addressed) for people who were born between Feb and June
            if (((month) >=2) and ((month)<=6)):
                odd_months_count=((month+1)//2) 
                even_months_count=month - odd_months_count -1
            #to count the number of odd months and even months till the next month of birthmonth (except february,since seperately addressed) for people who were born between July and December
            else:
                odd_months_count=((month+2)//2) 
                even_months_count=month - odd_months_count -1
            #to calculate the number of additional days to deduct from counting using months 
            if month==2:    #for february born people
                days_to_deduct=leap_effect_for_february-birthdate
            elif month<=7:  #for january to june born people excpet February
                if month%2==1:  #for if the birthmonth is odd
                    days_to_deduct=31- birthdate
                else:           #for if the birthmonth is even
                    days_to_deduct=30- birthdate
            else:           #for july to December born people
                if month%2==0:  #for if the birthmonth is even
                    days_to_deduct=31- birthdate
                else:           #for if the birthmonth is odd
                    days_to_deduct=30- birthdate
            days_count=(odd_months_count*31)+(even_months_count*30)+leap_effect_for_february-days_to_deduct
        #to apply the effect to seperate identity gender vice
        if credentials_list[count_2][2]=='F':   #if female, additional 500 would be added
            second_3_digits=500+days_count
        else:
            second_3_digits=(days_count)        #if male, nothing will get addded
        #to set second_3_digits as a textual information with 3 digits for printing
        if len(str(second_3_digits))==1:
            second_3_digits_to_print= ('00'+str(second_3_digits))
        elif len(str(second_3_digits))==2:
            second_3_digits_to_print= ('0'+str(second_3_digits))
        else:
            second_3_digits_to_print=str(second_3_digits)

        #last 3 digits to print as per the order of submission
        submission_list.append(birthday_ymd_components_list_for_calculations[0])
        order=submission_list.count(birthday_ymd_components_list_for_calculations[0])
        order_as_a_string=str(order)
        if len(order_as_a_string)==3:
            order_for_submission=order_as_a_string
        elif len(order_as_a_string)==2:
            order_for_submission=("0"+order_as_a_string)
        elif len(order_as_a_string)==1:
            order_for_submission=("00"+order_as_a_string)
        name_to_print=str(credentials_list[count_2][0])
        nic_to_print=first_4_digits_to_print+second_3_digits_to_print+order_for_submission
        line_to_print=name_to_print+" "+nic_to_print+"\n"
        #print(line_to_print)
        #print(type(line_to_print))
       

        #to print the NIC number with the name of the person
        if len(submission_list)==1:
            attribute= "w"
        else:
            attribute="a"
        f=open("output.txt",attribute)
        f.write(line_to_print)
        f.close()
        #to set birthday_ymd_components_lists as empty for next person's data ieteration
        file.close()
        birthday_ymd_components_list_for_calculations=[]
        birthday_ymd_components_list=[]
            



    
    



