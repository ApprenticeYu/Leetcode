class Solution:
    def is_BST(self,root):
        def loop(root,lower = float('-inf'),upper = float('inf')):
            if not root:
                return True
            if root.val <= lower or root.val >= upper:
                return False
            if not loop(root.left,lower,root.val):
                return False
            if not loop(root.right,root.val,upper):
                return False
            return True
        return loop(root)
