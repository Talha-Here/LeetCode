class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # first a sorted list as res in first pass, if the value is greater then we get in else and check if we can add 
        res = [nums[0]]
        max_len = 0
        for i in nums[1:]:
            if i > res[-1]:
                res.append(i)
                max_len += 1
            else: # using binary search on the res list that we have created 
                left, right = 0, len(res) - 1
                while left < right:
                    mid = (left + right)//2
                    if res[mid] < i:
                        left = mid + 1
                    else:
                        right = mid
                res[left] = i
        return max_len +1



            