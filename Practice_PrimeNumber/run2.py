import math

while True:
    try:
        input_number =  int(input('Please enter a integer : '))
        int(str(input_number))
        break
    except:
        print ('Not  a integer')
    
def IsPrime(i):
    limit = int(math.sqrt(i)//1)
    if i == 2 or i ==3:
        return True
    for number in range(2,limit+1):
        if i%number == 0:
            return False
            break
        if number == limit:
            return True
            break

for number in range(0,input_number+1):
    if IsPrime(number):
        print (number, end = ' ')
print ('', end = '\n')
