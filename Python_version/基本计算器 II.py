class Solution:
    def calculate(self,s):
        n = len(s)
        stack = []
        pre = '+'
        num = 0
        for i in range(n):
            if s[i] != '' and s[i].isdigit():
                num = num * 10 + ord(s[i]) - ord('0')
            if i == n - 1 or s[i] in '+-*/':
                if pre == '+':
                    stack.append(num)
                else if pre == '-':
                    stack.append(-num)
                else if pre == '*':
                    stack.append(stack.pop() * num)
                else:
                    stack.append(stack.pop() / num)
                pre = s[i]
                num = 0
        return sum(stack)
