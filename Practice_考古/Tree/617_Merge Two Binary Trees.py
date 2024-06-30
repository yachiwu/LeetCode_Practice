class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

def mergeTree(root1:TreeNode,root2:TreeNode)->TreeNode:
    if not root1 and not root2:
        return None
    v1 = root1.val if root1 else 0
    v2 = root2.val if root2 else 0
    mergeRoot  = TreeNode(v1+v2)
    mergeRoot.left = mergeTree(root1.left if root1 else None, root2.left if root2 else None )
    mergeRoot.right = mergeTree(root1.right if root1 else None, root2.right if root2 else None )

    return mergeRoot

root1  = TreeNode(1)
root1.left = TreeNode(3)
root1.right = TreeNode(2)
root1.left.left = TreeNode(5)

root2 = TreeNode(2)
root2.left = TreeNode(1)
root2.right = TreeNode(3)
root2.left.right = TreeNode(4)
root2.right.right = TreeNode(7)

ans = mergeTree(root1,root2)
print(ans.val, ans.left.val,ans.right.val)
