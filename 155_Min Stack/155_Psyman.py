import sys
import bisect
class MinStack(object):
	def __init__(self):
		"""
		initialize your data structure here.
		"""
		self.InternalStack = []
		self.SortedList = []

	def push(self, x):
		"""
		:type x: int
		:rtype: void
		"""
		self.InternalStack.append(x)
		bisect.insort( self.SortedList, x )
		
	def pop(self):
		"""
		:rtype: void
		"""
		Removed = self.InternalStack.pop()
		self.SortedList.remove(Removed)

	def top(self):
		"""
		:rtype: int
		"""
		return self.InternalStack[-1]

	def getMin(self):
		"""
		:rtype: int
		"""
		return self.SortedList[0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()