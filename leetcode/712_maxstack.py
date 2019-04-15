# not working
class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.max_value = 0

    def push(self, x: int) -> None:
        self.max_value = max(self.max_value, x)
        self.stack.append([x, self.max_value])

    def pop(self) -> int:
        pop_temp = self.stack[-1][0]
        self.stack = self.stack[:-1]
        return pop_temp

    def top(self) -> int:
        return self.stack[-1][0]

    def peekMax(self) -> int:
        return self.max_value

    def popMax(self) -> int:
        stack_temp = []
        while self.stack[-1][0] != self.max_value:
            stack_temp.append(self.stack.pop())
        self.stack.pop()  # remove max
        for value in reversed(stack_temp):
            self.stack.append(value)
        return self.max_value

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()