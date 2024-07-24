import timeit
import random
l = [random.randint(-10,10000) for i in range(100)]
d = {i: random.randint(-10,10000) for i in range(100)}

def test1():
    i = random.randint(0,99)
    return l[i]   
def test2():
    i = random.randint(0,99)
    return d[i]
def test3():
    all(i >= 0 for i in l)

def test4():
    all(i >= 0 for i in d.values())


print(timeit.timeit(test1,number=52802136))
print(timeit.timeit(test2,number=52802136))

