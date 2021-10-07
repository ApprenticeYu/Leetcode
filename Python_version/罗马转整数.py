class Solution:
    dict_table = {
    "I":1,
    "V":5,
    "X":10,
    "L":50,
    "C":100,
    "D":500,
    "M":1000
    }
    def string_number(self,S):
        ans = 0
        n = len(S)
        for i,s in enumerate(S):
            if i < n - 1 and Solution.dict_table[s] < Solution.dict_table[S[i + 1]]:
                ans -= Solution.dict_table[s]
            else:
                ans += Solution.dict_table[s]
        return ans
result = Solution()
print(result.string_number("MCMXCIV"))
