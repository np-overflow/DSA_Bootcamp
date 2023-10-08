class TrieNode:
    def __init__(self):
        self.children = [None] * 27  # Array of size 27
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def char_to_index(self, char):
        if char == " ":
            return 26
        return ord(char) - ord("a")

    def insert(self, word):
        current_node = self.root
        for char in word:
            index = self.char_to_index(char)
            if not current_node.children[index]:
                current_node.children[index] = TrieNode()
            current_node = current_node.children[index]
        current_node.is_end_of_word = True

    def search(self, query):
        def dfs(node, current_prefix):
            if node.is_end_of_word:
                results.append(current_prefix)
            
            for i, child_node in enumerate(node.children):
                if child_node:
                    dfs(child_node, current_prefix + chr(ord("a") + i))

        current_node = self.root
        results = []
        prefix = ""
        
        for char in query:
            index = self.char_to_index(char)
            if not current_node.children[index]:
                return results
            prefix += char
            current_node = current_node.children[index]
        
        dfs(current_node, prefix)
        return [query + word[len(prefix):] for word in results]

    def starts_with(self, prefix):
        current_node = self.root
        for char in prefix:
            index = self.char_to_index(char)
            if not current_node.children[index]:
                return False
            current_node = current_node.children[index]
        return True

    def delete(self, word):
        nodes_to_remove = []  # Stack to keep track of nodes to be removed
        current_node = self.root

        # Find the nodes corresponding to the characters in the word
        for char in word:
            index = self.char_to_index(char)
            if not current_node.children[index]:
                # Word is not in the Trie
                return
            nodes_to_remove.append((index, current_node))
            current_node = current_node.children[index]

        # If the last node represents the end of the word, mark it as not the end
        if current_node.is_end_of_word:
            current_node.is_end_of_word = False

        # Check if the last node has no children; if so, remove it and its ancestors
        if not any(current_node.children):
            for index, parent_node in reversed(nodes_to_remove):
                parent_node.children[index] = None

# Example usage:
trie = Trie()
trie.insert("apple")
trie.insert("app")
trie.insert("application")
trie.insert("bat")
trie.insert("cat")

results = trie.search("app")
print(results)  # Output: ["app", "apple", "application"]
trie.delete("app")
results = trie.search("app")
print(results)  # Output: ["apple", "application"]
