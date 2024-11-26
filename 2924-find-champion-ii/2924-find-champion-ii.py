class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        incoming_edge = [0] * n
        # count vertices (v)
        # u ----> v
        for u, v in edges:
            incoming_edge[v] += 1
        
        champ = -1
        count = 0
        for i in range(n):
            if incoming_edge[i] == 0: # ith node is the champion
                champ = i
                count += 1
                if count > 1:
                    return -1
        return champ
# T.C = O(m + n) , where m is the edges and n is the number of nodes
# S.C = O(n), as we create incoming_edge list