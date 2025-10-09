class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i] # prefix = prefix * nums[i]
        print(nums)
        print(res)
        postfix = 1
        for i in range(n-1, -1, -1): # in reversed order
            res[i] *= postfix
            print(nums)
            print(res)
            postfix *= nums[i]
        print(nums)
        print(res)
        
        return res
