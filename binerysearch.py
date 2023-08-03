

def binary(arr,left,right,n):
    if left > right :
        return -1
    mid = left+right//2
    if n == mid :
        print(arr[mid])
    
    if n < mid :
        return binary(arr,left,mid-1,n)
    

arr = [1,2,3,4,5,6,21,22,23,24,25]
left = 0
right = len(arr)-1
print(right)
k = binary(arr,left,right,5)
print(k)