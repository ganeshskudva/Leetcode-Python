class MyCircularDeque:

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        :type k: int
        """
        # Track the current number of elements in the deque
        self._size = 0
        # Pointers to the front and rear of the deque, both start at 0
        self._front, self._rear = 0, 0
        # Set the maximum capacity of the deque
        self._capacity = k
        # Initialize the deque with -1 values to represent empty slots
        self._data = [-1] * k

    def insertFront(self, value):
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        # If deque is full, insertion fails
        if self.isFull():
            return False
        # If deque is empty, directly assign the value at the front pointer
        if self.isEmpty():
            self._data[self._front] = value
        else:
            # Move front pointer one step back (circularly) and assign the value
            self._front = (self._front - 1) % self._capacity
            self._data[self._front] = value
        # Increment the size of the deque after successful insertion
        self._size += 1
        return True

    def insertLast(self, value):
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        # If deque is full, insertion fails
        if self.isFull():
            return False
        # If deque is empty, directly assign the value at the rear pointer
        if self.isEmpty():
            self._data[self._rear] = value
        else:
            # Move rear pointer one step forward (circularly) and assign the value
            self._rear = (self._rear + 1) % self._capacity
            self._data[self._rear] = value
        # Increment the size of the deque after successful insertion
        self._size += 1
        return True

    def deleteFront(self):
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        # If deque is empty, deletion fails
        if self.isEmpty():
            return False
        # Set the front value to -1 (optional, to indicate it's removed)
        self._data[self._front] = -1
        # Move front pointer one step forward (circularly)
        self._front = (self._front + 1) % self._capacity
        # Decrease the size of the deque after successful deletion
        self._size -= 1
        # If the deque becomes empty after deletion, reset rear to front
        if self.isEmpty():
            self._rear = self._front
        return True

    def deleteLast(self):
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        # If deque is empty, deletion fails
        if self.isEmpty():
            return False
        # Set the rear value to -1 (optional, to indicate it's removed)
        self._data[self._rear] = -1
        # Move rear pointer one step back (circularly)
        self._rear = (self._rear - 1) % self._capacity
        # Decrease the size of the deque after successful deletion
        self._size -= 1
        # If the deque becomes empty after deletion, reset front to rear
        if self.isEmpty():
            self._front = self._rear
        return True

    def getFront(self):
        """
        Get the front item from the deque.
        :rtype: int
        """
        # Return the value at the front pointer
        return self._data[self._front]

    def getRear(self):
        """
        Get the last item from the deque.
        :rtype: int
        """
        # Return the value at the rear pointer
        return self._data[self._rear]

    def isEmpty(self):
        """
        Checks whether the circular deque is empty or not.
        :rtype: bool
        """
        # Returns true if the size is 0, false otherwise
        return self._size == 0

    def isFull(self):
        """
        Checks whether the circular deque is full or not.
        :rtype: bool
        """
        # Returns true if the deque is at maximum capacity, false otherwise
        return self._size == self._capacity
