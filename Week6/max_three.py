# #max_three
# #Maximum Product of Three Numbers
# D.E. Shaw Python Interview Question

# Given a list of integers, return the maximum product of any three numbers in the array.

# For example, for A = [1, 3, 4, 5], you should return 60, since 3∗4∗5=603∗4∗5=60.

# For B = [−4, −2, 3, 5] you should return 40 since −4∗−2∗5=40−4∗−2∗5=40

# p.s. this is the same as question 9.2 in Ace the Data Science Interview.

def max_three(input):

    big_list = [1, 1, 1]
    negative_list = []

    for a_number in input:
        #positive numbers 
        if a_number > big_list[0]:
            big_list[0] = a_number
        elif a_number > big_list[1]:
            big_list[1] = a_number
        elif a_number > big_list[2]:
            big_list[2] = a_number
        
        #negative numbers 
        elif len(negative_list) < 2 and a_number < 0:
            negative_list.append(a_number)

        elif len(negative_list) >= 2:

            if a_number < negative_list[0]:
                negative_list[0] = a_number
            elif a_number < negative_list[1]:
                negative_list[1] = a_number
        
        big_list.sort()
        negative_list.sort()

    #compare 
    if sum( negative_list) < -2 and len(negative_list) >= 2:
        pos = big_list[0] * big_list[1]
        squ = negative_list[0] * negative_list[1]
        if pos <= squ:
            a, b, c = [negative_list[0], negative_list[1], big_list[2]]
            return a * b * c

    return big_list[0] * big_list[1] * big_list[2]


#testing 
#testing 

A = [1, 3, 4, 5]

B = [ -4, -2, 3, 5]

print(max_three(A))

print(max_three(B))

C = [-5, 5, 2, 1]
print(max_three(C))