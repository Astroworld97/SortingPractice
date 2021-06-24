# https://www.geeksforgeeks.org/merge-sort/
def sort(arr, leftIndex, rightIndex):
    if (rightIndex > leftIndex):
        midIndex = leftIndex + (rightIndex - leftIndex) / 2
        sort(arr, leftIndex, midIndex)
        sort(arr, midIndex + 1, rightIndex)


def merge(arr, leftIndex, rightIndex, midIndex):
    length1 = midIndex - leftIndex + 1  # length of left subarray
    length2 = rightIndex - midIndex  # length of right subarray

    # temp arrays

    leftArray = [i for i in arr if arr[leftIndex:midIndex]]
    rightArray = [i for i in arr if arr[midIndex:rightIndex]]

