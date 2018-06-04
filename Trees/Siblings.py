class Node:
    def __init__(self,key):
        self.data = key
        self.left = None
        self.right = None
        self.next = None

def siblings(Tree):
    res = []
    curr_depth_nodes = [Tree]
    if not Tree:
        return
    while curr_depth_nodes:
        res = curr_depth_nodes
        for i in range(len(res)-1):
            res[i].next = res[i+1]
            print(res[i].data, " -> " ,res[i+1].data)
        curr_depth_nodes = [node for curr in curr_depth_nodes for node in (curr.left, curr.right) if node]

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

siblings(root)
