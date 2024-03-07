# Problem Statement: You are given a positive integer n. Your task is to find and return its square root.
# If ‘n’ is not a perfect square, then return the floor value of ‘sqrt(n)’.

# -----------------------------------------------------------------------------------------------------------------------

def Sqrt(n):
    low = 1
    high = n

    while(low <= high):
        mid = (low+high) // 2

        if(mid*mid <= n):
            low = mid+1
        else:
            high = mid-1
    return high


n = 25
ans = Sqrt(n)
print("The Square root of given n is", ans)
