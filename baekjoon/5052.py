from sys import stdin


class Node:
    def __init__(self, char, isTerminal=False) -> None:
        self.char = char
        self.isTerminal = isTerminal
        self.children = {}


class Trie:
    def __init__(self) -> None:
        self.head = Node(None)

    def insert(self, string) -> None:
        current_node = self.head

        for char in string:
            if char not in current_node.children:
                current_node.children[char] = Node(char)
            current_node = current_node.children[char]

        current_node.isTerminal = True

    def search(self, string) -> bool:
        current_node = self.head

        for char in string:
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                return False

        if current_node.isTerminal:
            return True
        else:
            return False

    def consistency_check(self, string, numbers) -> bool:
        current_node = self.head

        for char in string:
            if char in current_node.children:
                current_node = current_node.children[char]
            # 탐색중에 termal 문자열을 만났는데(data in numbers) 
            # 그 밑으로 node들이 더 달려있다면
            # 일관성이 없음

            '''
            # 매 검색마다 O(N)
            if current_node.data in numbers and len(current_node.children) != 0:
                return False
            '''
            ''' O(L) 강제
            if current_node.data == string and len(current_node.children)!=0:
                return False
            '''
            if current_node.isTerminal==True and len(current_node.children)!=0:
                return False

        return True


T = int(stdin.readline())


def sol(): # M: 가장 긴 문자열의 길이 L:가장 짧은 길이 #T:O(N*M) , 가장 짧은 문자부터 검색하면 O(N*M+NlogN+L)
    N = int(stdin.readline())

    numbers = list()

    for _ in range(N):
        numbers.append(stdin.readline().rstrip())

    trie = Trie()

    # 입력 받은 전화번호들을 trie 구조에 추가해줌
    for number in numbers:
        trie.insert(number)
    
    # 가장 짧은 전화번호부터 검색하게
    numbers.sort(key=lambda x: len(x))

    # 각각의 전화번호에 대해서 trie에서 일관성 검사를 해줌
    # 원하는 string을 찾았을때 밑에 자식들이 더있으면 일관성이 없음 -> O(N*M)
    # Node 안에 termal을 붙여줘도 될듯 : best case는 가장 짧은 문자부터 시작할때
    for number in numbers:
        valid = trie.consistency_check(number, numbers)

        if not valid:
            print("NO")
            return
    print("YES")


for _ in range(T):
    sol()
