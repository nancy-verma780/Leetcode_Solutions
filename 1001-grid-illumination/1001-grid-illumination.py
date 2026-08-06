class Solution(object):
    def gridIllumination(self, n, lamps, queries):
        """
        :type n: int
        :type lamps: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        from collections import Counter

     
        rows, cols = Counter(), Counter()
        diag1, diag2 = Counter(), Counter()
        
   
        lamp_set = set()
        
        for r, c in lamps:
            if (r, c) not in lamp_set:
                lamp_set.add((r, c))
                rows[r] += 1
                cols[c] += 1
                diag1[r - c] += 1
                diag2[r + c] += 1
        
        ans = []
        for r, c in queries:
           
            if rows[r] > 0 or cols[c] > 0 or diag1[r - c] > 0 or diag2[r + c] > 0:
                ans.append(1)
            else:
                ans.append(0)
       
            for i in range(r - 1, r + 2):
                for j in range(c - 1, c + 2):
                    if (i, j) in lamp_set:
                     
                        lamp_set.remove((i, j))
                        rows[i] -= 1
                        cols[j] -= 1
                        diag1[i - j] -= 1
                        diag2[i + j] -= 1
                        
        return ans

        