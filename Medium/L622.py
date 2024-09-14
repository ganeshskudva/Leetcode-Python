class MyCircularQueue:

    def __init__(self, k: int):
        # Initialize a fixed-size list `q` to represent the circular queue
        # The queue has a size of `k`, and all elements are initialized to 0
        self.q = [0] * k  
        
        # Initialize the `front` pointer to 0. This points to the front of the queue.
        self.front = 0
        
        # Initialize the `rear` pointer to -1. This will be updated to point to the last added element.
        self.rear = -1
        
        # Initialize the `length` to track the current number of elements in the queue.
        self.length = 0
        
        # Store the capacity of the circular queue.
        self.cap = k

    def enQueue(self, value: int) -> bool:
        # If the queue is full, we cannot add any more elements, so return False
        if self.isFull():
            return False

        # Increment the `rear` pointer (move to the next position) and wrap it around
        # if it exceeds the array bounds (modulo operation for circular behavior).
        self.rear = (self.rear + 1) % len(self.q)
        
        # Place the new value at the position indicated by `rear`.
        self.q[self.rear] = value
        
        # Increase the `length` to reflect the new element added.
        self.length += 1
        
        # Return True to indicate successful insertion.
        return True

    def deQueue(self) -> bool:
        # If the queue is empty, we cannot dequeue any element, so return False
        if self.isEmpty():
            return False

        # Increment the `front` pointer (move to the next position) and wrap it around
        # using modulo operation if it exceeds the array bounds.
        self.front = (self.front + 1) % len(self.q)
        
        # Decrease the `length` as we have removed an element from the queue.
        self.length -= 1
        
        # Return True to indicate successful removal.
        return True

    def Front(self) -> int:
        # If the queue is empty, return -1 as there is no front element.
        # Otherwise, return the element at the position `front`.
        return -1 if self.isEmpty() else self.q[self.front]

    def Rear(self) -> int:
        # If the queue is empty, return -1 as there is no rear element.
        # Otherwise, return the element at the position `rear`.
        return -1 if self.isEmpty() else self.q[self.rear]

    def isEmpty(self) -> bool:
        # The queue is empty if the `length` is 0.
        return self.length == 0

    def isFull(self) -> bool:
        # The queue is full if the `length` equals the capacity of the queue (`cap`).
        return self.length == self.cap
