from collections import Counter

def main():
    print(sherlockAndAnagrams("abba"))
    print("expected: 4")

def sherlockAndAnagrams(s):
    # Write your code here
    
    # substring dict to match substrings to
    d = Counter()
    # substring list to traverse and reverse
    l = []
    
    # get substrings
    i = 0
    while (i < len(s)):
        j = i
        while (j < len(s)):
            v = s[i:j+1]
            if len(v) != 1 and len(v) != len(s):
                d[v] = 0
                l.append(v)
            j += 1
        i += 1
    
    print(l)
    
    # pick a substring, don't compare against itself
    # check anagrams
    count = 0
    for a in l:
        a_rev = a[::-1]
        if a_rev in d:
            count += 1
    
    return count