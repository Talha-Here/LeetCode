class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        res = []
        # creating backtracking (recursive) function
        def backtrack(cur_str, open_bracket, close_bracket):
            #res.append(cur_str)
            if len(cur_str) == 2*n:
                res.append(cur_str)
                return
            
            #open brackets
            if open_bracket < n:
                backtrack(cur_str + "(", open_bracket + 1, close_bracket)
                
            #close brackets
            if close_bracket < open_bracket:
                backtrack(cur_str + ")", open_bracket, close_bracket + 1)

        backtrack("",0,0)
        return res

# Time: O(2^n)
# Space: O(n)
