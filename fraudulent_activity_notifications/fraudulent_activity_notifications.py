from bisect import bisect
import math

## My solution ##############################

def activityNotifications(expenditure, d):
    # Write your code here
    n = len(expenditure)
    notices = 0
    
    for i in range(0, n-d, 1):

        # trailing expenditures for day i+d
        if i == 0:
            te = sorted(expenditure[i:i+d])
        else:
            # remove outgoing value on left side of sliding window
            old_val = expenditure[i-1]
            te.remove(old_val)
            # insert incoming value in the right place to keep te sorted
            new_val = expenditure[i+d-1]
            te.insert(bisect(te, new_val), new_val)
        
        # the day's expenditure
        de = expenditure[i+d]
        
        # print(f"te: {te}, de: {de}")
        # print(f"2*median(te) = {2*median(te)}")
        if de >= 2*median(te):
            notices += 1

    return notices

def median(l):
    n = len(l)
    if n%2 == 0:
        a = l[n//2 - 1]
        b = l[n//2]
        # print(f"a: {a}, b: {b}, avg: {normal_round((a+b)/2)}")
        return normal_round((a+b)/2)
    else:
        return l[normal_round(n/2) - 1]
    
def normal_round(n):
    return math.floor(n) if n - math.floor(n) < 0.5 else math.ceil(n)


## Website solution ##############################

def get_limit(f,d):
    count = 0 
    m1,m2 = (d//2,d//2+1)
    m = []
    for i,j in enumerate(f):
        count+=j
        if not m and m1<=count:
            m.append(i)
        if m2<=count:
            m.append(i)
            break
    return m[-1]*2 if d%2 else sum(m)

def activityNotifications2(e, n, d):
    f = [0]*201
    count = 0
    for i in e[:d]:
        f[i]+=1
    for i,v in enumerate(e[d:]):
        limit = get_limit(f,d)
        if v>=limit:
            count+=1
        f[v]+=1
        f[e[i]]-=1

    return count