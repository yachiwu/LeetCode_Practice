from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def createTreeNode(nums: List[Optional[int]]) -> TreeNode:
    if not nums:
        return None
    
    # 創建根節點
    root = TreeNode(nums[0])
    current = root
    queue = [current]
    
    index = 1
    while queue and index < len(nums):
        node = queue.pop(0)
        
        # 處理左子節點
        if index < len(nums) and nums[index] is not None:
            node.left = TreeNode(nums[index])
            queue.append(node.left)
        index += 1
        
        # 處理右子節點
        if index < len(nums) and nums[index] is not None:
            node.right = TreeNode(nums[index])
            queue.append(node.right)
        index += 1
    
    return root

def printTreeNode(root: TreeNode) -> List[int]:
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # 去除结果列表末尾的多余 None
    while result and result[-1] is None:
        result.pop()
    return result

# 測試範例
nums = [2, None, 3, None, 4, None, 5, None, 6]
tree = createTreeNode(nums)
print(printTreeNode(tree))

nums2 = [3, 9, 20, None, None, 15, 7]
tree2 = createTreeNode(nums2)
print(printTreeNode(tree2))