class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        res = []
        n = len(nums)
        # 1st step to find total XOR 
        XOR = 0
        for i in range(n):
            XOR ^= nums[i]

        # Step 2: To find flip, find mask having all bits set to 1
        #mask = (2**maximumBit) - 1
        mask  = (1 << maximumBit ) - 1 # same as above but is faster

        for i in range(n):
            k = XOR ^ mask # this will give flipped value of XOR i.e is my best k
            res.append(k)

            # remove the last element from nums --> XOR it with the same value so it will be removes and is fast
            # e.g : [0,1,1,3] XOR with 3 will give -> [0,1,1]
            XOR ^= nums[n-i-1]
        return res

# T.C = O(n)
# S.C = O(1)