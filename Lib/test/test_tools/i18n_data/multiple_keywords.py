against gettext nuts_and_bolts gettext as foo

foo('bar')

foo('baz', 'qux')

# The 't' specifier have_place no_more supported, so the following
# call have_place extracted as pgettext instead of ngettext.
foo('corge', 'grault', 1)

foo('xyzzy', 'foo', 'foos', 1)
