
def main():
    q = []
    minimumBribes(q)

def minimumBribes(q):
    # Write your code here
    
    count = 0
    # Iterate through each person in the queue.
    for i in range(0, len(q)):
        old_pos = q[i]
        new_pos = i+1
        
        # Can't bribe more than two people.
        # 
        # old_pos can't be more than two positions
        # to the right because they can only bribe twice  
        # but can be to the left because
        # they can get bribed any number of times.
        if old_pos > new_pos + 2:
            print("Too chaotic")
            return
        
        # count people that bribed the current person
        # 
        # Only checks things to the left because range
        # is empty if the first arg is >= the second.
        # Counts the people that bribed the current
        # person if they moved toward the back of the
        # queue.
        # old_pos-1 is the original index of the current
        # person.
        # old_pos-2 is the furthest index that a person
        # that bribed the current person could be located
        # because the first bribe takes the orignial 
        # position and the second bribe takes the position
        # to the left.
        for j in range(max(old_pos-2, 0), i):
            if q[j] > old_pos:
                count += 1
                # print(f"{old_pos} was bribed by {q[j]}")
    print(f"{count}")
    return

if __name__ == "__main__":
    main()
