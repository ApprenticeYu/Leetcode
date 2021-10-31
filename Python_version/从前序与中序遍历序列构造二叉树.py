class Solution:
    def create_tree(self,preorder,inorder):
        def loop(pre_begin,pre_end,in_begin,in_last):
            if pre_begin > pre_end:
                return None
            pre_root_idx = pre_begin
            in_root_idx = idx[preorder[pre_root_idx]]
            size = in_root_idx - in_begin
            root = TreeNode(preorder[pre_root_idx])
            root.left = loop(pre_begin + 1,pre_begin + size,in_begin,in_root_idx - 1)
            root.right = loop(pre_begin + size + 1,pre_end,in_root_idx + 1,in_last)
            return root
        idx = {number:i for i,number in enumerate(inorder)}
        n = len(preorder)
        return loop(0,n - 1,0,n - 1)
