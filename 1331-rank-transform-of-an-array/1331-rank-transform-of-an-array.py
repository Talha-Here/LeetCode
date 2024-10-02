class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # sort , make sure no repeated is sorted
        # then add it to the dict/hashmap
        num_to_rank = {}
        sort_num = sorted(set(arr)) # set to remove duplicates
        rank = 1
        # hashmap created 
        for num in sort_num:
            num_to_rank[num] = rank
            rank += 1
            
        # re-arranging arr according to hashmap
        for i in range(len(arr)):
            # print(num_to_rank[arr[i]])
            arr[i] = num_to_rank[arr[i]]
        return arr 
        
# T.C: O(NlogN)
# S.C: O(N)