# Function to remove an item from queue.

# It changes front and size

def DeQueue(self):

	if self.isEmpty():		print("Queue is empty")

		return

	print("% s dequeued from queue" % str(self.Q[self.front]))

	self.front = (self.front + 1) % (self.capacity)

	self.size = self.size - 1

# This code is contributed by Susobhan Akhuli
