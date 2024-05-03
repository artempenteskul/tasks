# task number - 206


class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node


def reverse_linked_list(head: ListNode or None) -> ListNode or None:
    if not head:
        return None

    prev = None
    current = head

    while current:
        current_next = current.next
        current.next = prev
        prev = current
        current = current_next

    head = prev

    return head


if __name__ == '__main__':
    input_head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    output_head = reverse_linked_list(input_head)

    output_list = []
    while output_head:
        output_list.append(output_head.val)
        output_head = output_head.next

    print(f'Output linked list - {output_list}')  # [5, 4, 3, 2, 1]

    ###

    input_head = ListNode(1, ListNode(2))
    output_head = reverse_linked_list(input_head)

    output_list = []
    while output_head:
        output_list.append(output_head.val)
        output_head = output_head.next

    print(f'Output linked list - {output_list}')  # [2, 1]

    ###

    input_head = None
    output_head = reverse_linked_list(input_head)

    output_list = []
    while output_head:
        output_list.append(output_head.val)
        output_head = output_head.next

    print(f'Output linked list - {output_list}')  # []
