#leetcode problem : Merge two sorted list
#https://leetcode.com/problems/merge-two-sorted-lists/description/?envType=study-plan-v2&envId=top-interview-150

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linkedlist(values):
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for i in values[1:]:
        curr.next = ListNode(i)
        curr = curr.next
    return head

#method to print the merged list after recieving the head for it from solution class
def print_linkelist(head):
    vals = []
    while head:
        vals.append(str(head.val))
        head = head.next
    print(" -> ".join(vals))

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        #deciding on head for merged list
        if list1.val < list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next
        
        current = head  #saving the head of merged list and using a copy to add more nodes
        
        while list1 and list2:     #merging the two lists
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # attaching the remaining nodes left from any list
        current.next = list1 if list1 else list2
        return head

# for class solution time: O(m+n)    space: O(n)

#test case 
if __name__ == "__main__":
    S = Solution()
    s = [4,1,2,5,7,6,5,8,9,4,3]
    t = [1,5,3,6,4,7,8,5,1,2]
    list1 = create_linkedlist(s)
    list2 = create_linkedlist(t)
    print_linkelist(S.mergeTwoLists(list1,list2))