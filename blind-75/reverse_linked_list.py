from typing import Optional, List

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  
  def printList(self, head: Optional[ListNode]) -> None:
    curr = head
    while curr:
      print(curr.val)
      curr = curr.next
  
  
  def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    
    if head is None or head.next is None:
      return head
    
    stack = list()
    curr = head
    
    while curr:
      stack.append(curr)
      curr = curr.next
    
    # print(stack)
    revHead = ListNode()
    curr = revHead
    while len(stack) > 0:
      tempNode = stack.pop()
      # print(tempNode.val)
      curr.next = tempNode
      curr = curr.next
    
    curr.next = None
    
    self.printList(revHead.next)
    return revHead.next
    


obj = Solution()
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
obj.reverseList(head)

def extractListValues(head: Optional[ListNode]) -> List[int]:
  res = []
  curr = head
  while curr:
    res.append(curr.val)
    curr = curr.next
  
  return res

def test_000():
  head = ListNode(1)
  assert(extractListValues(obj.reverseList(head))) == [1]

def test_001():
  head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
  assert(extractListValues(obj.reverseList(head))) == [5,4,3,2,1]

def test_002():
  head = ListNode(2, ListNode(1))
  assert(extractListValues(obj.reverseList(head))) == [1, 2]

def test_003():
  head = None
  assert(extractListValues(obj.reverseList(head))) == []