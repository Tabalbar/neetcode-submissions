class MinStack:

    def __init__(self):
        self.numbers = []
        self.min_element_dict = {}

    def push(self, val: int) -> None:
        self.numbers.append(val)
        curr_index = len(self.numbers) - 1
        prev_index = len(self.numbers) - 2
        print(prev_index)
        if len(self.numbers) == 1:
            self.min_element_dict[curr_index] = val
        elif self.min_element_dict[prev_index] > val:
            self.min_element_dict[curr_index] = val
        else:
            self.min_element_dict[curr_index] = self.min_element_dict[prev_index]

    def pop(self) -> None:
        del self.min_element_dict[len(self.numbers) - 1]
        self.numbers.pop()
        

    def top(self) -> int:
        return self.numbers[len(self.numbers) - 1]

    def getMin(self) -> int:
        return self.min_element_dict[len(self.numbers) - 1]
