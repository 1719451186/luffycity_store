# 也可以不写成类，只要保证基本的功能即可
class Stack:
    def __init__(self):
        self.stack = []
    def push(self, item) :
        self.stack.append(item)

    def pop(self) :
        return self.stack.pop()

    def gettop(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None
    def isEmpty(self) :
        return len(self.stack) == 0


def brace_match(s):
    stack = Stack()
    for char in s:
        if char in {"(", "[", "{"}:
            stack.push(char)
        else:
            if stack.isEmpty():
                return False
            elif char == ")" and stack.gettop() == "(":
                stack.pop()
            elif char == "}" and stack.gettop() == "{":
                stack.pop()
            elif char == "]" and stack.gettop() == "[":
                stack.pop()
            elif char == ")" and stack.gettop() != "(":
                stack.push(char)
            elif char == "]" and stack.gettop() != "[":
                stack.push(char)
            elif char == "}" and stack.gettop() != "{":
                stack.push(char)
    if stack.isEmpty():
        return True
    else:
        return False

s1 = "[]{{(}}))))"
print(brace_match(s1))

