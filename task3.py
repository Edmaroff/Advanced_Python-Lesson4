class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.external_index = 0
        self.internal_index = -1
        self.index = 0
        return self

    def __next__(self):
        self.internal_index += 1
        if self.internal_index >= len(self.list_of_list[self.external_index]):
            self.external_index += 1
            self.internal_index = 0
        self.elem = self.list_of_list[self.external_index][self.internal_index]
        while isinstance(self.elem, list):
            if len(self.elem) == 1:
                self.elem = self.elem[0]
            else:
                while self.index < len(self.elem):
                    if self.index == len(self.elem) - 1:
                        self.internal_index += 1
                        self.elem = self.elem[-1]
                        self.index = 0
                        return self.elem
                    self.elem = self.elem[self.index]
                    self.index += 1
                    self.internal_index -= 1
                    return self.elem
        if self.external_index >= len(self.list_of_list):
            raise StopIteration
        return self.elem


list_of_lists_2 = [
    [['a'], ['b', 'c', [[1, 2]], 1, 5, 6]],
    ['d', 'e', [['f'], 'h'], False],
    [1, 2, None, [[[[['!']]]]], []]
]

# a = FlatIterator(list_of_lists_2)
# for i in a:
#     print(i)
