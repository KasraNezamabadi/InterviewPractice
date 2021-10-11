class Stack:

	def __init__(self, value: int = None):
		self.stack_array: [int] = []
		if value is not None:
			self.stack_array.append(value)

	def pushTo(self, value: int):
		self.stack_array.append(value)

	def popFrom(self):
		value = self.stack_array.pop()
		return value

	def get_count(self):
		return len(self.stack_array)


class MultiStack:
	def __init__(self, limit: int):
		self.list_of_stacks: [Stack] = []
		self.limit = limit

	def pushTo(self, value: int):
		if len(self.list_of_stacks) == 0:
			self.list_of_stacks.append(Stack(value))
		else:
			if self.list_of_stacks[-1].get_count() < self.limit:
				self.list_of_stacks[-1].pushTo(value)
			else:
				self.list_of_stacks.append(Stack(value))

	def popFrom(self):
		if len(self.list_of_stacks) > 0:
			result = self.list_of_stacks[-1].popFrom()
			if self.list_of_stacks[-1].get_count() == 0:
				self.list_of_stacks.pop()
			return result
		else:
			return None

multiStack = MultiStack(limit=4)
multiStack.pushTo(1)
multiStack.pushTo(2)
multiStack.pushTo(3)
multiStack.pushTo(4)
multiStack.pushTo(5)
multiStack.pushTo(6)


print(multiStack.popFrom())
print(multiStack.popFrom())
print(multiStack.popFrom())
print(multiStack.popFrom())
print(multiStack.popFrom())
print(multiStack.popFrom())
print(multiStack.popFrom())

v = 9
