# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        # find the middle node
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # reverse from the middle node
        def reverse_List(head):
            new_list = None
            current = head
            while current:
                next_node = current.next
                current.next = new_list 
                new_list = current
                current = next_node
            return new_list    
        rev_list = reverse_List(slow)
        # check palindrome
        left , right = head, rev_list
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next  # 此處修正
        return True  