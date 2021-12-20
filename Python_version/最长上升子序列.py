class Solution:
    def longest_sequence(self,nums):
        d = []
        for num in nums:
            if not d or num > d[-1]:
                d.append(num)
            else:
                left = 0
                right = len(d) - 1
                loc = right
                while left <= right:
                    mid = (left + right) / 2
                    if num <= d[mid]:
                        right = mid - 1
                        loc = mid
                    else:
                        left = mid + 1
                d[loc] = num
        return len(d)
