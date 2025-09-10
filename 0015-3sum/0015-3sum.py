class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() #NlogN 
        res = []
        i = 0
        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i-1]: # checking for duplicates 
                continue

            # 2 SUM on remainder list
            j = i+1
            k = len(nums)-1

            while j < k:
                total_sum = nums[i] + nums[j] + nums[k]
                if total_sum > 0:
                    k -= 1
                elif total_sum < 0:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j-1]: # checking for duplicates 
                        j += 1
        return res

# Time : NlogN + O(n^2) ==> O(n^2)
# Space: O(1) as we are sorting in place