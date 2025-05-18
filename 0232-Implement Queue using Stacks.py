class MyQueue:

    def __init__(self):
        from collections import deque
        self.stack1 = deque()

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        length = len(self.stack1) -1
        stack2 = deque()
        while length:
            length -= 1
            stack2.append(self.stack1.pop())
        popped = self.stack1.pop()
        while stack2:
            self.stack1.append(stack2.pop())
        return popped

    def peek(self) -> int:
        length = len(self.stack1)
        stack2 = deque()
        while length:
            length -= 1
            popped = self.stack1.pop()
            stack2.append(popped)
        while stack2:
            self.stack1.append(stack2.pop())
        return popped

    def empty(self) -> bool:
        if len(self.stack1) == 0:
            return True
        return False
    

####################### ANOTHER METHOD O(1)
class MyQueue:

    def __init__(self):
        from collections import deque
        self.in_stack = deque()
        self.out_stack = deque()

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        self.transfer()
        return self.out_stack.pop()

    def peek(self) -> int:
        self.transfer()
        return self.out_stack[-1]

    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack
    
    def transfer(self) -> None:
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())