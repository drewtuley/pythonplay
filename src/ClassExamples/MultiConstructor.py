class MultiConstructor(object):
    def __init__(self, *args, **kwargs):
        print('args=', args, ' kwargs=', kwargs)
        for key in kwargs:
            print('{}=>{}'.format(key, kwargs[key]))


mc = MultiConstructor()

mc = MultiConstructor(1)

mc = MultiConstructor(me='you')

mc = MultiConstructor('one', 1, one='One')
