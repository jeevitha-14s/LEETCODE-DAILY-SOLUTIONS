class Solution:
        def cloneGraph(self, node):
            if not node:
                return None
            clones = {node: Node(node.val)}
            stack = [node]
            while stack:
                cur = stack.pop()
                for nb in cur.neighbors:
                    if nb not in clones:
                        clones[nb] = Node(nb.val)
                        stack.append(nb)
                    clones[cur].neighbors.append(clones[nb])
            return clones[node]