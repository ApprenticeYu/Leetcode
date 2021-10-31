class Solution:
    def different_tree(self,n):
        def backward(begin,end):
            if begin > end:
                return [None,]
            trees = []
            for i in range(begin,end + 1):
                left_tree = backward(begin,i - 1)
                right_tree = backward(i + 1,end)
                for l in left_tree:
                    for r in right_tree:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        trees.append(root)
            return trees
        return backward(1,n) if n else []
