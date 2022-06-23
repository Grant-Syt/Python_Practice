from collections import Counter
from itertools import count


def main():
    s = "cdcd"
    # s = "zxmcvl;asjdofiwjad.,msdj"
    print(f"Overcounting Solution: {overcounting_solution(s)}")
    print(f"Sorting Solution: {sorting_solution(s)}")
    print(f"Character Frequency Solution: {char_freq_solution(s)}")
    print("Expected: 5")


def overcounting_solution(s):
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


# count anaagrams by sorting substrs
def sorting_solution(str_input):

    def count_anagrams_sort_impl(sub_strs):
        anagram_counts = Counter()
        count = 0
        for sub_str_list in sub_strs:
            for sub_str in sub_str_list:
                sorted_sub_str = ''.join(
                    sorted(sub_str))  # sorted returns list
                anagram_counts[sorted_sub_str] += 1   # count sorted strings
        # print(c)
        for key in anagram_counts:
            # simplified "n choose 2"
            count += int(anagram_counts[key] * (anagram_counts[key]-1) / 2)
        return count

    return count_anagrams_sort_impl(all_substrs(str_input))


# count anagrams by comparing character counts, faster without sorting
def char_freq_solution(str_input):

    def count_anagrams_char_count_impl(sub_strs):
        num_anagrams = 0        
        char_freqs = get_char_freqs(sub_strs)
        for len_group in sub_strs:
            num_anagrams += compare_char_freq(len_group, char_freqs)
        return num_anagrams

    def compare_char_freq(len_group, char_freqs):
        num_anagrams = 0
        for i in range(len(len_group)-1):
            for j in range(i+1, len(len_group)):
                freqs1 = char_freqs[len_group[i]]
                freqs2 = char_freqs[len_group[j]]
                if freqs1 == freqs2:
                    num_anagrams += 1
        return num_anagrams

    def get_char_freqs(sub_strs):
        char_freqs = {}
        for len_group in sub_strs:
            for sub_str in len_group:
                char_freq = Counter(sub_str)
                char_freqs[sub_str] = char_freq
        return char_freqs

    return count_anagrams_char_count_impl(all_substrs(str_input))


# find substrs with list comprehension
def all_substrs_list_comp(str_input):

    #           (3)                                        (2)
    sub_strs = [[str_input[j:j+i] for j in range(len(str_input) - i + 1)]
                for i in range(1, len(str_input))]  # (1)
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
    for i in range(1, n):  # sub string length
        arr = []
        for j in range(n - i + 1):  # starting points for slicing
            arr.append(str_input[j:j+i])
        sub_strs.append(arr)
    return sub_strs

def all_subarry(arr):
    res = [arr[i:j] for i in range(len(arr))
            for j in range(i+1, len(arr)+1)]
    return res


if __name__ == "__main__":
    main()
