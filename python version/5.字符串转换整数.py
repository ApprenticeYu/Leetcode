MIN_NUM,MAX_NUM = -2 ** 31,2 ** 31 - 1
class atoi:
    def __init__(self):
        self.state = "start"
        self.sign = 1
        self.ans = 0
        self.table = {
        "start":["start","signed","numbers","end"],
        "signed":["end","end","numbers","end"],
        "numbers":["end","end","numbers","end"],
        "end":["end","end","end","end"]
        }
    def get_num(self,x):
        if x.isspace():
            return 0
        elif x == "+" or x == "-":
            return 1
        elif x.isdigit():
            return 2
        else:
            return 3
    def get_solution(self,x):
        self.state = self.table[self.state][self.get_num(x)]
        if self.state == "numbers":
            self.ans = self.ans * 10 + int(x)
            self.ans = min(self.ans,MAX_NUM) if self.sign == 1 else min(self.ans,-MIN_NUM)
        elif self.state == "signed":
            self.sign = 1 if x == "+" else -1

class Solution:
    def result(self,S):
        atoi_result = atoi()
        for s in S:
            atoi_result.get_solution(s)
        return atoi_result.sign * atoi_result.ans

result_1 = Solution()
print(result_1.result("-91283472332"))
