# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        tail = dummy
        
        while head and head.next:
            left = head
            right = head.next
            head = right.next 
            
            tail.next = right  
            right.next = left 
            left.next = head  
            
            tail = left   
        
        return dummy.next
