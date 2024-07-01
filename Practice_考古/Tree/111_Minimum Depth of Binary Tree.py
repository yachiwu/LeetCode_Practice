class TreeNode:
    def __init__(self,val=0,left = None,right=None):
        self.val = val
        self.left = left
        self.right = right

def minDepth(root:TreeNode)-> int:   
    # root is None
    if not root:
        return 0
    # left right tree all exist
    if root.left and root.right:
        return min(minDepth(root.left),minDepth(root.right))+1
    # left or right tree not exist
    if root.left or root.right:
        return max(minDepth(root.left),minDepth(root.right)) +1
    # left right tree all not exist
    return 1
from typing import List

def createTreeNode(nums:List[int])->TreeNode:
    if not nums:
        return None
    nodes = [None if val is None else TreeNode(val )for val in nums]
    for i, node in enumerate(nodes):
        left_index = 2*i+1
        right_index = 2*i+2
        if left_index < len(nodes) and nodes[left_index] is not None:
            node.left = nodes[left_index]
        
        if right_index < len(nodes) and nodes[right_index] is not None:
            node.right = nodes[right_index]
    return nodes[0]

# from collections import deque
# def printTreeNode(root:TreeNode)->List[int]:
#     if not root:
#         return []
#     result = []
#     queue = deque([root])
#     while queue:
#         node = queue.popleft()
#         result.append(node.val)
#         if node.left:
#             queue.append(node.left)
#         if node.right:
#             queue.append(node.right) 
#     return result        

    
root = [3,None,20,None,None,15,7]
rootNode = createTreeNode(root)
ans = minDepth(rootNode)
print(ans)
