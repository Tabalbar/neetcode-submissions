# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast = head,head
        dummy = pointer1 = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        pointer2 = prev

        while pointer1.next != None and pointer2.next != None:
            tmp = pointer1.next
            pointer1.next = pointer2
            pointer1 = tmp

            tmp = pointer2.next
            pointer2.next = pointer1
            pointer2 = tmp