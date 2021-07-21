def hasArrayTwoCandidates(A, arr_size, sum):
     
    # sort the array
    quickSort(A, 0, arr_size-1)
    l = 0
    r = arr_size-1
     
    # traverse the array for the two elements
    while l<r:
        if (A[l] + A[r] == sum):
            return 1
        elif (A[l] + A[r] < sum):
            l += 1
        else:
            r -= 1
    return 0
 
# Implementation of Quick Sort
# A[] --> Array to be sorted
# si  --> Starting index
# ei  --> Ending index
def quickSort(A, si, ei):
    if si < ei:
        pi = partition(A, si, ei)
        quickSort(A, si, pi-1)
        quickSort(A, pi + 1, ei)
 
# Utility function for partitioning
# the array(used in quick sort)
def partition(A, si, ei):
    x = A[ei]
    i = (si-1)
    for j in range(si, ei):
        if A[j] <= x:
            i += 1
             
            # This operation is used to swap
            # two variables is python
            A[i], A[j] = A[j], A[i]
 
        A[i + 1], A[ei] = A[ei], A[i + 1]
         
    return i + 1
     
 
# Driver program to test the functions
A = []
arr = list(map(int,input("Enter the elements ").split()))
n = 16
if (hasArrayTwoCandidates(A, len(A), n)):
    print("Array has two elements with the given sum")
else:
    print("Array doesn't have two elements with the given sum")
