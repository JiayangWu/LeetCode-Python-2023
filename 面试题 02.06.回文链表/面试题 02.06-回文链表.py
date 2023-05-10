# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
    #     reversed_head = self.reverseLinkedList(head)
    #     ph = head
    #     pr = reversed_head

    #     while ph:
    #         print(ph.val, pr.val)
    #         if ph.val != pr.val:
    #             return False
    #         ph = ph.next
    #         pr = pr.next
        
    #     return True
    
    # def reverseLinkedList(self, head: ListNode) -> ListNode:
    #     prev, cur = None, head
    #     while cur:
    #         next_node = cur.next
    #         cur.next = prev
    #         prev, cur = cur, next_node
    #     return prev

        l = []
        p = head
        while p:
            l.append(p.val)
            p = p.next
        return l == l[::-1]