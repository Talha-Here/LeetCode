class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hash_s = defaultdict(int)
        hash_t = defaultdict(int)
        count_s = count_t = 0
        for string in s:
            hash_s[string] += 1
        print(hash_s)
        for string in t:
            hash_t[string] += 1
        print(hash_t)
        new_hash = dict(set(hash_t.items()) - set(hash_s.items()))
        return ("".join(new_hash.keys()))
# T.C = O(n)
# T.S = O(n)        