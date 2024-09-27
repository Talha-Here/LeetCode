class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        r = 0
        #for r in range(len(nums)): # we can use for also then we dont need to r+=1 at l3
        while r < len(nums):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l] #swapping
                l += 1 #move forward
            r += 1#if 0 then we dont need to do anything as we are swapping non-zero elements
        return nums

        