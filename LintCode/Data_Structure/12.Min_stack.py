# Implement a stack with min() function, which will return the smallest number in the stack.
# It should support push, pop and min operation all in O(1) cost.
# Use stack[] to operate push and pop and use min[] to record the minimum in stack
# O(1) in time cost and O(1) in mem cost
class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, number):
        self.stack.append(number)
        if len(self.min_stack) == 0 or number <= self.min_stack[-1]:
            self.min_stack.append(number)

    def pop(self):
        top = self.stack[-1]
        self.stack.pop()
        if top == self.min_stack[-1]:
            self.min_stack.pop()
        return top

    def min(self):
        return self.min_stack[-1]

if __name__ == '__main__':
    s = MinStack()
    print(s.push(1))
    print(s.pop())
    print(s.push(2))
    print(s.push(3))
    print(s.min())
    print(s.push(1))
    print(s.min())