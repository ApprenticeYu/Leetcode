import collections

class Solution:
    def class(self,nums,sequence):
        edges = collections.defaultdict(list)
        visited = [0] * nums
        valid = True
        result = list()

        for s in sequence:
            edges[s[1]].append(s[0])

        def dfs(u):
            nonlocal valid
            visited[u] = 1
            for v in edges[u]:
                if visited[v] == 0:
                    dfs(v)
                    if not valid:
                        return
                elif visited[v] == 1:
                    valid = False
                    return
            visited[u] = 2
            result.append(u)

        for i in range(nums):
            if visited[i] == 0 and valid:
                dfs(i)
        return valid
