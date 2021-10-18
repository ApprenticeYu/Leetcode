class Solution:
    def merged(self,nums):
        nums.sort(key = lambda x:x[0])
        merge = []
        for num in nums:
            if not merge or merge[-1][1] < num[0]:
                merge.append(num)
            else:
                merge[-1][1] = max(merge[-1][1],num[1])
        return merge

result = Solution()
print(result.merged([[1,4],[4,5]]))
