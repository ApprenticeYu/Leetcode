class Solution:
    def root_leaf_sum(self,root):
        def dfs(root,pre_num):
            if not root:
                return 0
            sum = pre_num * 10 + root.value
            if not root.left and not root.right:
                return sum
            else:
                return dfs(root.left,sum) + dfs(root.right,sum)
        return dfs(root,0)
