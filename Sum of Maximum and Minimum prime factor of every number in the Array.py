def isprime(i):
    for k in range(2,int(i**0.5+1)):
        if i%k == 0 :
            return False
    return True


def find(n):
    sum = 0
    for i in range(1,n+1):
        if n%i == 0 and isprime(i):
            sum = sum + i
    print(sum)


#k = find(15)
find(25)
