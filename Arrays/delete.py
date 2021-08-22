arr = []
arr = list(map(int,input("Enter the elements").split()))
key = int(input())
  
print("Array before deletion:")
print (arr)
  
# deletes key if found in the array
# otherwise shows error not in list
arr.remove(key)
print("Array after deletion")
print(arr)
