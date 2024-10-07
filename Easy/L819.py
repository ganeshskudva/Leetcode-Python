import re
from collections import Counter

def mostCommonWord(self, paragraph: str, banned: list) -> str:
    # Step 1: Use regex to replace all non-alphabetic characters with spaces
    # TC: O(n), where n is the number of characters in the paragraph
    # SC: O(n), as we create a new string without punctuation
    paragraph = re.sub(r"[^\w]", " ", paragraph)
    
    # Step 2: Convert paragraph to lowercase and split into words
    # TC: O(n), splitting the string into words takes linear time
    # SC: O(n), space for storing the words in the list
    words = paragraph.lower().split()
    
    # Step 3: Use Counter to count words that are not in the banned list
    # TC: O(n), iterating through all words and counting them
    # SC: O(m), where m is the number of unique words
    word_count = Counter(word for word in words if word not in banned)
    
    # Step 4: Return the most common word
    # TC: O(m log m), where m is the number of unique words due to sorting inside most_common()
    # SC: O(1), constant space for returning the most common word
    return word_count.most_common(1)[0][0]

# Overall Time Complexity (TC):
# - Regex substitution: O(n)
# - Splitting paragraph: O(n)
# - Counting words: O(n)
# - Finding the most common word: O(m log m), where m is the number of unique words
# Total TC: O(n + m log m), where n is the length of the paragraph and m is the number of unique words

# Overall Space Complexity (SC):
# - Space for regex result: O(n)
# - Space for storing the words list: O(n)
# - Space for Counter: O(m), where m is the number of unique words
# Total SC: O(n + m)
