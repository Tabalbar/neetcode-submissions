# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head == None:
            return []
        current_node = head
        length = 0
        while current_node.next != None:
            current_node = current_node.next
            length+=1
        length += 1
        target_index = length - n 

        if target_index <= 0:
            return head.next

        current_node = head
        i = 0
        while current_node.next != None:
            prev_node = current_node
            current_node = current_node.next
            i+=1
            if i == target_index:
                if current_node:
                    prev_node.next = current_node.next
                else:
                    prev_node.next = None
                break
        return head
        # [1->2->3->None] if n = 2
        # [2->3->None]
        # [3->None]
        # [None]
        # is none, return 0 when head is none
        # num == 1 [3->None]
        # num == 2 [2->3->None]
        # num == 3 [1->2->3->None]
        # if num == k + 1 , which is 2
        # I need to go one more up and point at 3. save my 
        # if head.next == None and n == 1:
        #     return head.next
        # def recursive_traversal(head):
        #     if head == None:
        #         return 0
        #     num = 1 + recursive_traversal(head.next)
        #     if num == n + 1:
        #         head.next = head.next.next
        #     return num
        # recursive_traversal(head)
        # if n == index:
        #     return head.next
        # return head