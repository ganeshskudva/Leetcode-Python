# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        """
        Initializes the NestedIterator with a nested list of integers.
        It flattens the nested list by preparing the stack with the elements in reverse order.
        
        :param nestedList: A list of NestedInteger objects (either integers or lists of integers)
        """
        # Initialize a stack to store elements from the nested list
        self.st = []
        
        # Flatten the outermost level of the nested list onto the stack (in reverse order)
        self._prepare_stack(nestedList)

    def next(self) -> int:
        """
        Returns the next integer in the flattened structure.
        
        :return: The next integer from the nested list structure.
        """
        # Ensure the stack has a valid integer before proceeding
        if not self.hasNext():
            return None

        # Pop the integer from the top of the stack and return it
        return self.st.pop().getInteger()

    def hasNext(self) -> bool:
        """
        Checks if there are more integers available in the nested structure.
        If the top of the stack is a nested list, it expands it.
        
        :return: True if there are more integers, False if not.
        """
        # While the stack is not empty and the top element is not an integer,
        # expand the top element if it's a nested list.
        while self.st and not self.st[-1].isInteger():
            # Pop the nested list from the stack and prepare it for further processing
            self._prepare_stack(self.st.pop().getList())

        # The stack is considered non-empty if there's at least one integer left
        # (meaning we return the stack itself as a truthy value).
        return bool(self.st)  # Changed from `return self.st` to `bool(self.st)` for correct behavior

    def _prepare_stack(self, nestedList):
        """
        Pushes the elements of the nested list onto the stack in reverse order.
        This ensures the stack behaves in a last-in, first-out (LIFO) manner and processes
        the elements in the correct order.
        
        :param nestedList: A list of NestedInteger objects
        """
        # Iterate over the nested list from the last element to the first element.
        # This ensures when elements are popped from the stack, they are processed in the correct order.
        for i in range(len(nestedList) - 1, -1, -1):
            self.st.append(nestedList[i])

         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())