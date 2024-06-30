class TreeNode:
    def __init__(self,val = 0, left = None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
from typing import List

def averageOfLevel(root:TreeNode)->List[float]:
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        level_sum = 0
        level_count = 0
        for _ in range(len(queue)):
            node = queue.popleft()
            level_sum += node.val
            level_count+=1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level_sum / level_count) 
    return result            

# Example usage:
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

ans = averageOfLevel(root)
print(ans)