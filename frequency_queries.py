from collections import Counter

def main():
    ops = """
            1 5 
            1 6 
            3 2
            1 10
            1 10 
            1 6 
            2 5 
            3 2 """
    ops = ops.split()
    ops = [[int(ops[a]), int(ops[a+1])] for a in range(0, len(ops)-1, 2)]
    print(ops)
    print(freqQuery(ops))

def freqQuery(queries):
    numCount = Counter()  # count numbers
    valCount = Counter()  # track values of numbers
    s = []
    for q in queries:
        op = q[0]
        data = q[1]
        if (op == 1):  # insert
            old_val = numCount[data]
            new_val = old_val + 1
            if old_val > 0:
                # subtract count of old val
                valCount[old_val] -= 1
            numCount[data] = new_val
            # add to count of new val
            valCount[new_val] += 1
        if op == 2:  # delete
            old_val = numCount[data]
            new_val = old_val - 1
            if old_val > 0:
                numCount[data] = new_val
                # adjust val counts
                valCount[old_val] -= 1
                valCount[new_val] += 1
        if op == 3:  # check
            s.append(1) if data in valCount else s.append(0)
    return s

if __name__ == "__main__":
    main()