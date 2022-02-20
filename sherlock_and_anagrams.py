from collections import Counter

def main():
    s = "cdcd"
    print(f"My Solution: {sherlockAndAnagrams_mySolution(s)}")
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

def sherlockAndAnagrams_exampleSolution(s):
    
    def all_substrs(s):
        
              #   (3)   (2)                             (1)
        ss = [[s[j:j+i] for j in range(len(s) - i + 1)] for i in range(1, len(s))]
        # 1. outer loop - i is the length of the slice, 1-(len(s)-1), 
        #                   stops before the full string,
        #                   makes list of lists
        # 2. inner loop - j is the start index of the slice, 0-(len(s)-i+1),
        #                   stops before the first out of range slice,
        #                   the +1 is because the stop is non-inclusive,
        #                   makes list
        # 3. function of variables - slice s from j to j+i
        
        # print(ss)
        return ss

    def countem(ll):
        c = Counter()
        s = 0
        for lst in ll:
            for e in lst:
                q = ''.join(sorted(e))
                c[q] += 1   # count sorted strings
        # print(c)
        for e in c:
            s += int(c[e]*(c[e]-1)/2) # simplified "n choose 2"
        return s

    return countem(all_substrs(s))
    

if __name__ == "__main__":
    main()