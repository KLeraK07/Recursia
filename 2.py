class List:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swap_pairs(head):
    if head is None or head.next is None:
        return head

    next_node = head.next
    head.next = swap_pairs(next_node.next)
    next_node.next = head
    
    return next_node

head = List(5, List(2, List(7, List(1))))
new_head = swap_pairs(head)

while new_head is not None:
    print(new_head.val, end=" -> ")
    new_head = new_head.next


