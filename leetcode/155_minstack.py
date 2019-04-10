class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        # only append to min_stack if empty or x smaller than values in min_stack
        if len(self.min_stack) == 0 or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self) -> None:
        pop_number = self.stack.pop(-1)
        # if min_value is pop, pop min_stack
        if pop_number == self.min_stack[-1]:
            self.min_stack.pop(-1)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
