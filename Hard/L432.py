from collections import defaultdict

class Node(object):
    def __init__(self):
        # Each Node holds a set of keys with the same frequency, along with pointers to the previous and next Node
        self.key_set = set([])  # Set to store keys at this frequency
        self.prev, self.nxt = None, None  # Doubly linked list pointers for previous and next nodes

    def add_key(self, key):
        # Add a key to the key set
        self.key_set.add(key)

    def remove_key(self, key):
        # Remove a key from the key set
        self.key_set.remove(key)

    def get_any_key(self):
        # Get any key from the key set (arbitrarily pick one)
        if self.key_set:
            result = self.key_set.pop()  # Pop the key (removes from set)
            self.add_key(result)  # Re-add to set so it is still in the node
            return result
        return None  # If no keys in set, return None

    def count(self):
        # Return the count of keys in this node (size of key_set)
        return len(self.key_set)

    def is_empty(self):
        # Check if the node has no keys (used to determine if node should be removed)
        return len(self.key_set) == 0


class DoubleLinkedList(object):
    def __init__(self):
        # Initialize a dummy head and tail for the doubly linked list (sentinel nodes)
        self.head_node, self.tail_node = Node(), Node()
        # Link dummy head to dummy tail
        self.head_node.nxt, self.tail_node.prev = self.tail_node, self.head_node

    def insert_after(self, x):
        # Insert a new node after node x and return the new node
        node, temp = Node(), x.nxt  # Create a new node
        x.nxt, node.prev = node, x  # Link x to the new node and set new node's previous to x
        node.nxt, temp.prev = temp, node  # Link new node to the next node and adjust the previous link of temp
        return node
    
    def insert_before(self, x):
        # Insert a new node before node x (reuses insert_after function)
        return self.insert_after(x.prev)

    def remove(self, x):
        # Remove node x from the linked list
        prev_node = x.prev
        prev_node.nxt, x.nxt.prev = x.nxt, prev_node  # Adjust links of the neighboring nodes to bypass x

    def get_head(self):
        # Get the first real node (the node after the dummy head)
        return self.head_node.nxt
    
    def get_tail(self):
        # Get the last real node (the node before the dummy tail)
        return self.tail_node.prev

    def get_sentinel_head(self):
        # Get the dummy head (used to mark the start of the list)
        return self.head_node

    def get_sentinel_tail(self):
        # Get the dummy tail (used to mark the end of the list)
        return self.tail_node
    

class AllOne(object):
    def __init__(self):
        """
        Initialize the data structure.
        """
        self.dll = DoubleLinkedList()  # Create a doubly linked list to hold the nodes
        self.key_counter = defaultdict(int)  # Dictionary to store the frequency of each key
        self.node_freq = {0: self.dll.get_sentinel_head()}  # Mapping frequency to node in the DLL

    def _rmv_key_pf_node(self, pf, key):
        """
        Remove the key from the node with frequency pf. 
        If the node is empty after removing the key, remove the node from the list.
        """
        node = self.node_freq[pf]  # Get the node corresponding to frequency pf
        node.remove_key(key)  # Remove the key from the node
        if node.is_empty():
            # If the node is empty, remove it from the list and delete it from node_freq
            self.dll.remove(node)
            self.node_freq.pop(pf)

    def inc(self, key):
        """
        Increments the value of the key by 1. If key doesn't exist, insert it with value 1.
        """
        self.key_counter[key] += 1  # Increment the frequency of the key
        cf, pf = self.key_counter[key], self.key_counter[key] - 1  # Current and previous frequencies
        
        if cf not in self.node_freq:
            # If the current frequency doesn't have a corresponding node, create one after the previous node
            self.node_freq[cf] = self.dll.insert_after(self.node_freq[pf])
        
        # Add the key to the node corresponding to its current frequency
        self.node_freq[cf].add_key(key)

        # If previous frequency was greater than 0, remove the key from the previous frequency node
        if pf > 0:
            self._rmv_key_pf_node(pf, key)

    def dec(self, key):
        """
        Decrements the value of the key by 1. If the value becomes 0, remove the key from the structure.
        """
        if key in self.key_counter:
            self.key_counter[key] -= 1  # Decrease the frequency of the key
            cf, pf = self.key_counter[key], self.key_counter[key] + 1  # Current and previous frequencies

            if self.key_counter[key] == 0:
                # If the frequency becomes 0, remove the key from key_counter
                self.key_counter.pop(key)
            
            if cf != 0:
                # If the current frequency is greater than 0, add the key to the node corresponding to the current frequency
                if cf not in self.node_freq:
                    # If the current frequency node doesn't exist, create it before the previous frequency node
                    self.node_freq[cf] = self.dll.insert_before(self.node_freq[pf])
                self.node_freq[cf].add_key(key)

            # Remove the key from the node corresponding to its previous frequency
            self._rmv_key_pf_node(pf, key)

    def getMaxKey(self):
        """
        Returns one of the keys with the maximum frequency.
        """
        return self.dll.get_tail().get_any_key() if self.dll.get_tail().count() > 0 else ""

    def getMinKey(self):
        """
        Returns one of the keys with the minimum frequency.
        """
        return self.dll.get_head().get_any_key() if self.dll.get_head().count() > 0 else ""
