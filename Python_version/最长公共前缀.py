class Solution:
    def thelongestcommonprefix(self,S):
        if S == "":
            return ""
        n = len(S)
        prefix = S[0]
        for i in range(1,n):
            prefix = self.find_common(prefix,S[i])
            if prefix == "":
                break
        return prefix

    def find_common(self,s1,s2):
        length = min(len(s1),len(s2))
        index = 0
        while index < length and s1[index] == s2[index]:
            index += 1
        return s1[:index]

result = Solution()
print(result.thelongestcommonprefix(["dog","racecar","car"]))
