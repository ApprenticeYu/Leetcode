import collections

class Solution:
    def level_order(self,root):
        ans = list()
        if not root:
            return ans
        d = collections.deque([root])
        while d:
            n = len(d)
            num = []
            for _ in range(n):
                node = d.popleft()
                num.append(node.val)
                if node.left:
                    d.append(node.left)
                if node.right:
                    d.append(node.right)
            d.apend(num)
        return d[::-1]
