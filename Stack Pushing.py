class DinnerPlates:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.space = [[]]
        self.fP = 0
        self.bP = 0

    def push(self, val: int) -> None:
        while self.fP < len(self.space):
            if len(self.space[self.fP]) < self.capacity:
                self.space[self.fP].append(val)
                if len(self.space[self.fP]) == self.capacity:
                    self.space.append([])
                    self.fP += 1
                    if self.fP > self.bP:
                        self.bP += 1
                return None
            self.fP += 1
        self.space.append([val])
        self.bP += 1
            
            
    def pop(self) -> int:
        if len(self.space) == 0:
            return -1 
        
        while self.bP > 0:
            if len(self.space[self.bP])  > 0:
                if len(self.space[self.bP]) == 1 and self.bP != 0:
                    temp = self.space[self.bP].pop()
                    self.bP -= 1
                else:
                    temp = self.space[self.bP].pop()
                return temp
            else:
                if self.bP == self.fP and self.bP != 0: 
                    self.fP -= 1
                if self.bP != 0:
                    self.bP -= 1
        if len(self.space) > 0 and  len(self.space[self.bP]) > 0:
            return self.space[self.bP].pop()
        return -1

    def popAtStack(self, index: int) -> int:
        if len(self.space) > index and len(self.space[index]) > 0:
            if index < self.fP:
                self.fP = index
            elif index == self.fP and self.fP != 0:
                self.fP -= 1
            if index > self.bP:
                self.bP = index
            return self.space[index].pop()
        return -1


# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)
