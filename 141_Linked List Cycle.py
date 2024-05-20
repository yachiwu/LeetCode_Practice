from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def createLinkedList(nums: List[int]) -> ListNode:
    dummy = ListNode()
    current = dummy
    nodes = []
    for num in nums:
        current.next = ListNode(num)
        current = current.next
        nodes.append(current)
    return dummy.next, nodes

def printLinkedList(head: Optional[ListNode]) -> List[int]:
    ansList = []
    current = head
    visited = set()
    while current and current not in visited:
        ansList.append(current.val)
        visited.add(current)
        current = current.next
    return ansList

def hasCycle(head: Optional[ListNode]) -> bool:
    slow , fast = head, head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if slow == fast:
            return True
            
    return False

# # Create the linked list
# head, nodes = createLinkedList([3, 2, 0, -4])
# # link node -4 to node 2
# nodes[-1].next = nodes[1]

# # check if this is Linked List Cycle
# ans = hasCycle(head)
# print(ans)
# head, nodes = createLinkedList([3, 2, 0, -4])

# head,nodes  = createLinkedList([1, 2, 3, 4])
# ans = hasCycle(head)
# print(ans)

