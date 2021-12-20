class Solution:
    def H_(self,citations):
        n = len(citations)
        total = 0
        cits = [0] * (n + 1)
        for citation in citations:
            if citation >= n:
                cits[n] += 1
            else:
                cits[citation] += 1
        for i in range(n,-1,-1):
            total += cits[i]
            if total >= i:
                return i
        return 0
