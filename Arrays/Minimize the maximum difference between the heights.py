def getMinDiff(arr, n, k):
        arr.sort()  #sorting the array
        ans=arr[n-1]-arr[0] #it's same as substracting an+k-(ao+k) or an-k-(a0-k)
        small,big=0,0
         
        for i in range(1,n):#trying to make each tower highest
          small=min(arr[0]+k,arr[i]-k) #finding minimum tower height
          big=max(arr[i-1]+k,arr[-1]-k) #finding maximum tower height
          ans=min(ans,big-small) #checking whether we get smaller value as result
             
             
             
        return ans
arr=[]
arr = list(map(int,input("Enter the elements ").split()))
k=6
printgetMinDiff(arr,len(arr),k)
