class Solution:
    def compute_element(self,nums):
        n = len(nums)
        ans = []
        num1,num2 = 0,0
        vote1,vote2 = 0,0
        for num in nums:
            if vote1 > 0 and num1 == num:
                vote1 += 1
            elif vote2 > 0 and num2 == num:
                vote2 += 1
            elif vote1 == 0:
                num1 = num
                vote1 += 1
            elif vote2 == 0:
                num2 = num
                vote2 += 1
            else:
                vote1 -= 1
                vote2 -= 1

        cnt1,cnt2 = 0,0
        for num in nums:
            if vote1 > 0 and num == num1:
                cnt1 += 1
            elif vote2 > 0 and num == num2:
                cnt2 += 1

        if vote1 > 0 and cnt1 > n / 3:
            ans.append(num1)
        if vote2 > 0 and cnt2 > n / 3:
            ans.append(num2)
        return ans
