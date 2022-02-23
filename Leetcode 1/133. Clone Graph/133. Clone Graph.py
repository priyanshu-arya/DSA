# https://leetcode.com/problems/clone-graph/

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        hashmap = {}

        def dfs(node):
            if node in hashmap:
                return hashmap[node]

            newCopy = Node(node.val)
            hashmap[node] = newCopy

            for neighbor in node.neighbors:
                newCopy.neighbors.append(dfs(neighbor))

            return newCopy

        if node:
            return dfs(node)
        return None