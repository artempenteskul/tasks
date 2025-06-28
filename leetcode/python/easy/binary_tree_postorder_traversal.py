# task number - 145
# topics - stack, tree, depth-first-search, binary tree


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def postorder_traversal(root: Node = None) -> list[int]:
    if not root:
        return []

    result = []

    stack = [root]

    while stack:
        node = stack.pop()
        result.append(node.val)

        if node.left:
            stack.append(node.left)

        if node.right:
            stack.append(node.right)

    return result[::-1]


if __name__ == '__main__':
    input_node = Node(val=1, right=Node(val=2, left=Node(val=3)))
    print(f'Postorder traversal - {postorder_traversal(input_node)}')  # [3, 2, 1]

    input_node = Node(val=1)
    print(f'Postorder traversal - {postorder_traversal(input_node)}')  # [1]

    input_node = None
    print(f'Postorder traversal - {postorder_traversal(input_node)}')  # []
