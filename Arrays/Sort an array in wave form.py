def sortInWave(arr, n):
     
    #sort the array
    arr.sort()
    
    # Swap adjacent elements
    for i in range(0,n-1,2):
        arr[i], arr[i+1] = arr[i+1], arr[i]
 
# Driver program
arr = []
arr = list(map(int,input("Enter the elements ").split()))
sortInWave(arr, len(arr))
for i in range(0,len(arr)):
    print (arr[i])
