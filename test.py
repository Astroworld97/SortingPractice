import math
def main():
    arr = [0, 1, 2, 3, 4, 5]

    leftIdx = 0
    midIdx = math.floor(len(arr) / 2)
    rightIdx = len(arr)

    newArrLeft = []
    for i in range(leftIdx, midIdx):
        newArrLeft.append(i)

    print("newArrLeft: ")
    for x in newArrLeft:
        print(x)

    newArrRight = []
    for i in range(midIdx, rightIdx):
        newArrRight.append(i)

    print("newArrRight: ")
    for x in newArrRight:
        print(x)


if __name__ == '__main__':
    main()