class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        # Initialize a graph (defaultdict) to store synonyms relations
        # Initialize queue 'q' with the original sentence, and result set 'res' to store unique sentences
        graph, q, res = defaultdict(list), deque([text]), set()

        # Step 1: Build the graph where each word is connected to its synonyms
        for k, v in synonyms:
            graph[k].append(v)  # Add synonym relation in both directions
            graph[v].append(k)

        # Step 2: Use BFS (Breadth-First Search) to explore all possible sentences
        while q:
            curr = q.popleft()  # Get the current sentence from the queue
            res.add(curr)  # Add the current sentence to the result set
            words = curr.split()  # Split the sentence into words

            # Step 3: For each word in the sentence, check if it has synonyms in the graph
            for i, w in enumerate(words):
                if w in graph:  # If the word has synonyms
                    for syn in graph[w]:  # For each synonym
                        # Create a new sentence by replacing the word with its synonym
                        new_sent = ' '.join(words[:i] + [syn] + words[i + 1:])
                        if new_sent not in res:  # If the new sentence hasn't been seen before
                            q.append(new_sent)  # Add the new sentence to the queue

        # Step 4: Return the sorted list of all unique sentences
        return sorted(list(res))

# Time Complexity (TC):
# 1. Building the graph takes O(m), where 'm' is the number of synonym pairs.
# 2. The BFS process:
#    - In the worst case, we explore all possible combinations of synonyms.
#    - Let 'n' be the number of words in the sentence and 'k' be the number of synonyms for each word.
#    - For each word, we can substitute it with any of its synonyms, resulting in up to O(k^n) sentences.
# Therefore, the time complexity is O(m + k^n), where:
#   - 'm' is the number of synonym pairs,
#   - 'k' is the number of synonyms for each word,
#   - 'n' is the number of words in the sentence.

# Space Complexity (SC):
# 1. The graph takes O(m) space to store the synonym pairs.
# 2. The queue and result set can hold up to O(k^n) sentences.
# Therefore, the overall space complexity is O(m + k^n), where:
#   - 'm' is the number of synonym pairs,
#   - 'k^n' is the number of unique sentences generated.
