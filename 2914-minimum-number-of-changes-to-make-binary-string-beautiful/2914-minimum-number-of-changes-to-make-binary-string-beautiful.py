class Solution:
    def minChanges(self, s: str) -> int:
        # 1 ptr , we will check i and i+1 element (window of size 2)
        res = 0

        for i in range(0, len(s), 2): # step of 2 cause of even length 
            if s[i] != s[i+1]:
                res += 1
        return res
# T.C = O(n)
# S.C = O(1)
        