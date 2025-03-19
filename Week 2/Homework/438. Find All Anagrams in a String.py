from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        
        pcount = Counter(p)
        scount = Counter(s[:len(p)])
        result = []

        if scount == pcount:
            result.append(0)

        for i in range(len(p), len(s)):
            scount[s[i]] += 1 # to add new character to window
            scount[s[i-len(p)]] -= 1 # to remove old characters

            if scount[s[i-len(p)]] == 0:
                del scount[s[i-len(p)]]

            if scount == pcount:
                result.append(i-len(p) + 1)
        
        return result