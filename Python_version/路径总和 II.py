class Solution:
    def path_sum(self,root,target):
        ans = list()
        temp = list()
        def dfs(root,target):
            if not root:
                return
            temp.append(root.val)
            target -= root.val
            if not root.left and not root.right and target == 0:
                ans.append(temp[:])
            dfs(root.left,target)
            dfs(root.right,target)
            temp.pop()
        dfs(root,target)
        return ans
