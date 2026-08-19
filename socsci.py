def greet_students(name, nChar):
    for i in range(nChar):
        print(name[i])

name = input("Enter a Name : ")
nChar = input("Enter any numeric number : ")
nChar = int(nChar)
greet_students(name, nChar)




def greet_students(name, nChar):
    for i in range(nChar):
        # Subtract i to shorten the slice each step
        print(name[0 : nChar - i])

name = input("Enter a Name: ")
greet_students(name, len(name))



def sum_of_squared(n):
    total_sum = 0
    for i in range(1, n + 1):
        total_sum += i ** 2
    return total_sum

n = 0
while n < 1 or n > 100:
    n = input("Enter a Number from 1 to 100 : ")
    n = int(n)

print("Sum of all squared numbers is", sum_of_squared(n))

