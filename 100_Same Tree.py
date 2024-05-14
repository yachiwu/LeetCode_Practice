class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List,Optional

def createTreeNode(nums: List[int]) -> TreeNode:
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
def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode])-> bool:
    # p , q is empty tree
    if not p and not q:
        return True
    if not p or not q or p.val!=q.val:
        return False
    return (isSameTree(p.left,q.left) and isSameTree(p.right,q.right))

p = [1,2,1]
q = [1,1,2]
p_tree = createTreeNode(p)
q_tree = createTreeNode(q)

ans = isSameTree(p_tree,q_tree)
print(ans)


