import collections

class Solution:
    def letter(self,random,magazine):
        if len(random) > len(magazine):
            return False
        return not collections.Counter(random) - collections.Counter(magazine)
