def fun1():
    x = 1
    def fun2():
        print x
    fun2()

def func(*args):
    return args

print func(*[1, 2])
