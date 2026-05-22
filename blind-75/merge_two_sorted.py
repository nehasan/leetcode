from typing import List, Optional

class ListNode:
  def __init__(self, val = 0, next = None):
    self.val = val
    self.next = next
  

class Solution:
  '''
  def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    
    def printList(list: Optional[ListNode]) -> None:
      curr = list
      while curr:
        print(curr.val)
        curr = curr.next
    
    def insertVal(list: Optional[ListNode], val: int) -> Optional[ListNode]:
      if list.val == 101:
        list.val = val
        return list
      else:
        list.next = ListNode(val)
        return list.next
    
    if list1 is None and list2 is None:
      return None
    
    curr1 = list1
    curr2 = list2
    res = ListNode(101)
    resCurr = res
    
    while curr1 or curr2:
      if curr1 and curr2:
        num1 = curr1.val
        num2 = curr2.val
        
        if num1 == num2:
          resCurr = insertVal(resCurr, num1)
          resCurr = insertVal(resCurr, num2)
          curr1 = curr1.next
          curr2 = curr2.next
        elif num1 < num2:
          resCurr = insertVal(resCurr, num1)
          curr1 = curr1.next
        else:
          resCurr = insertVal(resCurr, num2)
          curr2 = curr2.next
      elif curr1:
        resCurr = insertVal(resCurr, curr1.val)
        curr1 = curr1.next
      elif curr2:
        resCurr = insertVal(resCurr, curr2.val)
        curr2 = curr2.next
    
    printList(res)
    return res
  '''
  
  def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    
    def printList(list: Optional[ListNode]) -> None:
      curr = list
      while curr:
        print(curr.val)
        curr = curr.next
    
    if list1 is None and list2 is None:
      return None
    elif list1 is None:
      return list2
    elif list2 is None:
      return list1
    
    d = ListNode()
    curr = d
    
    '''
    while list1 or list2:
      if list1 and list2:
        if list1.val < list2.val:
          curr.next = list1
          curr = list1
          list1 = list1.next
        else:
          curr.next = list2
          curr = list2
          list2 = list2.next
      elif list1:
        curr.next = list1
        curr = list1
        list1 = list1.next
      elif list2:
        curr.next = list2
        curr = list2
        list2 = list2.next
    '''
    while list1 and list2:
      if list1.val < list2.val:
        curr.next = list1
        curr = list1
        list1 = list1.next
      else:
        curr.next = list2
        curr = list2
        list2 = list2.next
    
    curr.next = list1 if list1 else list2
    
    printList(d.next)
    return d.next
    
    
    
obj = Solution()

list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))

list1 = None
list2 = None

list1 = None
list2 = ListNode(0)

list1 = ListNode(1)
list2 = ListNode(1, ListNode(2, ListNode(3)))

list1 = ListNode(5)
list2 = ListNode(1, ListNode(2, ListNode(4)))

list1 = ListNode(5, ListNode(6, ListNode(7)))
list2 = ListNode(1)

obj.mergeTwoLists(list1, list2)
        