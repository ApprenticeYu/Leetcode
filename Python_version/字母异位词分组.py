import collections

class Solution:
    def letter(self,strings):
        mp = collections.defaultdict(list)
        for s in strings:
            key = "".join(sorted(s))
            mp[key].append(s)
        return list(mp.values())

result = Solution()
strings = ["a"]
print(result.letter(strings))
