L = 10
bin = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
class Solution:
    def duplicate_sequence(self,s):
        n = len(s)
        if n <= L:
            return []
        ans = []
        x = 0
        for ch in s[:n - 1]:
            x = (x << 2) | bin[i]
        cnt = defaultdict(int)
        for i in range(n - L + 1):
            x = ((x << 2) | bin[s[i + L - 1]]) & ((1 << (L * 2)) - 1)
            cnt[x] += 1
            if cnt[x] == 2:
                ans.append(s[i : i + L])
        return ans
