class MyStack:

    def __init__(self):
        from collections import deque
        self.queue1 = deque()
        

    def push(self, x: int) -> None:
        self.queue1.append(x)

    def pop(self) -> int:
        length = len(self.queue1) - 1
        queue2 = deque()
        while length:
            length -=1
            queue2.append(self.queue1.popleft())
        popped = self.queue1.popleft()
        self.queue1 = queue2
        return popped

    def top(self) -> int:
        length = len(self.queue1)
        queue2 = deque()
        while length:
            length -=1
            popped = self.queue1.popleft()
            queue2.append(popped)
        self.queue1 = queue2
        return popped

    def empty(self) -> bool:
        if len(self.queue1) == 0:
            return True
        return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()