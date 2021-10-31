class Solution:
    def array_to_BST(self,nums):
        def loop(left,right):
            if left > right:
                return None
            mid = (left + right + randint(0,1)) // 2
            root = TreeNode(nums[mid])
            root.left = loop(left,mid - 1)
            root.right = loop(mid + 1,right)
            return root
        return loop(0,len(nums) - 1))
