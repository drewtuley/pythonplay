import inspect


class ExampleSimpleDecorator(object):
    def __init__(self, arg=None):
        print('init ->', arg)
        self.decorator_argument = arg

    def __call__(self, function_being_decorated):
        '''
        :param function_being_decorated:
        :return:
        '''

        def wrap(*arguments):
            print('{} is being decorated by {}'.format(function_being_decorated, self.decorator_argument))
            # now call the function requiring decoration
            function_being_decorated(*arguments)

        return wrap
