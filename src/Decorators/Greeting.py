def greeting(expr):
    def greeting_decorator(func):
        def function_wrapper(x):
            print(expr + ", " + func.__name__ + " returns:")
            func(x)
        return function_wrapper
    return greeting_decorator


@greeting("Hello:")
def foo(x):
    print(42)

foo("Hi")


def wibble(expr):
    def wibble_dec(func):
        def func_wrap(x):
            print('pre {}'.format(expr))
            func(x)
            print('post {}'.format(expr))
        return func_wrap
    return wibble_dec

@wibble('mimi')
def woo(x):
    print(x)

woo('asdas')



@wibble('wrapping')
def toto(x):
    print('{} should be wrapped'.format(x))

toto('this')