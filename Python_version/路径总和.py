class Solution:
    def path_sum(self,root,target):
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == target
        return self.path_sum(root.left,target - root.val) or self.path_sum(root.right,target - root.val)
