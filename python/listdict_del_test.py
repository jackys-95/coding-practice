from timeit import timeit, Timer
from random import randrange

for i in range(1, 1000):
    list_str = "x = " + str(list(range(i)))
    list_time = Timer(list_str)
    del_list_time = Timer(list_str + ";del x[randrange(%d)]"%i,
                          "from __main__ import randrange")

    dict_str = "y = " + str({j:None for j in range(i)})
    dict_time = Timer(dict_str)
    del_dict_time = Timer(dict_str + "; del y[randrange(%d)] "%i,
                          "from __main__ import randrange")
    
    list_del_time = del_list_time.timeit(number = 1000) - list_time.timeit(number = 1000)
    dict_del_time = del_dict_time.timeit(number = 1000) - dict_time.timeit(number = 1000)
        
    print("%d, %10.3f, %10.3f" % (i, list_del_time, dict_del_time))
