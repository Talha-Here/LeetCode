class Solution:
    def minimumSteps(self, s: str) -> int:
        total_steps = black_moves = 0

        for num in s:
            if num == "0": # white so black ball will not move
                total_steps += black_moves
            else:
                black_moves += 1 #black ball so will move
        return total_steps
# tC: O(n)
# SC: O(1)        