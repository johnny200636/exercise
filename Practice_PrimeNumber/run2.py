import math

while True:
    try:
        input_number =  input('Please enter a integer : ')
        int(str(input_number))
        break
    except:
        print ('Not  a integer')
    
def IsPrime(i):
    limit = int(math.sqrt(i)//1)
    for number in range(0,limit+1):
        if i < 2: break
        if limit < 2:
            print i,
            break
        if number < 2: continue
        if i%number == 0:
            break
        if number == limit:
            print i,
            break

for number in range(0,input_number+1):
    IsPrime(number)

print ('')

