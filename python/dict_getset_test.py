from timeit import timeit, Timer
from random import randrange

for i in range(1, 10):
    set_timer = Timer("x[randrange(%d)] = None"%i, "from __main__ import randrange, x")
    get_timer = Timer("x[randrange(%d)]"%i, "from __main__ import randrange, x")
    x = { j : None for j in range(i) }
    get_time = get_timer.timeit(number = 1000)
    set_time = set_timer.timeit(number = 1000)
    print("%d,%10.3f,%10.3f" % (i, get_time, set_time))
