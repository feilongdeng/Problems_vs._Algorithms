#Building a Trie in Python

#Before we start let us reiterate the key components of a Trie or Prefix Tree.
#A trie is a tree-like data structure that stores a dynamic set of strings.
#Tries are commonly used to facilitate operations like predictive text or autocomplete features on mobile phones or web search.

#Before we move into the autocomplete function we need to create a working trie for storing strings. We will create two classes:

 #.A Trie class that contains the root node(empty string)
 #.A TrieNode class that exposes the general functionality of the Trie, like inserting a word or finding the node which represents a prefix.

# Give it a try by implementing the TrieNode and Trie classes below!

    
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        parent_node = self.root

        for char in word:
            parent_node.insert(char)

            parent_node = parent_node.children[char]
        

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        nodeFind = self.root

        for char in prefix:
            if char not in nodeFind.children:
                return None
            nodeFind = nodeFind.children[char]

        return nodeFind


class TrieNode:
    def __init__(self, value = ''):
        ## Initialize this node in the Trie
        self.value = value
        self.children = {}
        
        
    def insert(self, char):
        ## Add a child node in this Trie
        if char not in self.children:
            self.children[char] = TrieNode(char)
        
    def suffixes(self, suffix = ''):

        suflist = []

        if len(self.children) > 0:

            for child in self.children:

                suflist += self.children[child].suffixes(suffix + child)

            return suflist

        return [suffix]

    

    



MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)



def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print(', '.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print(None)


print("Test 1")    
f('') # return ''

print("\nTest 2")
f('a') # should return: 'nt, nthology, ntagonist, ntogym'

print("\nTest 3")
f('c') # should return "c not found"

print("\nTest 4")
f('anto') # should return "nym"
