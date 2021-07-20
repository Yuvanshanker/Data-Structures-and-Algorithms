def getOddOccurrence(arr, arr_size):
     
    for i in range(0,arr_size):
        count = 0
        for j in range(0, arr_size):
            if arr[i] == arr[j]:
                count+=1
             
        if (count % 2 != 0):
            return arr[i]
         
    return -1
     
     
# driver code
arr = []
arr = list(map(int,input("Enter the elements ").split()))
n = len(arr)
print(getOddOccurrence(arr, n))
