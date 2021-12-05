class Solution:
    def nearest_ancestor(self,root,p,q):
        node = root
        while True:
            if node.val > p.val and node.val > q.val:
                node = node.left
            elif node.val < p.val and node.val < q.val:
                node = node.right
            else:
                break
        return node
