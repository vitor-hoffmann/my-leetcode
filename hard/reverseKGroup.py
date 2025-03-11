# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(start: ListNode, end: ListNode) -> ListNode:
            prev, curr = None, start
            while curr != end:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev  

        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next

        dummy = ListNode(0)
        dummy.next = head
        prev_group_end = dummy
        curr = head

        while count >= k:
            start = curr
            for _ in range(k):
                curr = curr.next
            
            new_head = reverse(start, curr)
            
            prev_group_end.next = new_head
            prev_group_end = start  
            
            count -= k  

        prev_group_end.next = curr

        return dummy.next 