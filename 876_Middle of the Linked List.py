from typing import List, Optional
class ListNode:
    def __init__(self, val=0,next = None):
        self.val = val
        self.next = next

def createLinkedList(nums: List[int]) -> ListNode:
    dummy = ListNode()
    current = dummy
    for num in nums:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

def printLinkedList(head: Optional[ListNode]) -> List[int]:
    ansList = []
    current = head
    while current :
        ansList.append(current.val)
        current = current.next
    return ansList

def middleNode(head: Optional[ListNode])-> Optional[ListNode]:
# 當fast 走到linked list 結束的位置時，slow會正好在中間
# 跳出while的條件為fast == None
    slow, fast = head ,head
    # while fast is not the last node yet
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next 
    return slow

input= createLinkedList([1,2,3,4,5])
ans = middleNode(input)
print(printLinkedList(ans))