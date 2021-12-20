class Solution:
    def guess_number(self,target,guess):
        bully = 0
        t = [0] * 10
        g = [0] * 10
        for ta,gu in zip(target,guess):
            if ta == gu:
                bully += 1
            else:
                t[int(ta)] += 1
                g[int(gu)] += 1
        cows = sum(min(ta,gu) for ta,gu in zip(t,g))
        return f'{bully}A{cows}B'
