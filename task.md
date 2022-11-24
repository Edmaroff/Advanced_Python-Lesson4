# Домашнее задание к лекции 2.«Iterators. Generators. Yield»

1. Доработать класс `FlatIterator` в коде ниже. Должен получиться итератор, который принимает список списков и возвращает их плоское представление, т.е последовательность состоящую из вложенных элементов. Функция `test` в коде ниже также должна отработать без ошибок.

```python
class FlatIterator:
    def __init__(self, list_of_list):
        ...
    def __iter__(self):
        ...
        return self
    def __next__(self):
        ...
        return item
def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]
    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item
    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
if __name__ == '__main__':
    test_1()
```


2. Доработать функцию flat_generator, Должен получиться генератор, который принимает список списков и возвращает их плоское представление.
Функция `test` в коде ниже также должна отработать без ошибок.
```python
import types
def flat_generator(list_of_lists):
    ...
    yield
    ...
def test_2():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]
    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item
    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)
if __name__ == '__main__':
    test_2()
    
```

3.__*__ Написать итератор аналогичный итератору из задания 1, но обрабатывающий списки с любым уровнем вложенности.
Шаблон и тест в коде ниже:
```python
class FlatIterator:
    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
    def __iter__(self):
        ...
        return self
    
    def __next__(self):
        ...
        return item
def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]
    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item
    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
if __name__ == '__main__':
    test_3()
```

4.__*__ Написать генератор аналогичный генератору из задания 2, но обрабатывающий списки с любым уровнем вложенности.
Шаблон и тест в коде ниже:
```python
import types
def flat_generator(list_of_list):
    ...
    yield
    ...
def test_4():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]
    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item
    assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)
if __name__ == '__main__':
    test_4()
```