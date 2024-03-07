# Problem Statement: Given two numbers N and M, find the Nth root of M.
# The nth root of a number M is defined as a number X when raised to the power N equals M.
# If the ‘nth root is not an integer, return -1.
# -----------------------------------------------------------------------------------------------------------------------

def func(n, m, mid):
    ans = 1
    for i in range(1, n+1):
        ans *= mid
        if(ans > m):
            return 2
    if(ans == m):
        return 1
    return 0


def Nroot(n, m):
    low = 1
    high = m
    while(low <= high):
        mid = (low+high) // 2
        midN = func(n, m, mid)
        if(mid == 1):
            return mid
        elif midN == 0:
            low = mid+1
        else:
            high = mid-1
    return -1


n = 3
m = 27
ans = Nroot(n, m)
print("The Answer is: ", ans)
