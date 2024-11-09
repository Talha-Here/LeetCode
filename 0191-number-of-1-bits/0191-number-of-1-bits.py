class Solution:
    def hammingWeight(self, n: int) -> int:
        # ============== sol 1 --> using mod (%) and right shift by 1 ==============
        # res = 0
        # while n: # O(32)
        #     if n % 2 == 1: 
        #         res += 1
        #     # right shift
        #     n = n >> 1
        # return res
# T.C & S.C = O(1)

    # ============== sol 2 --> using n = n & (n-1) ==============
    # helps in saving time by removing zeros. e.g 10000001, in this we will skip zeros

        res = 0 
        while n:
            n = n & (n-1)
            res += 1
        return res
# T.C & S.C = O(1)