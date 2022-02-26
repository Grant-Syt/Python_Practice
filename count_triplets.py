
def main():
    count_triplets_1([1,2,2,4], 2)

# nieve solution
def count_triplets_1(arr, r):
    # need all size 3 subsets
    # sequential but not necessarily adjacent
    # check for geometric progression
    
    # nieve solution: triple for loop
    count = 0
    n = len(arr)
    for i in range(0, n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                ss = [arr[i], arr[j], arr[k]]
                # print(ss)
                if (ss[0]*r == ss[1] and ss[1]*r == ss[2]):
                    count += 1
    return count

if __name__ == "__main__":
    main()