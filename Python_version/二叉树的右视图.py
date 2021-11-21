class Solution:
    def right_view(self,root):
        right_dict = dict()
        max_depth = -1
        stack = [(root,0)]
        while stack:
            node,depth = stack.pop()
            if node is not None:
                max_depth = max(max_depth,depth)
                right_dict.setdefault(depth,node.value)
                stack.append((node.left,depth + 1))
                stack.append((node.right,depth + 1))
        return [right_dict[deep] for deep in range(max_depth + 1)]
