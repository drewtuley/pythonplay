from src.ClassExamples.ExampleSimpleDecorator import ExampleSimpleDecorator


@ExampleSimpleDecorator('andrew')
def funcky():
    # this function is actually passed at compile time as an arg to the __call__ method
    # in the decorator class. The __call__ method then returns a function that Python assigns
    # to this function....
    print('I am in the middle of funkyiness')


print('function funcky() is actually', funcky)
funcky()


@ExampleSimpleDecorator('hope')
def civet():
    print('I am a civet')

print('function civet() is actually', civet)
civet()


@ExampleSimpleDecorator()
def no_decoration_parameter(arg):
    print('I have no decoration argument....')
    print('I have been called with ',arg)

print('function no_decoration_parameter() is actually', no_decoration_parameter)
no_decoration_parameter(10)


@ExampleSimpleDecorator('multiples')
def multiple_args(a,b):
    print('I have been called with {} and {}'.format(a,b))

print('function multiple_args() is actually', multiple_args)
multiple_args('AA', 'BB')


@ExampleSimpleDecorator(arg='Keyword Argument')
def keyword_func():
    print('me')


print('function keyword_func() is actually', keyword_func)
keyword_func()
