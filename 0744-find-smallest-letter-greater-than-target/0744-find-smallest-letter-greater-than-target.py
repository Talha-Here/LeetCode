class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        #using binary search
        left = 0
        right = len(letters) - 1
        # if the number is out of bound
        if target >= letters[-1] or target < letters[0]:
            return letters[0]
        
        while left <= right:
            # mid = left + (right-left) // 2 # using this so that it doesn't goes out of bounds (for Cpp Java)
            mid = (left + right) //2
            if letters[mid] <= target:
                left = mid + 1
            # if letters[mid] > target:
            else:
                right = mid - 1
        return letters[left]


        