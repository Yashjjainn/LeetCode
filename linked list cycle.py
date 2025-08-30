#leetcode problem : linked list cycle
#https://leetcode.com/problems/linked-list-cycle/?envType=study-plan-v2&envId=top-interview-150

from typing import Optional
class ListNode:
    def __init__(self,value):
        self.val = value
        self.next = None


def create_linkedlist(values,pos):
    #create a linked list with cycle at index pos if pos!= -1
    node = [ListNode(v) for v in values]
    for i in range(len(node) - 1):
        node[i].next = node[i+1]
    if pos != -1:
        node[-1].next = node[pos]
    return node[0] if node else None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:    #using floyd's cycle detection algorithm
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

#  for class solution time: O(n)     space: O(1)

#test case 
if __name__ == "__main__":
    S = Solution()
    s = [1,3,5,2,6]
    head = create_linkedlist(s,2) #has cycle
    print(S.hasCycle(head))
    
    head1 = create_linkedlist([1,3,4,5],-1)
    print(S.hasCycle(head1))

