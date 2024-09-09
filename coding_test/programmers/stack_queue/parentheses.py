def solution(s):
    opened = []
    for char in s:
        if char == "(":
            opened.append(char)
        elif not opened:
            return False
        else:
            opened.pop()
    return not bool(opened)
