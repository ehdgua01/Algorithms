import re
import operator


__OPERATOR = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.floordiv,
}
OPERATOR_PRIORITY = {
    "*": 3,
    "/": 3,
    "+": 2,
    "-": 2,
    "(": 1,
}


def is_number(value: str) -> bool:
    result = re.fullmatch(r"^(-)?[0-9]+(\.[0-9]+)?", value)
    return False if result is None else True


class TreeNode(object):
    def __init__(self, value) -> None:
        self.left = None
        self.right = None
        self.value = value


class StackNode(object):
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class Stack(object):
    def __init__(self):
        self.top = None
        self.size = 0

    def pop(self):
        if self.is_empty:
            raise Exception("Stack is empty")
        data = self.top.data
        self.top = self.top.next
        self.size -= 1
        return data

    def push(self, new: StackNode) -> None:
        if not isinstance(new, StackNode):
            raise TypeError("Not node type")
        if self.is_empty:
            self.top = new
        else:
            new.next = self.top
            self.top = new
        self.size += 1

    def peek(self):
        return None if self.is_empty else self.top.data

    def get_size(self) -> int:
        return self.size

    @property
    def is_empty(self) -> bool:
        return self.top is None


def postfix_to_tree(expr: list) -> TreeNode:
    __stack = Stack()

    for token in expr:
        if is_number(token):
            __stack.push(StackNode(TreeNode(round(float(token), 2))))
        elif token in __OPERATOR:
            p1 = __stack.pop()
            p2 = __stack.pop()
            node = TreeNode(token)
            node.left = p2
            node.right = p1
            __stack.push(StackNode(node))
    return __stack.pop()


def calculate_expression_tree(node: TreeNode):
    if (node.left is None) and (node.right is None):
        return node.value

    p1 = calculate_expression_tree(node.left)
    p2 = calculate_expression_tree(node.right)

    if node.value in __OPERATOR:
        return __OPERATOR[node.value](p1, p2)
    return node
