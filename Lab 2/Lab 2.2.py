#Develop a program to read the names of two sports and generate the sentences by iterating
subject_elements_list=["I","We"]    #To define subject elements
verb_elements_list=["play","watch"] #To define verb elements
object_sports_list=list(map(str,input().split()))#[:2]   #to input sports as a list
if len(object_sports_list) == 2:     #To get procced further, only if 2 sports are there in the input_sports_list
    for subject_element in subject_elements_list: #To iterate subject, verb, object sports elements to generate senetences.
        for sport_element in object_sports_list:
            for verb_element in verb_elements_list:
                print(subject_element,"",verb_element,"",sport_element+".")     #To print the sentences 
