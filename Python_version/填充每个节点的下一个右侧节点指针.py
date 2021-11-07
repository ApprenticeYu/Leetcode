class Solution:
    def full_ptr(self,root):
        if not root:
            return root
        cur = root
        while cur.left:
            node = cur
            while node:
                node.left.next = node.right
                if node.next:
                    node.right.next = node.next.left
                node = node.next
            cur = cur.left
        return root
