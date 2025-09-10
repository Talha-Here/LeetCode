class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort array
        # first get i pointer 
        # check if the next val is same as no duplicates 
        # left and right where left is i+1 and right is last index
        # 2 sum II logic on left and right , if 3sum is > 0 then r--
        # if 3sum is < 0 l++
        # else 3sum == 0, append it to the res
        # lastly make sure that no duplicates so L++ and is not out of index

        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]: #empty [] if i = 0 and skipping the duplicate
                continue
            l , r = i+1 , len(nums)-1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a,nums[l],nums[r]])
                    l+=1
                    #need to check that the new l val is not same as the previous
                    while nums[l] == nums[l-1] and l<r:
                        l+=1 
        return res


# T: O(nlogn) + O(n^2) => O(n^2)
# S: O(n)

        