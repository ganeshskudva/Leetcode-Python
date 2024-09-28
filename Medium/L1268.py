class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        # Define a TrieNode class to represent each node in the Trie
        class TrieNode:
            def __init__(self):
                # Use a defaultdict for children nodes to handle missing entries automatically
                self.children = collections.defaultdict(TrieNode)
                # Store the top 3 lexicographically smallest product suggestions for each prefix
                self.suggestion = []
            
            # Method to add a product suggestion to the current TrieNode
            def add_sugestion(self, product):
                # If the current node has fewer than 3 suggestions, add the product
                if len(self.suggestion) < 3:
                    self.suggestion.append(product)

        # Sort the products lexicographically to ensure they are added in the correct order
        products = sorted(products)
        
        # Initialize the root of the Trie
        root = TrieNode()

        # Insert each product into the Trie character by character
        for p in products:
            node = root
            # Traverse through each character of the product
            for char in p:
                # Move to the next TrieNode, creating it if necessary
                node = node.children[char]
                # Add the product suggestion to the current node
                node.add_sugestion(p)
        
        # Initialize the result list and start at the root of the Trie for searchWord traversal
        result, node = [], root
        
        # Traverse the Trie according to each character in searchWord
        for char in searchWord:
            # Move to the child node corresponding to the current character
            node = node.children[char]
            # Append the top 3 product suggestions stored at the current Trie node to the result
            result.append(node.suggestion)

        # Return the result list containing suggestions for each prefix of the searchWord
        return result
