"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        self.visited = dict()
        return self.doClone(node, self.visited)
        
    def doClone(self, node, visited):
        if(node==None):
            return node
        if(len(node.neighbors)==0):
            return Node(node.val)
        if(not visited.get(node)):
            newNode = Node(node.val)
            visited[node]=newNode
            for i in node.neighbors:
                newNode.neighbors.append(self.doClone(i, visited))
        return visited[node]