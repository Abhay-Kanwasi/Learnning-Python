# Function to add an item to the queue.

# It changes rear and size

def EnQueue(self, item):

	if self.isFull():		print("Full")

		return

	self.rear = (self.rear + 1) % (self.capacity)

	self.Q[self.rear] = item

	self.size = self.size + 1

	print("% s enqueued to queue" % str(item))

