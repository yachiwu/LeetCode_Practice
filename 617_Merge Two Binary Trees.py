class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List,Optional
from collections import deque
def createTreeNode(nums: List[int]) -> TreeNode:
    if not nums:
        return None
    nodes = [None if val is None else TreeNode(val) for val in nums]
    # [1,3,2,5]
    #     1
    #    / \
    #   3   2
    #  /
    # 5

    for i, node in enumerate(nodes):
        left_index = 2*i+1
        right_index = 2*i+2
        if left_index < len(nodes):
            node.left = nodes[left_index]
        if right_index < len(nodes):    
            node.right = nodes[right_index]
    return nodes[0]    


def mergeTrees(root1: TreeNode, root2: TreeNode) -> TreeNode:
    if not root1 and not root2:
        return None
    v1 = root1.val if root1 else 0
    v2 = root2.val if root2 else 0
    root = TreeNode(v1+v2)
    root.left = mergeTrees(root1.left if root1 else None, root2.left if root2 else None)
    root.right = mergeTrees(root1.right if root1 else None, root2.right if root2 else None)
    
    return root

def print_level_order_traversal(root:TreeNode)->List:
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

root1 = createTreeNode([1,3,2,5])
root2 = createTreeNode([2,1,3,None,4,None,7])
ans = mergeTrees(root1,root2)
ans_list = print_level_order_traversal(ans)
print(ans_list)

# [1,3,2,5]
#     1
#    / \
#   3   2
#  /
# 5
# [2,1,3,None,4,None,7]
#        2
#     /    \
#    1      3
#   / \    / \
# None 4  None 7



 
