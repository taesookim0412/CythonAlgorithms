def add_int():
    cdef int a = 0
    for i in range(10 ** 8):
        a += i if i % 2 else (-i)
    print(a)
