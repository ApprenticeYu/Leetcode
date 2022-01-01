import collections

class Solution:
    def only_character(self,words):
        f = collections.Counter(words)
        for i,ch in enumerate(words):
            if f[ch] == 1:
                return i
        return -1
