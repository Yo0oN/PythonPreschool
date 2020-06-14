# 트리의 각 노드를 위한 클래스
class Node :
    def __init__ (self, value) :
        self.value = value # 값
        self.left = None # 왼쪽 노드
        self.right = None # 오른쪽 노드

# 이진탐색트리
class NodeMgmt :
    # 제일 이진 탐색 트리를 만들 때 처음 노드를 head 루트로 놓는다.
    def __init__(self, head) :
        self.head = head # root노드 (제일 위)

    # 루트로부터 노드를 하나씩 연결하기
    def insert(self, value) :
        # 노드를 순회해야함. 제일 첫번째 시작은 루트부터임.
        self.current_node = self.head
        while True :
            # 만약 현재 확인중인 노드가 새로 들어온 값보다 크다면
            if value < self.current_node.value :
                # 들어온 값은 왼쪽으로 가야한다. 현재 노드의 왼쪽에 값이 있는지 확인하고
                # 만약 있다면 
                if self.current_node.left != None :
                    # 현재 확인 중인 노드를 왼쪽노드로 바꿔주고
                    self.current_node = self.current_node.left
                else :
                    # 없다면 노드를 새로 만들어서 이어준다.
                    self.current_node.left = Node(value)
                    # 그리고 반복문을 종료
                    break
            # 만약 현재 확인중인 노드가 새로 들어온 값보다 작다면
            else :
                # 들어온 값은 오른쪽으로 가야한다. 현재 노드의 오른쪽에 값이 있는지 확인하고
                if self.current_node.right != None :
                    # 값이 있다면 확인중인 노드를 오른쪽으로 바꿔준다.
                    self.current_node = self.current_node.right
                else :
                    # 값이 없다면 새 노드를 만들어 오른쪽에 이어준다.
                    self.current_node.right = Node(value)
                    # 그리고 반복문 종료
                    break
    # 이진 탐색트리를 탐색해보기
    def search(self, value) :
        # 처음은 루트부터 시작
        self.current_node = self.head
        # 루트노드부터 확인하기
        while self.current_node :
            # 만약 현재 노드의 값이 찾는값과 같다면 True
            if self.current_node.value == value :
                return True
            # 현재 노드의 값이 찾는값보다 크다면 
            elif value < self.current_node.value :
                # 현재노드를 왼쪽으로 옮겨서 다시 탐색
                self.current_node = self.current_node.left
            # 현재 노드의 값이 찾는값보다 작다면
            else :
                # 현재 노드를 오른쪽으로 옮겨서 다시 탐색
                self.current_node = self.current_node.right
        # 모든 노드를 봤는데 없다면 False 
        return False
    # 이진 탐색 트리에서 노드 삭제하기
    def delete(self, value) :
        searched = False # 값이 있는지 알려주는 변수
        self.current_node = self.head # 삭제할 노드
        self.parent = self.head # 삭제 노드의 부모 노드
        while self.current_node :
            # 현재 노드가 찾으려는 노드면 반복문 중단
            if self.current_node.value == value :
                searched = True
                break
            # 현재 노드가 찾으려는 값보다 크다면 왼쪽으로 가야함.
            elif value < self.current_node.value :
                # 왼쪽에 자식노드가 있다면 현재노드를 자식노드로 바꿔주고, 부모노드를 현재노드로 해준다.
                if self.current_node.left != None :
                    self.parent = self.current_node
                    self.current_node = self.current_node.left
                # 자식노드가 없다면 찾는값이 없으니 중단
                else :
                    break
                # 사실 elif안쪽의 if줄, else, break줄 없어도 상관없이 current_node가 None이 되는순간 반복문이 멈추니 없어도 된다.
            # 현재 노드가 찾으려는 값보다 작다면 오른쪽으로 가야함.
            else :
                # 오른쪽에 자식노드가 있다면 현재노드를 자식노드로 바꿔주고, 부모노드를 현재노드로 해준다.
                if self.current_node.right != None :
                    self.parent = self.current_node
                    self.current_node = self.current_node.right
                # 자식노드가 없다면 찾는값이 없으니 중단
                else :
                    break
        # 만약 삭제하려는 값이 없다면 여기서 함수를 중단한다.
        if searched = False :
            return False
        # 삭제값이 있다면 계속 진행
        # 삭제하려는 노드가 리프노드일 경우
        if self.current_node.left == None and self.current_node.right == None :
            # 삭제하려는노드가 부모의 왼쪽노드라면
            if value < self.parent.value :
                self.parent.left = None
            # 삭제하려는 노드가 부모의 오른쪽이라면
            else :
                self.parent.right = None
        # 삭제하려는 노드의 왼쪽에 자식이 있다면
        if self.current_node.left != None and self.current_node.right == None :
            # 삭제하려는노드가 부모의 왼쪽노드라면
            if value < self.parent.value :
                self.parent.left = self.current_node.left
            # 삭제하려는 노드가 부모의 오른쪽이라면
            else :
                self.parent.right = self.current_node.right
        # 삭제하려는 노드의 오른쪽에 자식이 있다면
        if self.current_node.left == None and self.current_node.right != None :
            # 삭제하려는노드가 부모의 왼쪽노드라면
            if value < self.parent.value :
                self.parent.left = self.current_node.left
            # 삭제하려는 노드가 부모의 오른쪽이라면
            else :
                self.parent.right = self.current_node.right



head = Node(1)
BST = NodeMgmt(head)
BST.insert(2)
BST.insert(3)
BST.insert(0)
BST.insert(4)
BST.insert(8)
print(BST.search(7))
