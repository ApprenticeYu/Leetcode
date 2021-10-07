class Solution:
    convert_table = [
    (1000,"M"),
    (900,"CM"),
    (500,"D"),
    (400,"CD"),
    (100,"C"),
    (90,"XC"),
    (50,"L"),
    (40,"XL"),
    (10,"X"),
    (9,"IX"),
    (5,"V"),
    (4,"IV"),
    (1,"I")
    ]

    def num_convert(self,number):
        ans = list()
        for num,sign in Solution.convert_table:
            while number >= num:
                number -= num
                ans.append(sign)
            if number == 0:
                break
        return "".join(ans)

result = Solution()
print(result.num_convert(1994))
