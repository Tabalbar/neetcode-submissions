# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        index = 0
        nodes_visited = {}

        prev = ListNode()
        curr = head.next

        while curr:
            if curr.next and curr.next.val in nodes_visited:
                return True
            nodes_visited[curr.val] = index
            curr = curr.next
            index+= 1
        return False