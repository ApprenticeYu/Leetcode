class Solution:
    def convert_to_title(self,number):
        ans = list()
        while number > 0:
            number -= 1
            ans.append(chr((number % 26) + ord('A')))
            number //=  26
        return "".join(ans[::-1])
