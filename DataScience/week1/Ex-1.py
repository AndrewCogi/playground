import math

# define isPrime function
def isPrime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            return False;
    return True;

# test case 1
n=4
if isPrime(n) == True:
    print("result:",n,"is prime.")
else:
    print("result:",n,"is not Prime.")

# line clear
print()

# test case 2
n=32767
if isPrime(n) == True:
    print("result:",n,"is prime.")
else:
    print("result:",n,"is not Prime.")
