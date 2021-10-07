class Solution:
    def valid(self,S):
        if len(S) % 2 == 1:
            return False
        table = {
        ")":"(",
        "]":"[",
        "}":"{"
        }
        stack = list()
        for ch in S:
            if ch in table:
                if not stack or table[ch] != stack[-1]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(ch)
        return not stack

result = Solution()
print(result.valid("{[]}"))
