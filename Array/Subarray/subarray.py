
def PrintSubArray(arr):

    subarray = [[]]    # variable to store subarray

    for i in range(len(arr)+1):                          # run a loop till the end of given list
        for j in range(i+1,len(arr)+1):                  # Iterate over a loop from i+1 to end(length)
            sub = arr[i:j]                               # of the list to get all the sublists from i to its right.
            subarray.append(sub)
    return subarray

list = [1,2,3,4]
print(PrintSubArray(list))