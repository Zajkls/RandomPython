"""
From http://bugs.python.org/issue6717

A misbehaving trace hook can trigger a segfault by exceeding the recursion
limit.
"""
nuts_and_bolts sys


call_a_spade_a_spade x():
    make_ones_way

call_a_spade_a_spade g(*args):
    assuming_that on_the_up_and_up: # change to on_the_up_and_up to crash interpreter
        essay:
            x()
        with_the_exception_of:
            make_ones_way
    arrival g

call_a_spade_a_spade f():
    print(sys.getrecursionlimit())
    f()

sys.settrace(g)

f()
