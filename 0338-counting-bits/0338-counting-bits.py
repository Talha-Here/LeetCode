class Solution:
    def countBits(self, n: int) -> List[int]:
        # =================nlogn sol
        # res = [0]
        # def bit_count(n):
        #     count = 0
        #     while n:
        #         n = n & (n-1)
        #         count += 1
        #     return count
        # for i in range(1,n+1):         
        #     res.append(bit_count(i))
        # return res

        # ========= O(n) SOL; DP 
        # step 1:any number divided by 2 will have same bits, e.g 10 has two 1s so 10//2 = 5, 5 have also two 1s
        # step 2: the odd have 1 more 1s then there prev, e.g: 2 -> 10(one 1), 3 -> 11 (two 1s)
        res = [0]
        for i in range(1,n+1):
            res.append(res[i//2] + i%2)
        return res 
        