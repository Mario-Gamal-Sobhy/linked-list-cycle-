###########################Floyd's Cycle Detection (the "tortoise and hare" algorithm)####################
########################### can be solved using the SET() but the space will be O(n)  ####################  

class Solution(object):
    def hasCycle(self, head):

        dummy = ListNode()
        dummy.next = head
        slow = fast = dummy


        while fast and fast.next :
            fast = fast.next.next
            slow = slow.next 

            if slow is fast:
                return True 

        return False              
