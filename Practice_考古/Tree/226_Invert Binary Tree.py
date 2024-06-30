class TreeNode:
    def __init__(self, val =0 ,left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root:TreeNode)->TreeNode:
    if not root:
       return None
    temp = root.left
    root.left = root.right
    root.right = temp
    invertTree(root.left)
    invertTree(root.right)

    return root

from typing import List
def createTreeNode(nums:List[int])->TreeNode:
    if not nums:
        return None
    nodes = [None if val is None else TreeNode(val) for val in nums]
    for i, node in enumerate(nodes):
        left_index = 2*i+1
        right_index = 2*i+2
        if left_index < len(nodes) and nodes[left_index] is not None:
            node.left = nodes[left_index]
        
        if right_index < len(nodes) and nodes[right_index] is not None:
            node.right = nodes[right_index]
    return nodes[0]

from collections import deque
def printTreeNode(root:TreeNode)->List:
    if not root:
        return []
    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result
            


root = [4,2,7,1,3,6,9]
rootNode = createTreeNode(root)
ans = invertTree(rootNode)
print(printTreeNode(ans))

