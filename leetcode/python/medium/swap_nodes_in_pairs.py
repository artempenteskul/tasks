# task number - 24
# topics - linked list, recursion


class ListNode:
    def __init__(self, val: int = 0, next_node: 'ListNode' = None) -> None:
        self.val = val
        self.next = next_node


def collect_linked_list_values(head: ListNode or None) -> list[int]:
    res = []

    if not head:
        return res

    while head:
        res.append(head.val)
        head = head.next

    return res


def swap_pairs(head: ListNode or None = None) -> ListNode or None:
    if not head or not head.next:
        return head

    dummy = ListNode()
    dummy.next = head
    prev = dummy

    while head and head.next:
        first = head
        second = head.next

        first.next = second.next
        second.next = first
        prev.next = second

        head = first.next
        prev = first

    return dummy.next


if __name__ == '__main__':
    input_head = ListNode(1, next_node=ListNode(2, next_node=ListNode(3, next_node=ListNode(4))))
    print(f'Output linked list - {collect_linked_list_values(swap_pairs(input_head))}')  # [2, 1, 4, 3]

    input_head = None
    print(f'Output linked list - {collect_linked_list_values(swap_pairs(input_head))}')  # []

    input_head = ListNode(1)
    print(f'Output linked list - {collect_linked_list_values(swap_pairs(input_head))}')  # [1]

    input_head = ListNode(1, next_node=ListNode(2, next_node=ListNode(3)))
    print(f'Output linked list - {collect_linked_list_values(swap_pairs(input_head))}')  # [2, 1, 3]
