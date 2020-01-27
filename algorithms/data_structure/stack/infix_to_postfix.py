import re

from stack import Stack, Node

OPERATOR = {
    '*': 3,
    '/': 3,
    '+': 2,
    '-': 2,
    '(': 1,
}


def is_number(token: str):
    result = re.fullmatch(r'([0-9]|\.)+', token)
    return False if result is None else True


def infix_to_postfix(expression: str):
    postfix = []
    operator_stack = Stack()

    for token in expression.split():
        if is_number(token):
            postfix.append(token)
        elif token == '(':
            operator_stack.push(Node(token))
        elif token == ')':
            top_op = operator_stack.pop()
            while top_op != '(':
                postfix.append(top_op)
                top_op = operator_stack.pop()
        else:
            while (
                    not operator_stack.is_empty
                    and OPERATOR[operator_stack.peek()] >= OPERATOR[token]
            ):
                postfix.append(operator_stack.pop())
            operator_stack.push(Node(token))

    while not operator_stack.is_empty:
        postfix.append(operator_stack.pop())

    return postfix


print(infix_to_postfix('1 + ( 2 * 123 * 2323 + 999 ) * 123 + 1'))
