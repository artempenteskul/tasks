# task number - 1290

class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node


def get_decimal_value(head: ListNode) -> int:
    str_decimal_value = ''

    while head:
        str_decimal_value += str(head.val)
        head = head.next

    return int(str_decimal_value, 2)


if __name__ == '__main__':
    input_1 = ListNode(1, ListNode(0, ListNode(1)))
    print(f'Decimal value for input [1, 0, 1] - {get_decimal_value(input_1)}')  # 5

    print()

    input_2 = ListNode(0)
    print(f'Decimal value for input [0] - {get_decimal_value(input_2)}')  # 0
