class Empty(Exception):
    pass

class LinkedStack:
    class _Node:
        __slots__ = '_element', '_next'
        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._head._element

    def push(self, e):
        self._head = self._Node(e, self._head)
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer
    
    def __str__(self):
        result = []
        start = self._head
        for _ in range(self._size):
            result.append(str(start._element))
            start = start._next
        return f"< {', '.join(result)}"
    

if __name__ == '__main__':
    S = LinkedStack()
    print(S)
    S.push(1)
    S.push(2)
    S.push(3)
    print(S)
    S.pop()
    print(S)
