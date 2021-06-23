#https://www.geeksforgeeks.org/selection-sort/
def sort(arr):

    for i in range(len(arr)):
        minIdx = i
        for j in range(i+1, len(arr)):
            if(arr[minIdx] > arr[j]):
                minIdx = j

        arr[i], arr[minIdx] = arr[minIdx], arr[i]
