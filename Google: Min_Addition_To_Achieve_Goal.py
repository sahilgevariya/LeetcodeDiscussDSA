# Leetcode : https://leetcode.com/problems/minimum-number-of-coins-to-be-added/

'''
- c is an array of positive integers and t is a positive integer representing our target.
- We want to use c to generate all the integers from 1 to t by picking any number of integers from c and add them.
- Note that each number from c can only be used once when contributing to a value between 1 and t.
- It is possible that array c is not able to achieve our goal. In such cases, we can add any integers we need into c to help achieve the goal.
- Return the minimum number of new values need to be added to array c to achieve our goal.

Example 1:
Input: c = [1,4,10], t = 19 Output: 2

Example 2:
Input: c = [1,4,10,5,7,19], t = 19  Output: 1

Example 3:
Input: c = [1,1,1], t = 20  Output:3
'''
import bisect
def isPossible(vals, n):
    idx = bisect.bisect_right(vals, n) - 1
    if vals[idx] == n:  return True

    while idx >= 0:
        n -= vals[idx]
        if n == 0:
            return True
        elif n < 0:   
            n += vals[idx]

        idx -= 1
    return False
    
# Greedy + Brute-Force ~(TC > nlogn)
def findMinNewValReqToAdded(vals, target):
    vals.sort()    # nlogn
    min_additions = 0
    num_to_added = []
    
    for num in range(1, target + 1):    # n * logn
        if not isPossible(vals, num):
            bisect.insort(vals, num)
            num_to_added.append(num)
            min_additions += 1
            
    # print(num_to_added)
    return min_additions

# Prefix sum (O(nlogn))
def optimal(nums, target):
    nums.sort()
        
    n = len(nums)
    obtainable_uptill = 0
    req_additions = 0
    idx = 0
    
    while idx < n and obtainable_uptill < target:
        unobtainable_coin = obtainable_uptill + 1
        
        # unobtainable_coin == nums[idx] is handle after while
        while unobtainable_coin < nums[idx]:
            # use the largest possible val (obtain + 1) as it doubles the obtainable range
            obtainable_uptill += unobtainable_coin
            unobtainable_coin = obtainable_uptill + 1
            req_additions += 1
            
        # now nums[idx] is in obtainable range, but with this num it increases our range
        obtainable_uptill += nums[idx]
        idx += 1
            
    while obtainable_uptill < target:
        obtainable_uptill += (obtainable_uptill + 1)
        req_additions += 1
            
    return req_additions
    
c = [1,4,10]
t = 19   
print(optimal(c,t))  # 2
print(findMinNewValReqToAdded(c,t))  # 2
