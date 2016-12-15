class MinStack(object):

	def __init__(self):
		"""
		initialize your data structure here.
		"""
		self.stack_list = []
		self.min_stack_list = []

	def push(self, x):
		"""
		:type x: int
		:rtype: void
		"""
		if not self.min_stack_list or x <= self.min_stack_list[-1]:
			self.min_stack_list.append(x)
		self.stack_list.append(x)

	def pop(self):
		"""
		:rtype: void
		"""
		if self.stack_list:
			if self.min_stack_list and self.stack_list[-1] == self.min_stack_list[-1]:
				self.min_stack_list.pop()
			self.stack_list.pop()

	def top(self):
		"""
		:rtype: int
		"""
		if self.stack_list:
			return self.stack_list[-1]


	def getMin(self):
		"""
		:rtype: int
		"""
		if self.min_stack_list:
			return self.min_stack_list[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
 
 
if __name__ == "__main__":
	res = MinStack()
	res.push(-2)
	res.push(0)
	res.push(-3)
	res.getMin()
	res.pop()
	res.top()
	res.getMin()
	
	