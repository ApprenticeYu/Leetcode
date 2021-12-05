class Solution:
    def all_path(self,root):
        def dfs(root,path):
            if root:
                path += str(root.val)
                if not root.left and not root.right:
                    paths.append(path)
                else:
                    path += '->'
                    dfs(root.left,path)
                    dfs(root.right,path)
        paths = []
        dfs(root,'')
        return paths
