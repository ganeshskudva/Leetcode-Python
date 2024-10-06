from collections import deque

class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        """
        This function checks if two sentences are similar. Sentences are considered similar if we can remove
        words from the front or the back of both sentences such that both sentences become equal.

        Parameters:
        sentence1 (str): The first input sentence, a string of words.
        sentence2 (str): The second input sentence, a string of words.

        Returns:
        bool: True if the sentences can be made similar by removing words from the front or back, otherwise False.

        Time Complexity: O(min(n, m)), where `n` is the number of words in `sentence1` and `m` is the number of words in `sentence2`.
                         We traverse both deques from the front and back, so the time complexity depends on the shorter sentence.
                         
        Space Complexity: O(n + m), where `n` is the number of words in `sentence1` and `m` is the number of words in `sentence2`.
                          We store both sentences in separate deques, resulting in space complexity proportional to the size of both sentences.
        """

        # Convert both sentences into deques by splitting them into lists of words.
        dq1, dq2 = map(deque, (sentence1.split(), sentence2.split()))

        # While both deques have elements and their front elements are equal, remove the front elements.
        # This loop checks for similarities at the start of both sentences.
        while dq1 and dq2 and dq1[0] == dq2[0]:
            dq1.popleft()  # Remove the word from the front of sentence1
            dq2.popleft()  # Remove the word from the front of sentence2

        # While both deques have elements and their back elements are equal, remove the back elements.
        # This loop checks for similarities at the end of both sentences.
        while dq1 and dq2 and dq1[-1] == dq2[-1]:
            dq1.pop()  # Remove the word from the back of sentence1
            dq2.pop()  # Remove the word from the back of sentence2

        # If either deque becomes empty, return True (sentences are similar).
        # If both deques still have elements after the comparisons, return False.
        return not dq1 or not dq2
