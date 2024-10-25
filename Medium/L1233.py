class Trie:
    def __init__(self):
        # The sub-dictionary will store children nodes, where each folder level can have a sub-folder as a Trie node
        self.sub = collections.defaultdict(Trie)  # Space: O(N) where N is the total number of folder parts
        self.index = -1  # Stores the index of the folder, default to -1 (used for marking folder end)

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        self.root = Trie()  # Root Trie node
        self.ans = []  # List to store the result
        # Time: O(M * L), where M is the number of folders and L is the average length of each folder
        for i in range(len(folder)):
            cur = self.root  # Start from the root Trie node
            words = folder[i].split('/')  # Split folder path into parts
            # Time: O(L), iterate through each part (folder or sub-folder)
            for c in words:
                cur = cur.sub[c]  # Traverse or create the sub-folder nodes in the Trie
            cur.index = i  # Mark the folder end with the index
        # After constructing the Trie, we perform a DFS to collect non-subfolder paths
        self.dfs(self.root, folder)
        return self.ans
    
    def dfs(self, trie: Trie, folder: List[str]):
        # If the current node marks the end of a folder (i.e., a valid non-subfolder path)
        if trie.index != -1:
            self.ans.append(folder[trie.index])  # Add it to the result
        else:
            # Recursively traverse all sub-folders
            for c in trie.sub.values():
                self.dfs(c, folder)  # DFS over all child nodes

# Time Complexity (TC):
# - The Trie construction takes O(M * L), where M is the number of folders and L is the average length of the folder paths.
# - DFS takes O(M * L) to visit all nodes in the Trie, where each folder path is split into parts.
# - Total TC: O(M * L).

# Space Complexity (SC):
# - The Trie data structure will take O(N) space, where N is the total number of parts across all folder paths.
# - The recursion stack in DFS can go as deep as O(M) in the worst case.
# - Total SC: O(N), where N is the number of parts in all folders.
