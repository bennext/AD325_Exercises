
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
    
    DEBUG = True
    class Stack:
        def __init__(self, optional_max_length = -1):
            self.stack_list = []
            self.max_length = optional_max_length

        def __len__(self):
            return len(self.stack_list)

        def len(self):
            return len(self.stack_list)
        
        def pop(self):
            return self.stack_list.pop()
        
        def push(self, item):
            if len(self.stack_list) == self.max_length:
                if DEBUG:
                    print("Stack is Full")
                return False
            
            self.stack_list.append(item)
            return True
        
        def print_list(self):
            print(self.stack_list)

        def top(self):
            # empty list will throw error 
            return self.stack_list[-1]

    indexOfProblem = -1
    stack = Stack()
    for aLetter in source:
        indexOfProblem += 1
        # if DEBUG: 
        #     print(aLetter)

        if aLetter == "{" or aLetter == "[" or aLetter == "(":
            stack.push ( aLetter )
        
        if aLetter == "}" or  aLetter == ")" or aLetter == "]":
            if stack.len() == 0:
                return indexOfProblem
            
            if aLetter == "}" :
                if stack.top() == "{": 
                    stack.pop() 
                else:
                    return indexOfProblem

            if aLetter == ")" :
                if stack.top() == "(": 
                    stack.pop() 
                else:
                    return indexOfProblem

            if aLetter == "]" : 
                if stack.top() == "[": 
                    stack.pop() 
                else:
                    return indexOfProblem

    return -1 


# test code:

print(check_balance("ftgyuhijouyty;'][p=-o0ooplo0]"))
print(check_balance("{[()]}"))

print (check_balance ("()"))
            



            



    

    

