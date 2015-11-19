import math

input_number =  input('Please enter a integer : ')
while float(input_number).is_integer() == False:
    input_number =  input('Please enter a integer : ')

List_prime_number = [1]
for x in range(2,input_number+1):
    determinant = 0
    for y in range(0,len(List_prime_number)):
        if determinant == 2: break
        if x%List_prime_number[y] == 0:
            determinant = determinant + 1
    if determinant == 1:
        List_prime_number.append(x)
        print x,
print ('')
del List_prime_number[:]

