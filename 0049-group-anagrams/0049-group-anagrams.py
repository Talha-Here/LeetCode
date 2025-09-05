class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0]*26

            for c in s:
                count[ord(c) - ord("a")] += 1
            # print(count)
            # print(res)
            res[tuple(count)].append(s)
            # print("after tuple",res)
        return list(res.values())

# Time & Space: O(m*n) , where n is len of list and m is len of strings in list