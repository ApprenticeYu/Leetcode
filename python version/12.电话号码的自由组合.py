class Solution:
    def lettercombination(self,S):
        if not S:
            return list()
        table = {
        "2":"abc",
        "3":"def",
        "4":"ghi",
        "5":"jkl",
        "6":"mno",
        "7":"pqrs",
        "8":"tuv",
        "9":"wxyz"
        }

        def back(index):
            n = len(S)
            if index == n:
                anss.append("".join(ans))
            else:
                for letter in table[S[index]]:
                    ans.append(letter)
                    back(index + 1)
                    ans.pop()
        anss = list()
        ans = list()
        back(0)
        return anss

result = Solution()
print(result.lettercombination("2"))
