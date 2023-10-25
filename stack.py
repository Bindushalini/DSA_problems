
class Stack:
    def __init__(self):
        self.items = []

    def is_stack_empty(self):
        return len(self.items) == 0
        # return not self.items

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def top(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


if __name__ == "__main__":
    s = Stack()
    print(s)
    print(s.is_stack_empty())
    s.push(3)
    print(s)
    s.push(7)
    s.push(5)
    print(s)
    print(s.pop())
    print(s)
    print(s.top())
    print(s.size())
