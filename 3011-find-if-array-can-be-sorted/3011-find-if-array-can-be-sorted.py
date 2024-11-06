class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        # appraoch 1 is using bubble sort just additional check is of set bit - O(n^2)

        # Approach 2 - segemets of same bits and sorting them, then cheking max of curr segment < min of next segment ==> O(n)

        def bin_bits(n):
            return bin(n).count("1") # built in func; we can use our own, solve leetcode easy problem for it

        cur_min, cur_max = nums[0] , nums[0]
        prev_max = float("-inf")

        for n in nums:
            if bin_bits(n) == bin_bits(cur_min):
                cur_min = min(cur_min, n)
                cur_max = max(cur_max, n)
            else:
                if prev_max > cur_min: # the max of prev segment should be less than the curr_min
                    return False
                prev_max = cur_max
                cur_min, cur_max = n, n
        if prev_max > cur_min: # the max of prev segment should be less than the curr_min
                    return False
        return True

# T.C = O(n)
# T.C = O(1)