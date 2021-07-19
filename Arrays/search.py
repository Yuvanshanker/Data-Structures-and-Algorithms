def findElement(arr, n, key):
    for i in range (n):
        if (arr[i] == key):
            return i
    return -1

arr = []
arr = list(map(int,input("Enter the elements").split()))

print(arr)
key = 10
n = len(arr)
#search operation
index = findElement(arr, n, key)
if index != -1:
    print ("element found at position: " + str(index + 1 ))
else:
    print ("element not found")
