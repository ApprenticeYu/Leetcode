class Solution:
    def __init__(self):
        self.visit = {}

    def clone_graph(self,node):
        if not node:
            return node
        if node in self.visit:
            return self.visit[node]
        clone_node = Node(node.value,[])
        self.visit[node] = clone_node
        if node.neighbors:
            clone_node.neighbors = [self.clone_graph(Node) for Node in node.neighbors]
        return clone_node
