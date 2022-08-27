from sys import stdin


answer = []

words = set()

# 트라이에서의 탐색이 독특함.


class Node:
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}


# 결국 두  단어의 합치기는
# 접두사+나머지로 구분했을때
# 나머지가 이미 존재하는 단어인지
class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, word):
        global words
        curr_node = self.head

        words.add(word)

        for c in word:
            if c not in curr_node.children:
                curr_node.children[c] = Node(c)

            curr_node = curr_node.children[c]

        curr_node.data = word

    def traverse(self, word):
        global answer, words
        curr_node = self.head

        for c in word:
            if curr_node.data != None and word.removeprefix(curr_node.data) in words:
                answer.append(word)

            if c in curr_node.children:
                curr_node = curr_node.children[c]

            else:
                break


lines = []
trie = Trie()

lines = stdin.readlines()

for w in lines:
    trie.insert(w.strip())

for w in lines:
    trie.traverse(w.strip())

answer = list(set(answer))

for s in sorted(answer):
    print(s)
