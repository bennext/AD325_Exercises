# Given a target number, write a function to return the largest prime factor of that target number.

# For example, for the number 42, the prime factors are 2, 3, and 7, so we'd return 7 because that's the largest prime factor.

# For the number 25, it's prime factors are 5 and 5, so we'd return 5.

def largest_prime_factor(target):
    
    def is_prime(p): # checks if prime 
      p_number = int(p ** 0.5) + 1 # start with the sqrt rounded up
      p_range = range(p_number, 1,  -1) # lots of numbers in reverse order 

      for t in p_range:
         if p % t == 0: #checks prime
            return False
         
      return True
            
    
    my_number = int(target ** 0.5) + 1 # start with the sqrt rounded up

    my_range_list = range(my_number, 1,  -1) # lots of numbers in reverse order 

    for n in my_range_list:
        if target % n == 0: # looks for factors
          if is_prime(n) :
           return n
  
    
    return -1

# testings 

print(largest_prime_factor(25))

# my_number = 25 

# my_range_list = range(my_number, 1,  -1) 
# print (  my_range_list )

# for n in my_range_list:
#    print(n) 


