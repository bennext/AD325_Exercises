def binary_search (sorted_list_of_integers, integer_target_value):
    
    def binary_search (sorted_list_of_integers, integer_target_value, left, right):
        # inner def using bounds
        if integer_target_value < sorted_list_of_integers[left] or integer_target_value > sorted_list_of_integers[right]  :
            return -1
        #checks if number is outside bounds
        
        new_middle = ((right - left) // 2) + left
        if sorted_list_of_integers[new_middle] == integer_target_value:
            return new_middle
        #checks if found it

        if new_middle == left or new_middle == right:
             return -1 
        #if list only has 2 items and neither are it then it is not in the list

            
        if integer_target_value > sorted_list_of_integers[new_middle]:
                high = right
                return binary_search (sorted_list_of_integers, integer_target_value, new_middle, high)
                #keep going bigger

        if integer_target_value < sorted_list_of_integers[new_middle]:
                low = left
                return binary_search (sorted_list_of_integers, integer_target_value, left, new_middle)
                #keep going smaller 

        
    
    middle = len(sorted_list_of_integers) // 2
    if sorted_list_of_integers[middle] == integer_target_value:
        return middle
    #checks if middle happens to be answer

    if sorted_list_of_integers[-1] == integer_target_value:
         return len(sorted_list_of_integers) - 1
    #checks if end happens to be answer

    if integer_target_value > sorted_list_of_integers[middle]:
        high = len(sorted_list_of_integers) - 1
        return binary_search (sorted_list_of_integers, integer_target_value, middle, high)
    #recures but with a new bound using the top half
    
    if  integer_target_value < sorted_list_of_integers[middle] :
        low = 0
        return binary_search (sorted_list_of_integers, integer_target_value, low, middle)
    #recures but with a new bound using the top half

    return -2 #code should never reach here



#testing 

#     0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16
a = [-4,  2,  7, 10, 15, 20, 22, 25, 30, 36, 42, 50, 56, 68, 85, 92, 103]

index = binary_search(a, 42)   # 10
print (index)
index = binary_search(a, 66)   # -1
print(index)

print(binary_search(a, -4)) # 0

print(binary_search(a, 30)) # 8

print (binary_search(a, 92)) # 15

print (binary_search(a, 103)) # 16

