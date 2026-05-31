def pop(self):
    if not self.is_empty():
        return self.items.pop()
    return "Stack is Empty"