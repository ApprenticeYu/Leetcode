import collections

class Solution:
    def arrays_mul(self,num1,num2):
        if len(num1) > len(num2):
            return self.arrays_mul(num2,num1)
        m = collections.Counter()
        for num in num1:
            m[num] += 1
        intersections = list()
        for num in num2:
            if (count := m.get(num,0)) > 0:
                intersections.append(num)
                m[num] -= 1
                if m[num] == 0:
                    m.pop(num)
        return intersections
