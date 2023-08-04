# write python programe to given number is pallindome or not 

def pallin(n,revnum=0):
    if n == 0 :
        return revnum
    revnum = revnum*10 + n%10
    return(n//10,revnum)

