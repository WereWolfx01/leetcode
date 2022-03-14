# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverse(self, head):
        prev = None
        curr = head
        
        while curr != None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            
        return prev 
    
    def merge(self, l1, l2):
        while l2 != None:
            next = l1.next
            l1.next = l2
            l1 = l2
            l2 = next
        
    
    
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        
        if head == None or head.next == None:
            return
        
        l1 = head
        slow = head
        fast = head
        prev = None
        
        while fast != None and fast.next != None:
            prev = slow               #tail of first half
            slow = slow.next          #head of second half
            fast = fast.next.next     #tail of second half
        
        prev.next = None
        
        l2 =  self.reverse(slow)                  #head of reversed second half
        
        
        self.merge(l1, l2)
        
    
