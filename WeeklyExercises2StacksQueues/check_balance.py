
# use the stack 

#  check_balance
# Language/Type:Python

#     listcollectionsstring

# Author:Marty Stepp on 2017/07/07

# Write a function named check_balance that accepts a string of source code and uses a list to check whether the braces/parentheses are balanced. 
# Every ( or { must be closed by a } or ) in the opposite order. 
# Return the index at which an imbalance occurs, or -1 if the string is balanced. 
# If any ( or { are never closed, return the string's length.

# Here are some example calls:

# #    index   0123456789012345678901234567890
# check_balance("if a(4) > 9: foo(a(2)) }")      # returns -1 because balanced
# check_balance("for (i=0i&lta(3}i += 1): foo{) )")   # returns 14 because } out of order
# check_balance("while True) foo() }{ ()"         # returns 20 because } doesn't match any {
# check_balance("if x:")                          # returns 8 because { is never closed

# Constraints: Use a single stack as auxiliary storage. 



def check_balance (source):

    indexOfProblem = -1
    stack = []
    for aLetter in source:
        indexOfProblem += 1


        if aLetter == "{" or aLetter == "[" or aLetter == "(":
            stack.append ( aLetter )
        
        if aLetter == "}" or  aLetter == ")" or aLetter == "]":
            if len(stack) == 0:
                return indexOfProblem
            
            if aLetter == "}" :
                if stack[-1] == "{": 
                    stack.pop() 
                else:
                    return indexOfProblem

            if aLetter == ")" :
                if stack[-1] == "(": 
                    stack.pop() 
                else:
                    return indexOfProblem

            if aLetter == "]" : 
                if stack[-1] == "[": 
                    stack.pop() 
                else:
                    return indexOfProblem
                
    if len(stack) > 0:
        return indexOfProblem + 1 
    else: 
        return -1 


# test code:

print(check_balance("ftgyuhijouyty;'][p=-o0ooplo0]"))
print(check_balance("{[()]}"))

print (check_balance ("()"))
            



            



    

    

