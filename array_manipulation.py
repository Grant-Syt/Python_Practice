from collections import Counter
from time import perf_counter
from random import randint

"""
This function runs a test on the 3 methods implemented below.
The amount of data being processed can be adjusted with the
first two variables declared in the function.
"""
def main():
    # array size
    n = 1000000
    # max value to add to some range of the array
    max_k = 1000000

    # randomly build queries based on above values
    queries = []
    for i in range(100):
        a = randint(1, n)
        b = randint(a, n)
        k = randint(1, max_k)
        queries.append([a, b, k])

    # print(f"n: {n}\nqueries: \n{queries}")

    func2run = [arrayManipulation_1, arrayManipulation_2, arrayManipulation_3]
    times = []
    for i, func in enumerate(func2run):    

        times.append(time_func(func, n, queries))
        print(f"time{i+1}: {times[i]}")

    print(f"method 1 is {round(times[1]/times[0])}x faster than method 2")
    print(f"method 1 is {round(times[2]/times[0])}x faster than method 3")

# Use counter as a dictionary, so you can use keys
# that aren't initialized. Then sort so you can 
# iterate through just the ups and downs in order.
def arrayManipulation_1(n, queries):
    # Counter is used for counting duplicate elements 
    # in strings and lists.
    # In this case it is used as a dictionary, but
    # it doesn't throw errors when assigning a value
    # to a non existant key.
    c = Counter()
    for a,b,k in queries:
        # We don't need to worry about a and b being
        # 1-indexed, because we are just tracking the
        # ups and downs with a dictionary.
        c[a]  +=k
        c[b+1]-=k
    currSum = 0
    maxSum = 0
    # Using a dictionary saves us time here because
    # we don't need to iterate through the parts of 
    # the array where no changes happen.
    # However, we do need to sort based on the keys
    # to calculate the correct maxSum. In other
    # words, we need to travese the changes in
    # the order they would have in the array.
    # We also cut off the last entry because it must
    # be a "b" which is always subtraction.
    for i in sorted(c)[:-1]:
        currSum+= c[i]
        maxSum = max(maxSum,currSum)
    return maxSum

# Still use an array, but only record the ups and downs.
# Then iterate through the whole array.
#
# This wastes a lot of time iterating through parts of
# the array where no changes occur.
def arrayManipulation_2(n, queries):
    arr = [0 for _ in range(n)]
    # just record the ups and downs.
    # the value of i is the difference
    # between i and i-1.
    for a, b, k in queries:
        # values given are 1-indexed
        a_idx = a-1
        b_idx = b-1
        arr[a_idx] += k
        if(b_idx+1<n): arr[b_idx+1] -= k
    cur_sum = 0 
    max_sum = 0
    # sum all values as you iterate throught the array
    # to compute the value at each index. keep track of
    # the max.
    for i in arr:
        cur_sum += i
        max_sum = max(max_sum, cur_sum)
    return max_sum

# naive solution
# Keep track of the max as you add all the queries 
# to a real array.
def arrayManipulation_3(n, queries):
    arr = [0 for i in range(0, n)]
    max_v = 0
    # iterate through queries
    for a, b, k in queries:
        # compute all the values
        for j in range(a-1, b):
            v = arr[j] + k
            arr[j] = v
            # update max as you go
            if v > max_v: 
                max_v = v
    return max_v

def time_func(func, *params):
    start = perf_counter()
    func(*params)
    end = perf_counter()
    return end-start

if __name__ == "__main__":
    main()