import collections

class Solution:
    def combine_sum2(self,candidates,target):
        def dfs(position,rest):
            nonlocal sequence
            if rest == 0:
                ans.append(sequence[:])
                return
            if position == len(candidates) or rest < freq[position][0]:
                return
            dfs(position + 1,rest)
            most = min(rest // freq[position][0],freq[position][1])
            for i in range(1,most + 1):
                sequence.append(freq[position][0])
                dfs(position + 1,rest - i * freq[position][0])
            sequence = sequence[:-most]

        ans = list()
        sequence = list()
        freq = sorted(collections.Counter(candidates).items())
        dfs(0,target)
        return ans
