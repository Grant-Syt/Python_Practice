from collections import Counter


def main():
    print("expected 2")
    print(count_triplets_1([1, 2, 2, 4], 2))
    print(count_triplets_2([1, 2, 2, 4], 2))
    print(count_triplets_3([1, 2, 2, 4], 2))
    print(count_triplets_4([1, 2, 2, 4], 2))


def count_triplets_1(arr, r):
    # nieve solution, too slow
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


def count_triplets_2(arr, r):
    # wrong in some test cases
    # Single pass through data, O(n).
    #
    # Build dict; key: num, val: num of occurances.
    #
    # If you work backwards you only need to multiply
    # to check if you have seen the right numbers.
    #
    # Multiply alternative options. Don't over count
    # the first number in the triplets.

    c = Counter()
    count = 0
    for e in reversed(arr):
        c[e] += 1
        if e*r in c and e*r*r in c:
            count += 1 * c[e*r] * c[e*r*r]  # mult options
    return count


def count_triplets_3(arr, r):
    # Source: HR discussion tab
    # website solution
    #
    # Still uses division, which is apparently
    # not required

    a = Counter(arr)  # unprocessed
    b = Counter()  # processed
    s = 0
    for i in arr:
        j = i//r  # preceding number
        k = i*r  # following number
        a[i] -= 1  # don't over count
        if b[j] and a[k] and i % r == 0:
            s += b[j]*a[k]  # count combinations
        b[i] += 1  # move to b
    return s

def count_triplets_4(arr, r):
    # Source: HR discussion tab
    # my version of smart guy solution
    #
    # track partially complete triplets with
    # dicts

    pt2 = Counter() # partial triplets
    pt3 = Counter()
    count = 0
    for e in arr:
        if(pt3[e]):
            count += pt3[e] # complete triplets
        if(pt2[e]):
            pt3[e*r] += pt2[e] # 2/3 triplets
        pt2[e*r] += 1 # 1/3 triplets
    return count


if __name__ == "__main__":
    main()
