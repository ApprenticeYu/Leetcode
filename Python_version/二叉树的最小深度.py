class Solution:
    def min_depth(self,root):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        depth = 10 ** 9
        if root.left:
            depth = min(min_depth(root.left),depth)
        if root.right:
            depth = min(min_depth(root.right),depth)
        return depth + 1
