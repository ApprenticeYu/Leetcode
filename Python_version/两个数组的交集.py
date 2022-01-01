class Solution:
    def arrays_mul(self,num1,num2):
        num1.sort()
        num2.sort()
        l1 = len(num1)
        l2 = len(num2)
        result = list()
        index1,index2 = 0,0
        while index1 < l1 and index2 < l2:
            if num1[index1] == num2[index2]:
                if not result or result[-1] != num1[index1]:
                    result.append(num1[index1])
                index1 += 1
                index2 += 1
            else if num1[index1] < num2[index2]:
                index1 += 1
            else:
                index2 += 1
        return result
