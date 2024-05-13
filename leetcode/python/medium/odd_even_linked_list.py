# task number - 328


class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node


def odd_even_list(head: ListNode or None) -> ListNode or None:
    if not head or not head.next:
        return head

    odd = head
    even = head.next
    even_head = head.next

    while even and even.next:
        odd.next = odd.next.next
        even.next = even.next.next

        odd = odd.next
        even = even.next

    odd.next = even_head

    return head


if __name__ == '__main__':
    input_head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    output_head = odd_even_list(input_head)

    output_list = []
    while output_head:
        output_list.append(output_head.val)
        output_head = output_head.next

    print(f'Output head list - {output_list}')  # [1, 3, 5, 2, 4]

    ###

    input_head = ListNode(2, ListNode(1, ListNode(3, ListNode(5, ListNode(6, ListNode(4, ListNode(7)))))))
    output_head = odd_even_list(input_head)

    output_list = []
    while output_head:
        output_list.append(output_head.val)
        output_head = output_head.next

    print(f'Output head list - {output_list}')  # [2, 3, 6, 7, 1, 5, 4]

    ###

    input_head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    output_head = odd_even_list(input_head)

    output_list = []
    while output_head:
        output_list.append(output_head.val)
        output_head = output_head.next

    print(f'Output head list - {output_list}')  # [1, 3, 2, 4]
