class Solution:
    def same_tree(self,root1,root2):
        if not root1 and not root2:
            return True
        elif not root1 or not root2:
            return False
        elif root1.val != root2.val:
            return False
        else:
            return self.same_tree(root1.left,root2.left) and self.same_tree(root1.right,root2.right)
