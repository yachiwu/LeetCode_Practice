# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional

def createTreeNode(nums:List[int])->TreeNode:
    if not nums:
        return None
    nodes = [None if val is None else TreeNode(val) for val in nums]
    for i,node in enumerate(nodes):
        left_index = 2*i+1
        right_index = 2*i+2
        if left_index < len(nodes):
            node.left = nodes[left_index]
        if right_index < len(nodes):    
            node.right = nodes[right_index]
    return nodes[0]


def isBalanced(root: Optional[TreeNode]) -> bool:
    def check(root:TreeNode)-> int:
        if root == None:
            return 0
        node_value = root.val
        l = check(root.left)
        r= check(root.right)
        # If the left or right subtrees are already unbalanced, 
        # or if the difference between them is greater than 1, then return -1 to represent unbalanced.
        if l == -1 or r ==-1 or abs(l-r)>1 :
            return -1
        return 1+ max(l,r)
    return check(root) != -1 
    
input_array = [3,9,20,None,None,15,7]
input_tree = createTreeNode(input_array )
ans = isBalanced(input_tree)
print(ans)