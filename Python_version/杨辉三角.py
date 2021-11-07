class Solution:
    def generate(self,rows):
        ret = list()
        for i in range(rows):
            temp = list()
            for j in range(0,i + 1):
                if j == 0 or j == 1:
                    temp.append(1)
                else:
                    temp.append(ret[i - 1][j] + temp[i - 1][j - 1])
            ret.append(temp)
        return ret
