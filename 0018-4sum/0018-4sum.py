class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res = []
        nums.sort()
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]: #to avoid duplicates
                continue
            for j in range(i+1, n):
                if j != i+1 and nums[j] == nums[j-1]: # to avoid duplicates
                    continue
                k = j+1 # after j
                l = n - 1 # last element
                # 2 sum 2 approach
                while k < l:
                    cur_sum = nums[i] + nums[j] + nums[k] + nums[l]
                    if cur_sum == target:
                        res.append([nums[i] , nums[j] , nums[k] , nums[l]])
                        k += 1
                        l -= 1
                        while k < l and nums[k] == nums[k-1]: #to avoid duplicates
                            k +=1 
                        while k < l and nums[l] == nums[l+1]: #to avoid duplicates
                            l -=1 
                    elif cur_sum < target:
                        k += 1
                    else:
                        l -= 1
        return res
                    
