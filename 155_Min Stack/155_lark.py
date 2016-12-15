class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minList = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if len(self.minList)==0:
            self.minList.append(x)
        elif self.minList[len(self.minList)-1] < x:
            self.minList.append(x)
        else:
            for i in range(0,len(self.minList)):
                if self.minList[i] < x:
                    continue
                else:
                    self.minList = self.minList[:i] + [x] + self.minList[i:]
                    break

    def pop(self):
        """
        :rtype: void
        """
        self.minList.remove(self.stack[len(self.stack)-1])
        self.stack = self.stack[:len(self.stack)-1]

    def top(self):
        """
        :rtype: int
        """
        return self.stack[len(self.stack)-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minList[0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
