class Solution:
    def reverse_word(self,s):
        def is_letter(ch):
            return ch in 'aeiouAEIOU'
        n = len(s)
        s = list(s)
        left,right = 0,n - 1
        while left < right:
            while left < right and not is_letter(s[left]):
                left += 1
            while right > left and not is_letter(s[right]):
                right -= 1
            if left < right:
                s[left],s[right] = s[right],s[left]
                left += 1
                right -= 1
        return ''.join(s)

result = Solution()
print(result.reverse_word('leetcode'))
