class Stack:

    def __init__(self, initial_size = 10):
        self.arr = [0 for _ in range(initial_size)]
        self.next_index = 0
        self.num_elements = 0

    def push(self, data):
        if self.next_index == len(self.arr):
            print("Out of space! Increasing array capacity ...")
            self._handle_stack_capacity_full()

        self.arr[self.next_index] = data
        self.next_index += 1
        self.num_elements += 1

    # the pop method
    def pop(self):
        if self.num_elements==0:
            return None
        self.next_index-=1
        self.num_elements-=1
        return "popped"

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0

    def _handle_stack_capacity_full(self):
        old_arr = self.arr
        self.arr = [0 for _ in range( 2* len(old_arr))]
        for index, value in enumerate(old_arr):
            self.arr[index] = value
