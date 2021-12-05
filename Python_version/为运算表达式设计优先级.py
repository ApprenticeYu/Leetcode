class Solution:
    def design_level(self,S):
        if S.isdigit():
            return [int(S)]
        res = []
        for i,s in enumerate(S):
            if s in '+-*':
                left = self.design_level(S[:i])
                right = self.design_level(S[i + 1:])
                for l in left:
                    for r in right:
                        if s == '+':
                            res.append(l + r)
                        elif s == '-':
                            res.append(l - r)
                        else:
                            res.append(l * r)
        return res
