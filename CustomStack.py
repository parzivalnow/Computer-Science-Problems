class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.capacity = maxSize
        self.size = 0

    def push(self, x: int) -> None:
        if self.size < self.capacity:
            (self.stack).insert(0, x)
            self.size += 1

    def pop(self) -> int:
        if self.size > 0:
            temp = self.stack[0]
            if len(self.stack) > 1:
                del self.stack[0]
            else:
                self.stack = []
            self.size -= 1
            return temp
        return -1

    def increment(self, k: int, val: int) -> None:
        if self.size > 0:
            count = 0
            for i in range(len(self.stack)-1,-1,-1):
                if count < k:
                    count += 1
                    self.stack[i] += val
                else:
                    break
