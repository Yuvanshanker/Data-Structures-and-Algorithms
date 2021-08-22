def insert(arr, element):
    arr.append(element)
 
# declaring array and key to insert
arr = []
arr = list(map(int,input("Enter the elements").split()))
key = int(input())
  
# array before inserting an element
print ("Before Inserting: ")
print (arr)
  
# array after Inserting element
insert(arr, key)
print("After Inserting: ")
print (arr)
