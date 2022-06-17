
from pprint import pprint


def main():
    arr = [2, 3, 6, 1, 5, 4]
    allSubarry(arr)
    print("")
    allSubsequence(arr)


def allSubarry(arr):
    res = [arr[i:j] for i in range(len(arr)) for j in range(i+1, len(arr)+1)]
    pprint(res)
    return res


def allSubsequence(arr):
    subseqHelper(arr, 0, [])


def subseqHelper(arr, i, subarr):
    # base case
    if i == len(arr):
        print(subarr)
    else:
        # ignore ith
        subseqHelper(arr, i+1, subarr)
        # add ith
        subseqHelper(arr, i+1, subarr+[arr[i]])
    return


main()
