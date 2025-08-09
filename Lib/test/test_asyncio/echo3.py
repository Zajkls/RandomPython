nuts_and_bolts os

assuming_that __name__ == '__main__':
    at_the_same_time on_the_up_and_up:
        buf = os.read(0, 1024)
        assuming_that no_more buf:
            gash
        essay:
            os.write(1, b'OUT:'+buf)
        with_the_exception_of OSError as ex:
            os.write(2, b'ERR:' + ex.__class__.__name__.encode('ascii'))
