# task number - 1669


class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node


def merge_in_between(list_1: ListNode, a: int, b: int, list_2: ListNode) -> ListNode:
    list_2_head = list_2

    list_2_last = list_2
    while list_2_last.next:
        list_2_last = list_2_last.next

    list_1_split_head, list_1_split_tail = None, None

    counter = 0
    list_1_iter = list_1

    while not (list_1_split_head and list_1_split_tail):
        if counter + 1 == a:
            list_1_split_head = list_1_iter
        elif counter - 1 == b:
            list_1_split_tail = list_1_iter

        list_1_iter = list_1_iter.next
        counter += 1

    list_1_split_head.next = list_2_head
    list_2_last.next = list_1_split_tail

    return list_1


if __name__ == '__main__':
    list1_input = ListNode(10, ListNode(1, ListNode(13, ListNode(6, ListNode(9, ListNode(5))))))
    list2_input = ListNode(101, ListNode(102, ListNode(103)))

    a_input = 3
    b_input = 4

    result_list = merge_in_between(list1_input, a_input, b_input, list2_input)

    #
    result = []

    while result_list:
        result.append(result_list.val)
        result_list = result_list.next

    print(f'Result of merge in between fot the input: {result}')  # [10, 1, 13, 101, 102, 103, 5]
