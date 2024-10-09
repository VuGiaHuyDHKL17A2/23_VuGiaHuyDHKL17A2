class Stack:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.data = []
        self.top = -1

    def __del__(self):
        del self.data

    def push(self, value):
        if not self.is_full():
            self.data.append(value)
            self.top += 1
        else:
            print("Ngăn xếp đầy, không thể thêm phần tử.")

    def pop(self):
        if not self.is_empty():
            value = self.data.pop()
            self.top -= 1
            return value
        else:
            print("Ngăn xếp rỗng, không có phần tử để lấy.")
            return None

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.capacity - 1

    def count(self):
        return self.top + 1

    def print_stack(self):
        print("Nội dung ngăn xếp:", self.data)
