class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        a_streak = b_streak = c_streak = 0
        res = []
        total_str_count = a+b+c

        for i in range(total_str_count):
            # condition for a
            if (a >= b and a >= c and a_streak != 2) or (a > 0 and (b_streak == 2 or c_streak == 2)):
                res.append("a")
                a -= 1
                a_streak += 1
                b_streak = c_streak = 0
            # condition for b    
            elif (b >= a and b >= c and b_streak != 2) or (b > 0 and (a_streak == 2 or c_streak == 2)):
                res.append("b")
                b -= 1
                b_streak += 1
                a_streak = c_streak = 0
            # condtion for c
            elif (c >= a and c >= b and c_streak != 2) or (c > 0 and (a_streak == 2 or b_streak == 2)):
                res.append("c")
                c -= 1
                c_streak += 1
                a_streak = b_streak = 0

        return "".join(res)
# TC: O(a+b+c)
# SC: O(N), if we are considering res string builder list. We need it anyways, else SC is O(1)