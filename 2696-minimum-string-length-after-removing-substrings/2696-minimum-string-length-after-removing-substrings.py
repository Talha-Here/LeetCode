class Solution:
    def minLength(self, s: str) -> int:
        stack = []
      
        for c in s:
            stack.append(c)
            # loop till len is 2 or more and either last 2 elements must be AB or CD to be popped
            while len(stack) >= 2 and (
                (stack[-2] == "A" and stack[-1] == "B")
                or (stack[-2] == "C" and stack[-1] == "D")
            ):
                stack.pop()
                stack.pop()

        return len(stack)
# T.C = O(n)
# S.C = O(n)