class List:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swap_pairs(head):
    if head is None or head.next is None:
        return head
    
    # Запам'ятовуємо наступний вузол
    next_node = head.next
    
    # Обмін вузлів місцями
    head.next = swap_pairs(next_node.next)
    next_node.next = head
    
    return next_node

# Створюємо початковий зв'язаний список: 5 -> 2 -> 7 -> 1
head = List(5, List(2, List(7, List(1))))

# Викликаємо функцію swap_pairs
new_head = swap_pairs(head)

# Виводимо результат
while new_head is not None:
    print(new_head.val, end=" -> ")
    new_head = new_head.next

# Результат: 2 -> 5 -> 1 -> 7
