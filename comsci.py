# Code #1 Answers:

A. If name is “Joseph The Dreamer” and nChar is 5, what will be the output of the code above and why?

# The output of the code will be:
# J
# o 
# s 
# e 
# p 

# Since the function greet_students takes the name and nChar as inputs/values of the
#  given code, it will iterate through the first 5 characters of the name "Joseph The Dreamer" and print each character on a new line. The characters at index 0 to 4 are 'J', 'O', 'S', 'E', and 'P', which is why they are printed in that order.

# B. Using the same name and nChar is 20, what now is the output and why?

# The output of the code will be: 
# J
# o
# s 
# e 
# p 
# h 
#
# T 
# h 
# e 
#
# D 
# r 
# e 
# a 
# m 
# e
# r 
#Index error: string index out of range

#Since the function greet_students takes the name and nChar as inputs/values
#  of the given code, it will iterate through the first 20 characters of the name "Joseph The Dreamer". However, since the name only has 17 characters, it will print each character on a new line until it reaches the end of the string. After printing 'R', 'E', 'A', 'M', 'E', and 'R', it will attempt to access index 17, which does not exist, resulting in an IndexError: string index out of range.

# C. If there is an error message encountered in letter b, how will you be able to modify the code so that the error message will not appear.

#Since the error occurs when nChar is greater than the length of the name string,
#  we can modify the code to check if nChar is greater than the length of the name. If it is, we can manually set nChar value to the absolute length of the name string. For example, the name string "Joseph The Dreamer" has a length of 17, so if nChar is greater than 17, we can set nChar to exactly 18. This way, the function will only iterate through the valid indices of the name string and avoid the IndexError. (indices of 0 to 17).

Code #2 Answers:

#A. Find the syntax error and modify it. Please identify the error and what did you do to fix it?

#The syntax error is the missing colon (:) at the end of the for loop statement. 
# The correct syntax for the for loop should be with a colon at the end.



