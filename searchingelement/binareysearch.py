data = [1,2,3,4,5,6,7,8,9]

ele = int(input("Enter the element that you want to search "))

def linmethod(data,ele):
    for i in range(len(data)):
        if ele == data[i]:
            return i 
        else :
            return -1 
linmethod(data,5)