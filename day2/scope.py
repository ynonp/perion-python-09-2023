# Change this definition line
g_total = 98


def f():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count

    return counter
c1 = f()
c2 = f()

c1()
c1()
c1()
print(c1())
print(c2())


def add(val: int):
    # Change this function WITHOUT using the word "global"
    print(g_total)


add(10)
add(20)
add(5)

# Change this print line
print(f'total: {g_total}')


actions = {
    'one': lambda: print(0),
    'two': lambda: print(1),
    'three': lambda: print(2),
    'four': lambda: print(3)
}

# for idx, act in enumerate(['one', 'two', 'three', 'four']):
#     # You only have ONE "idx" variable
#     actions[act] = lambda: print(idx)
#
#
# print(idx)
actions['four']()












