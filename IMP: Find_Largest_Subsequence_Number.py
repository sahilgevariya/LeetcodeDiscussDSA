'''
Given a positive integer represented as a string, and an integer K, find the largest subsequence of length K that you can form from the given string.

Input: "3141592", K = 4
Output: "4592"

Input: "3141592", K = 3
Output: "592"
'''

# O(nlogn)
import heapq
def max_seq(word, k):
    n = len(word)
    if k == n:
        return word

    # Create list of pairs. Integer pairs with its index to keep the order. 
    check = [-1 * int(x) for x in word]
    pairs = list(zip(check, range(n)))
    
    max_heap = pairs[:((n - k) + 1)]    # possible-scope of first idx is [0, (n-k) + 1]
    heapq.heapify(max_heap)             ## O(n - k + 1)

    cur_idx = -1
    ret = list()
    for i in range(n - k + 1, n + 1):   # +1 adding last number
        last_selected_idx = cur_idx
        while cur_idx <= last_selected_idx:
            cur_num, cur_idx = heapq.heappop(max_heap)      ## O(log(n-k+1))

        ret.append(str(-1 * cur_num))
        if i < n:
            heapq.heappush(max_heap, pairs[i])          ## O(log(k))

    return "".join(ret)

print(max_seq("3141592", 4))    # 4592    
print(max_seq("3141592", 3))    # 592
print(max_seq("111596", 3))    # 596
