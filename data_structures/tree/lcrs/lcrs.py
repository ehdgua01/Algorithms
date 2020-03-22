class Node(object):
    def __init__(self, value) -> None:
        self.child = None
        self.sibling = None
        self.value = value


def append(parent: Node, child: Node) -> None:
    if parent.child is None:
        parent.child = child
    else:
        temp = parent.child
        while temp.sibling:
            temp = temp.sibling
        temp.sibling = child


def destroy(root: Node) -> None:
    if root.sibling:
        destroy(root.sibling)

    if root.child:
        destroy(root.child)

    root.sibling = None
    root.child = None


def print_tree(node: Node) -> dict:
    result = {}

    if node.child:
        result[node.value] = print_tree(node.child)
    else:
        result[node.value] = "last"

    if node.sibling:
        result.update(print_tree(node.sibling))

    return result
