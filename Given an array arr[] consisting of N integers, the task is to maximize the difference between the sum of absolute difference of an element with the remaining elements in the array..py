#Given an array arr[] consisting of N integers, the task is to maximize the difference between the sum of absolute difference of an element with the remaining elements in the array.
"""Input: arr[] = {1, 2, 4, 7}
Output: 6
Explanation:
For i = 1, |1 – 2| + |1 – 4| + |1 – 7| = 1 + 3 + 6 =10.
For i = 2, |2 – 1| + |2 – 4| + |2 – 7| = 1 + 2 + 5 = 8.
For i = 3, |4 – 1| + |4 – 2| + |4 – 7| = 3 + 2 + 3 = 8.
For i = 4, |7 – 1| + |7 – 2| + |7 – 4| = 6 + 5 + 3 = 14.
Maximum=14, Minimum=8.
Therefore, the maximum difference = 14 – 8 = 6.

Input: arr[] = {2, 1, 5, 4, 3}
Output: 4"""


arr = [2, 1, 5, 4, 3]

def min(arr,neg=1):
    for i in arr:
       k = i - neg
       print(k) 


