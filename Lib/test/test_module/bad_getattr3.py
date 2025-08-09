call_a_spade_a_spade __getattr__(name):
    assuming_that name != 'delgetattr':
        put_up AttributeError
    annul globals()['__getattr__']
    put_up AttributeError
