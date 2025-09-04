class Solution:
    def defangIPaddr(self, address: str) -> str:

        #  ---- This is O(n^2) cuz, stirngs are immutable 
        # res = ""
        # for elem in address:
        #     if elem == ".":
        #         res += "[.]" # O(n)
        #     else:
        #         res += elem # O(n)
        # return res

        # this is O(n) as ARRAY which is mutable and has O(1) inserts
        res = []
        for elem in address:
            if elem == ".":
                res.append("[.]") # O(1)
            else:
                res.append(elem) # O(1)
        return "".join(res) # O(n)
        
        