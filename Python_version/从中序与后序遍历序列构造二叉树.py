class Solution:
    def build_tree(self,inorder,postorder):
        def loop(in_begin,in_end):
            if in_begin > in_end:
                return None
            root_val = postorder.pop()
            in_root_idx = idx[root_val]
            root = TreeNode(root_val)
            root.left = loop(in_begin,in_root_idx - 1)
            root.right = loop(in_root_idx + 1,in_end)
            return root
        idx = {number:i for i,number in enumerate(inorder)}
        return loop(0,len(inorder) - 1)
