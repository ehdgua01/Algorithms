class Solution:
    def decodeString(self, s: str) -> str:
        decoded, count, stack = "", 0, []
        for char in s:
            if char.isdigit():
                count = count * 10 + int(char)
            elif char == "[":
                stack.append(decoded)
                stack.append(count)
                decoded, count = "", 0
            elif char == "]":
                num = stack.pop()
                last = stack.pop()
                decoded = last + decoded * num
            else:
                decoded += char
        return decoded
