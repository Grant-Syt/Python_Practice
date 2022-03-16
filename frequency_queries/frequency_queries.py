from collections import Counter


def main():

    with open("./frequency_queries/input05.txt", "r") as input_file:
        queries = input_file.read()
    queries = queries.split()[1:]  # list excluding size
    # group query pairs
    queries = [[int(queries[a]), int(queries[a+1])]
               for a in range(0, len(queries)-1, 2)]
    # print(queries)

    print(freqQuery(queries))


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
            if old_val > 0:  # can delete
                numCount[data] = new_val
                # adjust val counts
                valCount[old_val] -= 1
                valCount[new_val] += 1
        if op == 3:  # check
            s.append(1) if valCount[data] > 0 else s.append(0)
    return s


if __name__ == "__main__":
    main()
