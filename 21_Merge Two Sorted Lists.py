# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

from typing import List,Optional

class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

def createLinkedList(nums: List[int]) -> ListNode:
    dummy = ListNode()
    current = dummy
    for num in nums:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

def printLinkedList(list: Optional[ListNode]) -> List[int]:
    ansList = []
    while list:
        ansList.append(list.val)
        list = list.next
    return ansList


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode] : 
    # Create a dummy node to start the merged list
    dummy = ListNode()
    # Pointer to traverse the merged list
    current = dummy
    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next

        else:
            current.next = list2
            list2 = list2.next
        current = current.next   
    # Append the remaining nodes of the non-empty list to the merged list
    current.next = list1 if list1 else list2
    return dummy.next


list1 = createLinkedList([1, 2, 4])
list2 = createLinkedList([1, 3, 4])
ans = mergeTwoLists(list1,list2)
print(printLinkedList(ans))

