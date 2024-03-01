'''
***** Microsoft *****
A string s, is similar to another string t, if it possible to swap two adjacent characters at most once in s to turn it into t. Given a keyword string named key,
find how many substrings of text are similar to key.

Example 1 :
key : "moon"
text : "monomon"

Explanation :
* Consider the first four characters in text. i.e "mono". Swap the last two characters to match the keyword "moon".
* The last four characters in the text are "omon". Swap the first two characters to macth the keyword.

Thus,there are 2 substrings of "monomon" that are similar to "moon". Note, that no other substring is similar to the given key.

Example 2 :
key : "aaa"
text : "aaaa"

Output : 2. There are 2 substrings of "aaaa" that are similar to "aaa" are:
aaaa
aaaa

Example 3 :
key : "xxy"
text : "zxxyxyx"

Output : 3.

Constraints :
key and text will consist solely of lowercase english letters.
1 <= | key | <= | text | <= 50, Where | s | denotes the length of a string s.
'''

key = "moon"
text = "monomon"

def getSubstrings(key, text):
    
    def doCheck(i):
        chance = 1
        j = 0
        while j != len(key):
            if key[j] != text[i]:
                if chance and j+1 < len(key) and i+1 < len(text) and (text[i] == key[j+1] and key[j] == text[i+1]):
                    chance = 0
                    j += 1
                    i += 1
                else:
                    return False
            i += 1
            j += 1
            
        return True
    
    cnt = 0
    for i in range(len(text) - len(key) + 1):
        if doCheck(i):
            print(text[i: i+len(key)])
            cnt += 1
                
    return cnt
            
print(getSubstrings(key, text))
print(getSubstrings("aaa", "aaaa"))
print(getSubstrings("xxy", "zxxyxyx"))
