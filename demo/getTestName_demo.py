import inspect
#functions
def whoami():
    return inspect.stack()[1][3]

def MyFunc():
    x = whoami()
    print(x)

MyFunc()








def whosdaddy():
    return inspect.stack()[2][3]
def foo():
    print("hello, I am , daddy is %s" % (whoami(),whosdaddy()))
    bar()
def bar():
    print("hello, I am , daddy is %s" % (whoami(),whosdaddy()))
johny = bar
#call them.
foo()
bar()
johny()