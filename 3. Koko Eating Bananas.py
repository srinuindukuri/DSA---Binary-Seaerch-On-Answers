# Problem Statement: A monkey is given ‘n’ piles of bananas, whereas the ‘ith’ pile has ‘a[i]’ bananas.
# An integer ‘h’ is also given, which denotes the time (in hours) for all the bananas to be eaten.

# Each hour, the monkey chooses a non-empty pile of bananas and eats ‘k’ bananas.
# If the pile contains less than ‘k’ bananas, then the monkey consumes all the bananas and won’t eat any more bananas in that hour.

# Find the minimum number of bananas ‘k’ to eat per hour so that the monkey can eat all the bananas within ‘h’ hours.

# -----------------------------------------------------------------------------------------------------------------------------------

import math

# To find the Max Range


def findmax(v):
    maxi = float('-inf')
    n = len(v)
    # Find the minimum
    for i in range(n):
        maxi = max(maxi, v[i])
    return maxi

# To Calculate total Hours


def CalculateTotalHours(v, hourly):
    TotalH = 0
    n = len(v)
    # Find the total hours

    for i in range(n):
        TotalH += math.ceil(v[i]/hourly)
    return TotalH


def minimumRateToEatBananas(v, h):
    low = 1
    high = findmax(v)

    # Apply Binary Search
    while(low <= high):
        mid = (low+high) // 2
        TotalH = CalculateTotalHours(v, mid)
        if(TotalH <= h):
            high = mid-1
        else:
            low = mid+1
    return low


v = [7, 15, 6, 3]
h = 8
ans = minimumRateToEatBananas(v, h)
print("Koko should eat at least", ans, "bananas/hr.")
