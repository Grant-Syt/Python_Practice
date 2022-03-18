
def activityNotifications(expenditure, d):
    # Write your code here
    n = len(expenditure)
    notices = 0
    for i in range(0, n-d, 1):
        # trailing expenditures for day i+d+1
        te = expenditure[i:i+d]
        print(te)
        # the day's expenditure
        de = expenditure[i+d]
        print(de)
        print(sorted(te))
        print(median(te))
        if de >= 2*median(te):
            notices += 1
    return notices

def median(l):
    l = sorted(l)
    n = len(l)
    if n%2 == 0:
        a = l[n/2 - 1]
        b = l[n/2]
        return round((a+b)/2)
    else:
        return l[round(n/2)]