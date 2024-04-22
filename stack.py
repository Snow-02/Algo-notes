import numpy as np


class listnode:
    def __init__(self, val: int):
        self.val = val
        self.next: listnode | None = None


class stack_linklist:
    def __init__(self):
        self._peek: listnode | None = None
        self._len = 0

    def is_empty(self):
        if self._peek == None:
            return True
        else:
            return False

    def size(self):
        return self._len

    def push(self, val: int):
        node = listnode(val)
        node.next = self._peek
        self._peek = node
        self._len += 1

    def pop(self):
        if self._len == 0:
            raise IndexError("栈已空")
        else:
            num = self.peek()
            self._peek = self._peek.next
            self.len -= 1
            return num

    def peek(self):
        if self.is_empty():
            raise IndexError("栈为空")
        else:
            return self._peek.val
    
    def to_list(self) -> list :
        arr = []
        node = self._peek
        while node:
            arr.append(node.val)
            node = node.next
        arr.reverse()
        return arr
        
class stack_list():
    def __init__(self):
        self._stack : list = []
    
    def is_empty(self):
        return self._stack == []
    
    def size(self):
        return len(self._stack)
    
    def push(self, val :int):
        self._stack.append(val)
    
    def peek(self):
        if self.is_empty():
            raise IndexError("The stack is empty!")
        else:
            return self._stack[-1]
        
    def pop(self):
        if self.is_empty():
            raise IndexError("The stack is empty!")
        else:
            return self._stack.pop()
        
stack1 = stack_linklist()
stack2 = stack_list()
print(stack1.is_empty())
stack1.push(1)
print(stack1.is_empty())
stack2.push(2)
stack2.push(3)
print(stack2.pop())
print(f"len of stack1 = {stack1.size()} \nlen of stack2 = {stack2.size()}")
        

