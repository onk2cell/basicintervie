#Python programe to find the frime fact of number 

def fact(n):
    if n == 0 :
        return 1
    
    return fact(n-1)*n


k = fact(n=5)
print(k)