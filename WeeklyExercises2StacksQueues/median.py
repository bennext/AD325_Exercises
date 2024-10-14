

# Write a function named median that accepts a list of integers as its argument and returns the median of the numbers in the list. 
# The median is the number that will appear in the middle if you arrange the elements in order. 
# Assume that the list is of odd size (so that one sole element constitutes the median) 
# and that the numbers in the list are between 0 and 99 inclusive.

# For example, the median of [5, 2, 4, 17, 55, 4, 3, 26, 18, 2, 17] is 5, 
# and the median of [42, 37, 1, 97, 1, 2, 7, 42, 3, 25, 89, 15, 10, 29, 27] is 25. 

def median(listOfNums):

    listOfNums.sort()
    return listOfNums[len(listOfNums)//2]

    # print(listOfNums[len(listOfNums)//2])

    # print(listOfNums)


### testing

median([7, 9, 1,2,3])