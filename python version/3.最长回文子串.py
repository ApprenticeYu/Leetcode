class solution:
    def expand(self,s,left,right):
        n = len(s)
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1,right - 1
    def thelongeststring(self,s):
        begin,last = 0,0
        for i in range(len(s)):
            left1,right1 = self.expand(s,i,i)
            left2,right2 = self.expand(s,i,i + 1)
            if right1 - left1 > last - begin:
                begin,last = left1,right1
            if right2 - left2 > last - begin:
                begin,last = left2,right2
        return s[begin:last + 1]

result = solution()
print(result.thelongeststring("ac"))
