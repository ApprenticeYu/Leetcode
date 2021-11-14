class Solution:
    def compare_version(self,version1,version2):
        n = len(version1)
        m = len(version2)
        i,j = 0,0
        while i < n or j < m:
            x = 0
            while i < n and version1[i] != '.':
                x = x * 10 + ord(version1[i]) - ord('0')
                i += 1
            i += 1
            y = 0
            while j < m and version2[j] != '.':
                y = y * 10 + ord(version2[j]) - ord('0')
                j += 1
            j += 1
            if x != y:
                return 1 if x > y else -1
        return 0
