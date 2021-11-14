class Solution:
    def postorder(self,root):
        def loop(root):
            if not root:
                return
            loop(root.left)
            loop(root.right)
            res.append(root.value)
        res = list()
        loop(root)
        return ret
