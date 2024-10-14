#  Write a function named count_duplicates that accepts a list of integers as a parameter and that returns the number of 
# duplicate values in the list. 
# A duplicate value is a value that also occurs earlier in the list. 
# For example, if a list named a contains [1, 4, 2, 4, 7, 1, 1, 9, 2, 3, 4, 1], 
# then the call of count_duplicates(a) should return 6 because there are three duplicates of the value 1, 
# one duplicate of the value 2, and two duplicates of the value 4.

# Constraints: The list could be empty or could contain only a single element in such cases, 
# your function should return 0. 
# Do not modify the contents of the list. 

def count_duplicates(listOfInts):

    dupCounter = 0

    temp_list_set = []
    dup_flag = False 

    for q in listOfInts:
        
        for existingNumber in temp_list_set:
            if existingNumber == q:
                dup_flag = True
                dupCounter += 1

        if dup_flag == False:
            temp_list_set.append(q)
        
        dup_flag = False
    return dupCounter

# print (count_duplicates("6t5frfghu7y6tfg66"))

    # dupList = []
    # dupFound = False
    # 

    # for anInt in listOfInts:
    #     for dupInt in dupList:
    #         if anInt == dupInt:
    #             dupFound = True



    # return dupCounter


    # numbers_ive_found_only_once = []
    # numbers_ive_found_dups_of = []

    # my_set = set(listOfInts)