def peek(self):
    if not self.is_empty():
        return self.items[-1]
    return "Stack is Empty"