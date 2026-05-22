from typing import Optional

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
  
  
class Solution:
  def hasCycle(self, head: Optional[ListNode]) -> bool:
    
    curr = head
    
    if curr is None:
      return False
    
    if curr and curr.next is None:
      return False
      
    if curr and curr.next == curr:
      return True
    
    if curr and curr.next and curr.next.next == curr:
      return True
    
    fast = curr
    slow = curr
    
    while slow and fast:
      slow = slow.next
      fast = fast.next.next if fast.next else None
      if slow == fast:
        return True
    
    return False
    

obj = Solution()
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

def test__000():
  head = None
  assert(obj.hasCycle(head)) == False

def test__001():
  head = ListNode()
  assert(obj.hasCycle(head)) == False

def test__002():
  head = ListNode()
  head.next = node1
  node1.next = node2
  assert(obj.hasCycle(head)) == False

def test__003():
  head = ListNode()
  head.next = node1
  node1.next = node2
  node2.next = node1
  assert(obj.hasCycle(head)) == True

def test__004():
  head = ListNode()
  head.next = node1
  node1.next = node2
  node2.next = node1
  assert(obj.hasCycle(head)) == True