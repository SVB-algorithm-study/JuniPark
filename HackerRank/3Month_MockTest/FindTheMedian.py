#
# Complete the 'findMedian' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def findMedian(arr):
 # Write your code here
 n = len(arr)
 arr = sorted(arr)
 return arr[int((n-1)/2)]
