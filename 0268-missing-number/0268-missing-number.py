class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # sum of orginial length - sum of given length of nums
        n = len(nums) # O(1) , Space: O(1)
        formulaSum = (n * (n+1)) // 2 # GAUSS formula --- O(1) Space: O(1)
        originalSum = sum(nums) # O(n) Space: O(1)
        return formulaSum - originalSum # O(1) , Space: O(1)


        # 1 + 1 + n + 1
        # 3 + n
        # Time: O(n) , Space: O(1)
#-----------------Solution 2-------------------------------------
        # n = len(nums) # O(1) , Space: 
        # nums.sort() # Time: O(nlogn) (NO EXTRA SPACE)
        # for ind in range(n): # O(n) (ind is defined only once so no EXTRA SPACE)
        #     if ind != nums[ind]: # O(n)
        #         return ind 
        # return n
        
# 1 + nlogn + n + n
# 1 + nlogn + 2n
# nlogn + n
# Time: nlogn , Space : O(1)

     


