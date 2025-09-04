class Solution:
    def defangIPaddr(self, address: str) -> str:
        res = ""
        for elem in address:
            if elem == ".":
                res += "[.]"
            else:
                res += elem
        return res
        