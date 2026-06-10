# def try_or(fn, default):
#     try:
#         return fn()
#     except:
#         return default

# class ListNode:
#     def __init__(self, val: int, next = None) -> None:
#             self.val = val
#             self.next = next

# head = ListNode(4, ListNode(5, ListNode(6)))

# print(head.next.val)
# print(try_or(head.next.next.next.next, None))

class Parent:
    speaks = ['English']
    class_variable = 10

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.speaks.append('German')

    @classmethod
    def class_method(cls):
        print(f'Calling class method {cls}')


parent = Parent()
parent.speaks.append('French')
print(Parent.speaks)
print(parent.class_variable)

child = Child()
print(child.speaks)
child.class_method()