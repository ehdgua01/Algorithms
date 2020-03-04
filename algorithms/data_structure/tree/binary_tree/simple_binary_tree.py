class Node(object):
    def __init__(self, value: str) -> None:
        self.left = None
        self.right = None
        self.value = value


def pre_order_tree(node: Node) -> str:
    result = node.value

    if node.left:
        result += pre_order_tree(node.left)

    if node.right:
        result += pre_order_tree(node.right)

    return result


def in_order_tree(node: Node) -> str:
    result = node.value

    if node.left:
        result = in_order_tree(node.left) + result

    if node.right:
        result += in_order_tree(node.right)

    return result


def post_order_tree(node: Node) -> str:
    result = ''

    if node.left:
        result += post_order_tree(node.left)

    if node.right:
        result += post_order_tree(node.right)

    result += node.value
    return result


def destroy_tree(node: Node) -> None:
    if node.left:
        destroy_tree(node.left)

    if node.right:
        destroy_tree(node.right)

    node.left = None
    node.right = None
