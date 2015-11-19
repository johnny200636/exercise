import math

input_number = input('Please enter a integer:')
List_prime_number = [1]

if float(input_number).is_integer() == False:
    input_number =  input('Input a integer, you dumbass == :')
if input_number == 1:
    print 1
    
for x in range(2,input_number+1):
    determinant = 0
    for y in range(0,len(List_prime_number)):
        if List_prime_number[y] > int(math.sqrt(x)//1):
            break
        if (float(x)/float(List_prime_number[y])).is_integer() == True:
            determinant = determinant + 1
    if determinant == 1:
        List_prime_number.append(x)
List_prime_number.remove(1)
print List_prime_number


    
