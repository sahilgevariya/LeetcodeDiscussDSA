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
    
# Greedy + Brute-Force
def findMinNewValReqToAdded(vals, target):
    vals.sort()
    min_additions = 0
    num_to_added = []
    
    for num in range(1, target + 1):
        if not isPossible(vals, num):
            bisect.insort(vals, num)
            num_to_added.append(num)
            min_additions += 1
            
    # print(num_to_added)
    return min_additions

# Pattern finding (binary nums)
def optimal(vals, t):
    nums_l = sorted(vals)
    
    s = 1
    min_addition = 0
    while s <= t:
        if not isPossible(nums_l, s):
            bisect.insort(nums_l, s)
            min_addition += 1
        s *= 2
        
    return min_addition
    
c = [1,4,10]
t = 19   
print(optimal(c,t))  # 2
print(findMinNewValReqToAdded(c,t))  # 2
