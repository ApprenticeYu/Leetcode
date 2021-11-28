class Solution:
    def reverse_tree(self,root):
        if not root:
            return root
        left = reverse_tree(root.left)
        right = reverse_tree(root.right)
        root.left,root.right = right,left
        return root
