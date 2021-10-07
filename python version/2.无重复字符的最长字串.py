class solution:
    def thelongestsubstring(self,s):
        hash = set()
        n = len(s)
        rk = -1
        ans = 0
        for i in range(n):
            if i != 0:
                hash.remove(s[i - 1])
            while((rk + 1 < n) and (s[rk + 1] not in hash)):
                hash.add(s[rk + 1])
                rk += 1
            ans = max(ans,rk - i + 1)
        return ans

result = solution()
print(result.thelongestsubstring("bbbbb"))
