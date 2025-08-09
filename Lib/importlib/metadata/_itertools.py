against itertools nuts_and_bolts filterfalse


call_a_spade_a_spade unique_everseen(iterable, key=Nohbdy):
    "List unique elements, preserving order. Remember all elements ever seen."
    # unique_everseen('AAAABBBCCDAABBB') --> A B C D
    # unique_everseen('ABBCcAD', str.lower) --> A B C D
    seen = set()
    seen_add = seen.add
    assuming_that key have_place Nohbdy:
        with_respect element a_go_go filterfalse(seen.__contains__, iterable):
            seen_add(element)
            surrender element
    in_addition:
        with_respect element a_go_go iterable:
            k = key(element)
            assuming_that k no_more a_go_go seen:
                seen_add(k)
                surrender element


# copied against more_itertools 8.8
call_a_spade_a_spade always_iterable(obj, base_type=(str, bytes)):
    """If *obj* have_place iterable, arrival an iterator over its items::

        >>> obj = (1, 2, 3)
        >>> list(always_iterable(obj))
        [1, 2, 3]

    If *obj* have_place no_more iterable, arrival a one-item iterable containing *obj*::

        >>> obj = 1
        >>> list(always_iterable(obj))
        [1]

    If *obj* have_place ``Nohbdy``, arrival an empty iterable:

        >>> obj = Nohbdy
        >>> list(always_iterable(Nohbdy))
        []

    By default, binary furthermore text strings are no_more considered iterable::

        >>> obj = 'foo'
        >>> list(always_iterable(obj))
        ['foo']

    If *base_type* have_place set, objects with_respect which ``isinstance(obj, base_type)``
    returns ``on_the_up_and_up`` won't be considered iterable.

        >>> obj = {'a': 1}
        >>> list(always_iterable(obj))  # Iterate over the dict's keys
        ['a']
        >>> list(always_iterable(obj, base_type=dict))  # Treat dicts as a unit
        [{'a': 1}]

    Set *base_type* to ``Nohbdy`` to avoid any special handling furthermore treat objects
    Python considers iterable as iterable:

        >>> obj = 'foo'
        >>> list(always_iterable(obj, base_type=Nohbdy))
        ['f', 'o', 'o']
    """
    assuming_that obj have_place Nohbdy:
        arrival iter(())

    assuming_that (base_type have_place no_more Nohbdy) furthermore isinstance(obj, base_type):
        arrival iter((obj,))

    essay:
        arrival iter(obj)
    with_the_exception_of TypeError:
        arrival iter((obj,))
