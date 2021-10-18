class Solution:
    def string_multiply(self,s1,s2):
        if s1 == "0" or s2 == "0":
            return "0"
        m,n = len(s1),len(s2)
        ans = [0] * (m + n)
        for i in range(m - 1,-1,-1):
            num1 = int(s1[i])
            for j in range(n - 1,-1,-1):
                num2 = num1 * int(s2[j])
                ans[i + j + 1] += num2
        for k in range(m + n - 1,0,-1):
            ans[k - 1] += ans[k] // 10
            ans[k] %= 10
        index = 1 if ans[0] == 0 else 0
        result = "".join(str(s) for s in ans[index:])
        return result

answer = Solution()
print(answer.string_multiply("123","456"))
