import itertools
from typing import Iterable, Callable
from collections import defaultdict, Counter

def groupby(items: Iterable, key_fn: Callable):
    groups = defaultdict(list)
    for i in items:
        key = key_fn(i)
        groups[key].append(i)
    return groups


print(list(itertools.groupby(['one', 'two', 'three', 'four', 'five', 'abc'], lambda w: len(w))))
print(groupby(['one', 'two', 'three', 'four', 'five', 'abc'], lambda w: len(w)))


def uniq(source: Iterable):
    seen = set()
    for item in source:
        if item not in seen:
            yield item
            seen.add(item)


def real_uniq(source: Iterable):
    for item, count in Counter(source).items():
        if count == 1:
            yield item


def generator_uniq(source: Iterable):
    previous = None
    for i in source:
        if i != previous:
            yield i
        previous = i


items = [10, 20, 30, 40, 30, 30, 40, 30]
print(list(real_uniq(items)))
