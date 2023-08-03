#sum of all numbers upto n 

def sum(n):
    if n == 1 :
        return n 
    else:
        return n + sum(n-1)
    

k = sum(21)
print(k)