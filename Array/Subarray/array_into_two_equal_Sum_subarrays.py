#Split an array into two equal Sum subarrays
def SplitPoint(arr,n):
    
    left_sum = 0 
    
    for i in range(0,n):
        left_sum +=arr[i]
        
    right_sum = 0
    for i in range(n-1,-1,-1):
        right_sum +=arr[i]
        
        left_sum -= arr[i]
        
        if left_sum == right_sum:
            return i 
    return -1

def printSubArray(arr,n):
    
    splitpoint = SplitPoint(arr,n)
    
    if splitpoint == -1 or splitpoint == n:
        print('Cannot Continue')
    
    for i in range(0,n):
        if splitpoint==i:
            print()
        print (arr[i],end=' ')

if __name__ == "__main__":
    arr = [1,2,3,4,5,5]
    n=len(arr)
    printSubArray(arr,n)

#Time complexity = O(n)
#space complexity = O(1)
        