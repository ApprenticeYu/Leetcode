class Met:
    def __init__(self,root):
        self.root = root
        self._count_num = {}
        self._count_num_core(root)

    def kth_value(self,k):
        node = self.root
        while node:
            left = _get_count(node.left)
            if left < k - 1:
                node = node.right
                k -= left + 1
            elif left == k - 1:
                return node.val
            else:
                node = node.left

    def _get_count(self,node):
        return self._count_num_core(node) if node is not None else 0

    def _count_num_core(self,node):
        if not node:
            return 0
        self._count_num[node] = 1 + self._count_num_core(node.left) + self._count_num_core(node.right)
        return self._count_num[node]

class Solution:
    def kth_number(self,root,k):
        result = Met(root)
        return result.kth_value(k)
