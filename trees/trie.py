class TrieNode:

    def __init__(self) -> None:
        self.children = {}


class Trie:

    def __init__(self) -> None:
        self.root = TrieNode()

    def search(self, word):
        currentNode = self.root

        for char in word:
            # If the current node has a child key with a current character
            if currentNode.children.get(char):
                # Follow the child node
                currentNode = currentNode.children[char]
            else:
                # If the current character isn't found among the current nodes children
                # then the search word is not in the trie
                return None
        return currentNode

    def insert(self, word):
        currentNode = self.root

        for char in word:
            # If the current node has child key with current character
            if currentNode.children.get(char):
                # Follow the child node
                currentNode = currentNode.children[char]
            else:
                # Add the character as a new child node
                newNode = TrieNode()
                currentNode.children[char] = newNode

                # Follow this new node
                currentNode = newNode
        # After inserting the entire word into the trie
        # add a * key at the end
        currentNode.children['*'] = None

    def collectAllWords(self, node=None, word='', words=[]):

        # current node is the node passed in as the first paramter
        # or the root node if none is provided
        currentNode = node or self.root

        # Iterate through all the current node's children
        for key, childNode in currentNode.children.items():
            # If the current key is *, it means we hit the end of a complete word
            # so it can be added to our words array
            if key == '*':
                words.append(word)
            else:
                # If we're still in the middle of a word
                # we recursively call this function on the child node
                self.collectAllWords(childNode, word + key, words)
        return words

    def autocomplete(self, prefix):
        currentNode = self.search(prefix)
        if not currentNode:
            return None
        return self.collectAllWords(currentNode)

    def printKeys(self, node=None):
        currentNode = node or self.root

        for key, childNode in currentNode.children.items():
            print(key)
            if key != '*':
                self.printKeys(childNode.children)

    def autocorrect(self, text):
        currentNode = self.root
        suggestion = ''
        for char in text:
            if currentNode.children.get(char):
                suggestion += char
                currentNode = currentNode.children.get(char)
            else:
                # Collect all suffix with the prefix we've found so far
                return suggestion + self.collectAllWords(currentNode)[0]
        return suggestion