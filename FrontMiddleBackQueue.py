class FrontMiddleBackQueue:

    def __init__(self):
        self.bPtr = 0
        self.q = []

    def pushFront(self, val: int) -> None:
        self.q.insert(0, val)
        self.bPtr += 1

    def pushMiddle(self, val: int) -> None:
        self.q.insert(self.bPtr//2, val)
        self.bPtr += 1
        
    def pushBack(self, val: int) -> None:
        self.q.append(val)
        self.bPtr += 1
        
    def popFront(self) -> int:
        if len(self.q) > 0:
            temp = self.q[0]
            if self.bPtr != 1:
                del self.q[0]
            else:
                self.q = []
            self.bPtr -= 1
            return temp
        return -1

    def popMiddle(self) -> int:
        if self.bPtr != 0:
            temp = self.q[(self.bPtr-1)//2]
            if self.bPtr != 1:
                del self.q[(self.bPtr-1)//2]
            else:
                self.q = []
            self.bPtr -= 1
            return temp
        return -1

    def popBack(self) -> int:
        if self.bPtr != 0:
            temp = self.q[-1]
            if self.bPtr != 1:
                del self.q[-1]
            else:
                self.q = []
            self.bPtr -= 1
            return temp
        return -1
