class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        consecutive_count = 0

        for num in arr:
            # odd num
            if num % 2 == 1:
                consecutive_count += 1
            # even num
            else:
                consecutive_count = 0
            if consecutive_count == 3:
                return True
        return False
# T.C = O(n) , where n is the size of arr
# S.C = O(1)