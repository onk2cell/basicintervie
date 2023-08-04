#python prograne to find the sumof the num useing recurrion :


def sum(n):
    if n == 0 :
        return -1
    return sum(n-1) + n 


n = 56

k = sum(n)
print(k)