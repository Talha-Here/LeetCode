class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        # count = []
        max_grp_size = 0
        # considering we have 32 bit 
        for bit_pos in range(32): # O(32)
            count = 0
            # finding bit_pos is set or not (means is it 1 or not)
            for num in candidates: # O(n)
                if (num & (1 << bit_pos) > 0):
                    count += 1
            max_grp_size = max(max_grp_size, count)
        return max_grp_size 
        
# T.C =  O(n * 32) => O(n)
# S.C = O(1)