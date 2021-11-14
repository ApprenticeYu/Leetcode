class Solution:
    def preorder(self,root):
        def loop(root):
            if not root:
                return
            ret.append(root.value)
            loop(root.left)
            loop(root.right)
        ret = list()
        loop(root)
        return ret
