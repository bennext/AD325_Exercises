#  Write a function named is_stack_sorted accepts a list of integers as a parameter and treats it as a stack, 
# returning True if the elements in the stack occur in ascending (non-decreasing) order from bottom (end) to top (front), else False. 
#  This essentially means that you are checking whether the list is in reverse-sorted order. 
# An empty or one-element stack is considered to be sorted. 
# For example, if passed the following stack, your function should return True:

# [20, 20, 17, 11, 8, 8, 3, 2]

# The following stack is not sorted (the 15 is out of place), so passing it to your function should return a result of False:

# [18, 12, 15, 6, 1]

# You should treat the list as a stack and not use any index-related operations on it. 
# This means that the only operations you should use on the list are the pop and append functions and the len function. 
# You should not use the [] indexing operator nor any other operations that depend on accessing various elements by index. 
# You also should not use a for-each loop over the stack's elements.

# When your function returns, the stack should be in the same state as when it was passed in. 
# In other words, if your function modifies the stack, you must restore it before returning.

# Constraints: You may use one list as auxiliary storage. 
# Do not declare any other auxiliary data structures, but you can have as many simple variables as you like. 
# Your solution should run in O(N) time, where N is the number of elements of the list. 



def is_stack_sorted (givenstack):
    bucket = []
    goodsofar = True
    # print (givenstack.pop())
    # print (givenstack.pop())

    while len(givenstack) > 0 and goodsofar: 
        bucket.append(givenstack.pop())
        if len(bucket) > 1:
            if bucket[-1] < bucket[-2] :
                goodsofar = False

    while len(bucket) > 0:
        givenstack.append(bucket.pop())

    return goodsofar


## testing 

stack1 = [1,3,4,5,6,7]

stack2 = [8,7,6,5,4,3]

print (is_stack_sorted(stack1))
print (is_stack_sorted(stack2))
            




    