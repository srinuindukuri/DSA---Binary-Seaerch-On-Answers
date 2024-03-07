# Problem Statement: You are given an array ‘arr’ of size ‘n’ which denotes the position of stalls.
# You are also given an integer ‘k’ which denotes the number of aggressive cows.
# You are given the task of assigning stalls to ‘k’ cows such that the minimum distance between any two of them is the maximum possible.
# Find the maximum possible minimum distance.

# --------------------------------------------------------------------------------------------------------------------------------------

def canweplease(stalls, dist, cows):
    n = len(stalls)  # Size of array
    Countcows = 1  # Number of Cows Placed
    last = stalls[0]  # Position of Last Placed Cow

    for i in range(1, n):
        if (stalls[i] - last >= dist):
            Countcows += 1  # Place Next Cow
            last = stalls[i]  # Update Last Location
        if(Countcows >= cows):
            return True
    return False


def aggressiveCows(stalls, cows):
    n = len(stalls)  # Size of Array
    stalls.sort()  # Sort the Stalls
    low = 1
    high = stalls[n-1] - stalls[0]  # Example - high = Max[n-1] - Min[0]

    # Apply Binary Search
    while(low <= high):
        mid = (low+high) // 2
        if canweplease(stalls, mid, cows):
            low = mid+1
        else:
            high = mid-1
    return high


stalls = [0, 3, 4, 7, 10, 9]
cows = 4
ans = aggressiveCows(stalls, cows)
print("THE Maximum possible minimum distance is:  ", ans)

# Time Complexity: O(NlogN) + O(N * log(max(stalls[])-min(stalls[])))
# Space Complexity: O(1)
