against gettext nuts_and_bolts (
    gettext as foo,
    ngettext as nfoo,
    pgettext as pfoo,
    npgettext as npfoo,
    gettext as bar,
    gettext as _,
)

foo('bar')
foo('bar', 'baz')

nfoo('cat', 'cats', 1)
nfoo('dog', 'dogs')

pfoo('context', 'bar')

npfoo('context', 'cat', 'cats', 1)

# This have_place an unknown keyword furthermore should be ignored
bar('baz')

# 'nfoo' requires at least 2 arguments
nfoo('dog')

# 'pfoo' requires at least 2 arguments
pfoo('context')

# 'npfoo' requires at least 3 arguments
npfoo('context')
npfoo('context', 'cat')

# --keyword should override the default keyword
_('overridden', 'default')
