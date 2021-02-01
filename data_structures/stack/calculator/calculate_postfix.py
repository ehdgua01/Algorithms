import operator

from ..stack import Node, Stack

__OPERATOR = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.floordiv,
}


def calculate_postfix(postfix: list):
    result_stack = Stack()

    for token in postfix:
        try:
            try:
                result_stack.push(Node(int(token)))
            except ValueError:
                # 10진수 정수가 아닌 경우
                result_stack.push(Node(float(token)))
        except ValueError:
            if token in __OPERATOR:
                p1 = result_stack.pop()
                p2 = result_stack.pop()
                result_stack.push(Node(__OPERATOR[token](p1, p2)))
            else:
                raise Exception("허용되지 않은 데이터")
    return result_stack.pop()
