class NestedListIterator:
    def __init__(self, nestedList):
        self.arr = []
        self.ptr = 0
        def helper(list_):
            for i in list_:
                if type(i) != type(int):
                    helper(i)
                else:
                    self.arr.append(i)
        helper(nestedList)
        self.length = len(self.arr)
    
    def next(self) -> int:
        if self.ptr < self.length:
            tmp = self.ptr
            self.ptr += 1
            return self.arr[tmp]
        return -1
    
    def hasNext(self) -> bool:
         if self.ptr < self.length:
            return True
         return False
