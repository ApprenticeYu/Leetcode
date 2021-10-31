class Solution:
    def is_balance(self,root):
        def loop(root):
            if not root:
                return 0
            left = loop(root.left)
            right = loop(root.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            else:
                return max(left,right) + 1
        return loop(root) >= 0
