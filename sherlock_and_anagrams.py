from collections import Counter
from itertools import count

def main():
    s = "cdcd"
    # print(f"My Solution: {sherlockAndAnagrams_mySolution(s)}")
    print(f"Example Solution: {sherlockAndAnagrams_exampleSolution(s)}")
    print("Expected: 5")

def sherlockAndAnagrams_mySolution(s):
    # Write your code here
    
    # get substrings
    l = []
    i = 0
    while (i < len(s)):
        j = i
        while (j < len(s)):
            ss = s[i:j+1]
            if len(ss) == len(s):
                # full string won't match with anything
                break
            l.append(ss)
            j += 1
        i += 1

    # print()
    # print(l)

    # compare characters
    # this over counts by counting every ordering
    count = 0
    for i, ss in enumerate(l):
        rest = l[:i] + l[i+1:]
        # print(ss)
        # print(rest)
        for other in rest:
            # only need to compare same length substrings
            if len(ss) == len(other):
                c1 = Counter(ss)
                c2 = Counter(other)
                if c1.items() == c2.items():
                    # print(f"[{ss}, {other}]")
                    count += 1
    
    return count

def sherlockAndAnagrams_exampleSolution(str_input):
    
    # find substrs with list comprehension
    def all_substrs_list_comp(str_input):
        
              #           (3)                                        (2)
        sub_strs = [[str_input[j:j+i] for j in range(len(str_input) - i + 1)] 
                                for i in range(1, len(str_input))] # (1)
        # 1. outer loop - i is the length of the slice; 
        #                   stops before the full string;
        #                   makes list of lists
        # 2. inner loop - j is the start index of the slice;
        #                   stops before the first out of range slice;
        #                   the +1 is because the stop is non-inclusive;
        #                   makes list
        # 3. slice s from j to j+i
        
        # print(ss)
        return sub_strs

    # find substrs, easier to read
    def all_substrs(str_input):
        sub_strs = []
        n = len(str_input)
        for i in range(1, n): # sub string length
            arr = []
            for j in range(n - i + 1): # starting points for slicing
                arr.append(str_input[j:j+i])
            sub_strs.append(arr)
        return sub_strs

    def all_subarry(arr):
        res = [arr[i:j] for i in range(len(arr)) for j in range(i+1, len(arr)+1)]
        return res

    # count anaagrams by sorting substrs
    def count_anagrams_sort_impl(sub_strs):
        anagram_counts = Counter()
        count = 0
        for i in sub_strs:
            for i in i:
                q = ''.join(sorted(i))
                anagram_counts[q] += 1   # count sorted strings
        # print(c)
        for i in anagram_counts:
            count += int(anagram_counts[i]*(anagram_counts[i]-1)/2) # simplified "n choose 2"
        return count

    # count anagrams by comparing character counts, faster
    # def count_anagrams_char_count_impl():

    print(all_substrs(str_input))
    print(all_substrs_list_comp(str_input))
    print(all_subarry(str_input))

    return count_anagrams_sort_impl(all_substrs(str_input))
    

if __name__ == "__main__":
    main()