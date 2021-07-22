def kthSmallest(arr, n, k):
 
    # Sort the given array
    arr.sort()
 
    # Return k'th element in the
    # sorted array
    return arr[k-1]
 
# Driver code
if __name__=='__main__':
    arr = []
    arr = list(map(int,input("Enter the elements ").split()))
    n = len(arr)
    k = 2
    print("K'th smallest element is",
          kthSmallest(arr, n, k))
