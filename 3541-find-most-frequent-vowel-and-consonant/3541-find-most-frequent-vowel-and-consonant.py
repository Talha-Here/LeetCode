class Solution:
    def maxFreqSum(self, s: str) -> int:
        f = collections.Counter(s)
        vow = con = 0
        for k,v in f.items():
            if k in "aeiou":
                vow = max(vow, v)
            else:
                con = max(con, v)  
        return vow+con
        
# Time: O(n)
# Space: O(1)