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
        current_node = self.root
        results = []
        prefix = ""

        # Traverse the Trie based on the characters in the query.
        for char in query:
            index = self.char_to_index(char)
            if not current_node.children[index]:
                return "No complete words found for the query!"
            prefix += char
            current_node = current_node.children[index]

        stack = [(current_node, prefix)]

        while stack:
            node, current_prefix = stack.pop()

            if node.is_end_of_word:
                results.append(current_prefix)

            for i, child_node in enumerate(node.children):
                if child_node:
                    stack.append((child_node, current_prefix + chr(97 + i)))

        return results

    def delete(self, word):
        nodes_to_remove = []
        current_node = self.root

        for char in word:
            index = self.char_to_index(char)
            if not current_node.children[index]:
                return "Word does not exist!"
            nodes_to_remove.append((index, current_node))
            current_node = current_node.children[index]

        if current_node.is_end_of_word:
            current_node.is_end_of_word = False

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

results = trie.search("fish")
print(results)