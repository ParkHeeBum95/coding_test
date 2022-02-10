class Node:
    def __init__(self, key= None, value = None): #노드 생성
        self.key = key #key값 부여
        self.value = value #value값 부여
        self.next = None #다음 노드로의 링크(초기값 = None)
    def __str__(self): #print(node)시 수행될 함수
        return str(self.key) #노드 내 저장된 key값 출력

class SinglyLinkedList:
    def __init__(self): #연결 리스트 생성
        self.head = None
        self.size = 0
    def pushFront(self, key):
        new_node = Node(key) #새 노드 생성
        new_node.next = self.head #이 노드는 현재 노드의 이전 노트
        self.head = new_node #이제 self가 가르키는 노드를 삽입된 노드로 변경
        self.size += 1 #추가되었으므로 길이가 증가
    def pushBack(self, key):
        new_node = Node(key)#새 노드 생성
        if len(self) == 0: #노드가 없으면
            self.head = new_node #이 생성된 노드가 헤드노드로 삽입된다.
        else:
            tail = self.head
            while tail.next != None: #꼬리를 타고 물고간다 #O(n)
                tail = tail.next
            tail.next = new_node #마지막 노드에 삽입
            self.size += 1

    def popFront(self):
        if len(self) == 0:
            return None #삭제될 연산이 없다.
        else:
            x = self.head
            key = x.key
            self.head = x.next
            self.size -= 1
            del x
            return key
    def popBack(self):
        if len(self) == 0:
            return None
        else:
            pre, tail = None, self.head
            while tail.next != None: #꼬리를 물면서 뒤로 이동
                prev = tail
                tail = tail.next
            if prev == None: #기존 노드가 하나만 존재하면
                self.head = None
            else:
                prev.head = None
            key = tail.key
            del tail
            self.size -= 1
            return key

    def search(self,key):# #key 값의 노드 리턴, 없으면 None 리턴
        v = self.head
        while v != None:
            if v.key == key:
                return v
            v = v.next
        return None

