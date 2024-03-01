'''
Given a string s of length n, find the alphabetically largest subsequence of length i possible for each i where (1 ≤ i ≤ n).
Note: A subsequence is a string left after deleting some or no characters from the original string without changing their order. For example, "ac" is a subsequence of "abcd" but "ca" is not.

Example
Consider s = "hrw". The alphabetically largest subsequence

of length 1 is "w".
of length 2 is "rw".
of length 3 is "hrw".
The answer is ["w", "rw", "hrw"], without quotes.
'''

# TC : O(n * nlogn)
# For length k (not for all i to n)
import heapq
def max_seq(word, k):
    n = len(word)
    if k == n:
        return word

    # Create list of pairs. Integer pairs with its index to keep the order. 
    check = [-1 * ord(x) for x in word]
    pairs = list(zip(check, range(n)))
    
    max_heap = pairs[:((n - k) + 1)]    # possible-scope of first idx is [0, (n-k) + 1]
    heapq.heapify(max_heap)

    cur_idx = -1
    ret = list()
    for i in range(n - k + 1, n + 1):   # +1 adding last number
        last_selected_idx = cur_idx
        while cur_idx <= last_selected_idx:
            cur_num, cur_idx = heapq.heappop(max_heap)

        ret.append(str(chr(-1 * cur_num)))
        if i < n:
            heapq.heappush(max_heap, pairs[i])

    return "".join(ret)

# s = "hrw"
s = "fhudccnidfjok"
for i in range(1, len(s)+1):
    print(max_seq(s, i))    # hrw    
