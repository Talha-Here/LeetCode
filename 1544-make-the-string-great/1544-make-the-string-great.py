class Solution:
    def makeGood(self, s: str) -> str:

        #implementing own lower function
        def lower(c):
            # we know its a upper case if its lesser than ord(a)
            if ord(c) < ord('a'): # or we can use ord(c) > ord('z')
                delta = ord(c) - ord('A')
                lower_chr = chr(ord('a') + delta)
                return lower_chr
            # we know its already in lower case
            return c

        stack = []
        i = 0
        while i < len(s):
            if (
                stack and # stack should not be empty
                stack[-1] != s[i] and # both letters should not be same
                #stack[-1].lower() == s[i].lower() # their lower case must be same
                lower(stack[-1]) == lower(s[i]) # using our function 
            ):
                stack.pop()
            else:
                stack.append(s[i])
            i += 1
        return "".join(stack)
# T.C = O(n)
# S.C = O(n)
        