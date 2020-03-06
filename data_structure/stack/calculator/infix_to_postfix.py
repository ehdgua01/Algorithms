import re

from ..stack import Stack, Node

OPERATOR = {
    '*': 3,
    '/': 3,
    '+': 2,
    '-': 2,
    '(': 1,
}


def is_number(value: str) -> bool:
    result = re.fullmatch(r'^(-)?[0-9]+(\.[0-9]+)?', value)
    return False if result is None else True


def infix_to_postfix(expression: str) -> list:
    postfix = []
    operator_stack = Stack()

    for token in expression.split():
        if is_number(token):
            # 피연산자일 경우에 식에 추가
            postfix.append(token)
        elif token == '(':
            # 괄호가 열리는 부분은 일단 추가
            operator_stack.push(Node(token))
        elif token == ')':
            # 괄호가 열리는 요소가 나올 때까지 연산자를 식에 추가
            top_op = operator_stack.pop()
            while top_op != '(':
                postfix.append(top_op)
                top_op = operator_stack.pop()
        else:
            if token not in OPERATOR:
                raise Exception('허용되지 않은 연산자입니다.')
            while (
                    not operator_stack.is_empty
                    and OPERATOR[operator_stack.peek()] >= OPERATOR[token]
            ):
                # 현재 연산자보다 우선순위가 높은 연산자들을 식에 추가
                postfix.append(operator_stack.pop())
            # 현재 추가되는 연산자가 가장 우선순위가 높은 연산자
            operator_stack.push(Node(token))

    while not operator_stack.is_empty:
        # 우선순위가 높은 순서대로 식에 추가
        postfix.append(operator_stack.pop())

    return postfix
