# task number - 2


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    root = ListNode()
    cur = root

    head_one = False

    while l1 or l2:

        l1_val = 0 if l1 is None else l1.val
        l2_val = 0 if l2 is None else l2.val

        local_num = l1_val + l2_val + 1 if head_one else l1_val + l2_val

        head_one = True if local_num >= 10 else False

        cur.next = ListNode(local_num % 10)
        cur = cur.next

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    if head_one:
        cur.next = ListNode(1)

    return root.next


if __name__ == '__main__':
    list1 = ListNode(2, ListNode(4, ListNode(3, ListNode(3))))
    list2 = ListNode(5, ListNode(6, ListNode(4)))

    res1 = add_two_numbers(list1, list2)  # ListNode(7, ListNode(0, ListNode(8, ListNode(3))))
    while res1:
        print(res1.val)
        res1 = res1.next

    print('===')

    list1 = ListNode(8)
    list2 = ListNode(7)

    res2 = add_two_numbers(list1, list2)  # ListNode(5, ListNode(1))
    while res2:
        print(res2.val)
        res2 = res2.next
