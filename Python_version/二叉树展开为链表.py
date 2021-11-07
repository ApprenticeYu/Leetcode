class Solution:
    def tree_to_list(self,root):
        cur = root
        while cur:
            if cur.left:
                predecessor = next = cur.left
                while predecessor.right:
                    predecessor = predecessor.right
                predecessor = cur.right
                cur.left = None
                cur.right = next
            cur = cur.right
