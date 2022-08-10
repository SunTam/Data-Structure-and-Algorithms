
def PrintSubArray(arr):

    subarray = [[]]    # variable to store subarray

    for i in range(len(arr)):                          # run a loop till the end of given list
        for j in range(i+1,len(arr)):                  # Iterate over a loop from i+1 to end(length)
            sub = arr[i:j]                               # of the list to get all the sublists from i to its right.
            subarray.append(sub)
    return subarray

list = [1,2,3,4]
print(PrintSubArray(list))
'''
def simple_loop(arr):
    container = []
    for i in range(3):
        container.append(arr[i])
    return print(container)
if __name__== "__main__":
    arr = [1,2,3]
    simple_loop(arr)

'''
