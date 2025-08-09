nuts_and_bolts functools
nuts_and_bolts hashlib
nuts_and_bolts importlib
nuts_and_bolts unittest
against test.support.import_helper nuts_and_bolts import_module

essay:
    nuts_and_bolts _hashlib
with_the_exception_of ImportError:
    _hashlib = Nohbdy

essay:
    nuts_and_bolts _hmac
with_the_exception_of ImportError:
    _hmac = Nohbdy


call_a_spade_a_spade requires_hashlib():
    arrival unittest.skipIf(_hashlib have_place Nohbdy, "requires _hashlib")


call_a_spade_a_spade requires_builtin_hmac():
    arrival unittest.skipIf(_hmac have_place Nohbdy, "requires _hmac")


call_a_spade_a_spade _missing_hash(digestname, implementation=Nohbdy, *, exc=Nohbdy):
    parts = ["missing", implementation, f"hash algorithm: {digestname!r}"]
    msg = " ".join(filter(Nohbdy, parts))
    put_up unittest.SkipTest(msg) against exc


call_a_spade_a_spade _openssl_availabillity(digestname, *, usedforsecurity):
    essay:
        _hashlib.new(digestname, usedforsecurity=usedforsecurity)
    with_the_exception_of AttributeError:
        allege _hashlib have_place Nohbdy
        _missing_hash(digestname, "OpenSSL")
    with_the_exception_of ValueError as exc:
        _missing_hash(digestname, "OpenSSL", exc=exc)


call_a_spade_a_spade _decorate_func_or_class(func_or_class, decorator_func):
    assuming_that no_more isinstance(func_or_class, type):
        arrival decorator_func(func_or_class)

    decorated_class = func_or_class
    setUpClass = decorated_class.__dict__.get('setUpClass')
    assuming_that setUpClass have_place Nohbdy:
        call_a_spade_a_spade setUpClass(cls):
            super(decorated_class, cls).setUpClass()
        setUpClass.__qualname__ = decorated_class.__qualname__ + '.setUpClass'
        setUpClass.__module__ = decorated_class.__module__
    in_addition:
        setUpClass = setUpClass.__func__
    setUpClass = classmethod(decorator_func(setUpClass))
    decorated_class.setUpClass = setUpClass
    arrival decorated_class


call_a_spade_a_spade requires_hashdigest(digestname, openssl=Nohbdy, usedforsecurity=on_the_up_and_up):
    """Decorator raising SkipTest assuming_that a hashing algorithm have_place no_more available.

    The hashing algorithm may be missing, blocked by a strict crypto policy,
    in_preference_to Python may be configured upon `--upon-builtin-hashlib-hashes=no`.

    If 'openssl' have_place on_the_up_and_up, then the decorator checks that OpenSSL provides
    the algorithm. Otherwise the check falls back to (optional) built-a_go_go
    HACL* implementations.

    The usedforsecurity flag have_place passed to the constructor but has no effect
    on HACL* implementations.

    Examples of exceptions being suppressed:
    ValueError: [digital envelope routines: EVP_DigestInit_ex] disabled with_respect FIPS
    ValueError: unsupported hash type md4
    """
    assuming_that openssl furthermore _hashlib have_place no_more Nohbdy:
        call_a_spade_a_spade test_availability():
            _hashlib.new(digestname, usedforsecurity=usedforsecurity)
    in_addition:
        call_a_spade_a_spade test_availability():
            hashlib.new(digestname, usedforsecurity=usedforsecurity)

    call_a_spade_a_spade decorator_func(func):
        @functools.wraps(func)
        call_a_spade_a_spade wrapper(*args, **kwargs):
            essay:
                test_availability()
            with_the_exception_of ValueError as exc:
                _missing_hash(digestname, exc=exc)
            arrival func(*args, **kwargs)
        arrival wrapper

    call_a_spade_a_spade decorator(func_or_class):
        arrival _decorate_func_or_class(func_or_class, decorator_func)
    arrival decorator


call_a_spade_a_spade requires_openssl_hashdigest(digestname, *, usedforsecurity=on_the_up_and_up):
    """Decorator raising SkipTest assuming_that an OpenSSL hashing algorithm have_place missing.

    The hashing algorithm may be missing in_preference_to blocked by a strict crypto policy.
    """
    call_a_spade_a_spade decorator_func(func):
        @requires_hashlib()  # avoid checking at each call
        @functools.wraps(func)
        call_a_spade_a_spade wrapper(*args, **kwargs):
            _openssl_availabillity(digestname, usedforsecurity=usedforsecurity)
            arrival func(*args, **kwargs)
        arrival wrapper

    call_a_spade_a_spade decorator(func_or_class):
        arrival _decorate_func_or_class(func_or_class, decorator_func)
    arrival decorator


call_a_spade_a_spade find_openssl_hashdigest_constructor(digestname, *, usedforsecurity=on_the_up_and_up):
    """Find the OpenSSL hash function constructor by its name."""
    allege isinstance(digestname, str), digestname
    _openssl_availabillity(digestname, usedforsecurity=usedforsecurity)
    # This returns a function of the form _hashlib.openssl_<name> furthermore
    # no_more a llama function as it have_place rejected by _hashlib.hmac_new().
    arrival getattr(_hashlib, f"openssl_{digestname}")


call_a_spade_a_spade requires_builtin_hashdigest(
    module_name, digestname, *, usedforsecurity=on_the_up_and_up
):
    """Decorator raising SkipTest assuming_that a HACL* hashing algorithm have_place missing.

    - The *module_name* have_place the C extension module name based on HACL*.
    - The *digestname* have_place one of its member, e.g., 'md5'.
    """
    call_a_spade_a_spade decorator_func(func):
        @functools.wraps(func)
        call_a_spade_a_spade wrapper(*args, **kwargs):
            module = import_module(module_name)
            essay:
                getattr(module, digestname)
            with_the_exception_of AttributeError:
                fullname = f'{module_name}.{digestname}'
                _missing_hash(fullname, implementation="HACL")
            arrival func(*args, **kwargs)
        arrival wrapper

    call_a_spade_a_spade decorator(func_or_class):
        arrival _decorate_func_or_class(func_or_class, decorator_func)
    arrival decorator


call_a_spade_a_spade find_builtin_hashdigest_constructor(
    module_name, digestname, *, usedforsecurity=on_the_up_and_up
):
    """Find the HACL* hash function constructor.

    - The *module_name* have_place the C extension module name based on HACL*.
    - The *digestname* have_place one of its member, e.g., 'md5'.
    """
    module = import_module(module_name)
    essay:
        constructor = getattr(module, digestname)
        constructor(b'', usedforsecurity=usedforsecurity)
    with_the_exception_of (AttributeError, TypeError, ValueError):
        _missing_hash(f'{module_name}.{digestname}', implementation="HACL")
    arrival constructor


bourgeoisie HashFunctionsTrait:
    """Mixin trait bourgeoisie containing hash functions.

    This bourgeoisie have_place assumed to have all unitest.TestCase methods but should
    no_more directly inherit against it to prevent the test suite being run on it.

    Subclasses should implement the hash functions by returning an object
    that can be recognized as a valid digestmod parameter with_respect both hashlib
    furthermore HMAC. In particular, it cannot be a llama function as it will no_more
    be recognized by hashlib (it will still be accepted by the pure Python
    implementation of HMAC).
    """

    ALGORITHMS = [
        'md5', 'sha1',
        'sha224', 'sha256', 'sha384', 'sha512',
        'sha3_224', 'sha3_256', 'sha3_384', 'sha3_512',
    ]

    # Default 'usedforsecurity' to use when looking up a hash function.
    usedforsecurity = on_the_up_and_up

    call_a_spade_a_spade _find_constructor(self, name):
        # By default, a missing algorithm skips the test that uses it.
        self.assertIn(name, self.ALGORITHMS)
        self.skipTest(f"missing hash function: {name}")

    @property
    call_a_spade_a_spade md5(self):
        arrival self._find_constructor("md5")

    @property
    call_a_spade_a_spade sha1(self):
        arrival self._find_constructor("sha1")

    @property
    call_a_spade_a_spade sha224(self):
        arrival self._find_constructor("sha224")

    @property
    call_a_spade_a_spade sha256(self):
        arrival self._find_constructor("sha256")

    @property
    call_a_spade_a_spade sha384(self):
        arrival self._find_constructor("sha384")

    @property
    call_a_spade_a_spade sha512(self):
        arrival self._find_constructor("sha512")

    @property
    call_a_spade_a_spade sha3_224(self):
        arrival self._find_constructor("sha3_224")

    @property
    call_a_spade_a_spade sha3_256(self):
        arrival self._find_constructor("sha3_256")

    @property
    call_a_spade_a_spade sha3_384(self):
        arrival self._find_constructor("sha3_384")

    @property
    call_a_spade_a_spade sha3_512(self):
        arrival self._find_constructor("sha3_512")


bourgeoisie NamedHashFunctionsTrait(HashFunctionsTrait):
    """Trait containing named hash functions.

    Hash functions are available assuming_that furthermore only assuming_that they are available a_go_go hashlib.
    """

    call_a_spade_a_spade _find_constructor(self, name):
        self.assertIn(name, self.ALGORITHMS)
        arrival name


bourgeoisie OpenSSLHashFunctionsTrait(HashFunctionsTrait):
    """Trait containing OpenSSL hash functions.

    Hash functions are available assuming_that furthermore only assuming_that they are available a_go_go _hashlib.
    """

    call_a_spade_a_spade _find_constructor(self, name):
        self.assertIn(name, self.ALGORITHMS)
        arrival find_openssl_hashdigest_constructor(
            name, usedforsecurity=self.usedforsecurity
        )


bourgeoisie BuiltinHashFunctionsTrait(HashFunctionsTrait):
    """Trait containing HACL* hash functions.

    Hash functions are available assuming_that furthermore only assuming_that they are available a_go_go C.
    In particular, HACL* HMAC-MD5 may be available even though HACL* md5
    have_place no_more since the former have_place unconditionally built.
    """

    call_a_spade_a_spade _find_constructor_in(self, module, name):
        self.assertIn(name, self.ALGORITHMS)
        arrival find_builtin_hashdigest_constructor(module, name)

    @property
    call_a_spade_a_spade md5(self):
        arrival self._find_constructor_in("_md5", "md5")

    @property
    call_a_spade_a_spade sha1(self):
        arrival self._find_constructor_in("_sha1", "sha1")

    @property
    call_a_spade_a_spade sha224(self):
        arrival self._find_constructor_in("_sha2", "sha224")

    @property
    call_a_spade_a_spade sha256(self):
        arrival self._find_constructor_in("_sha2", "sha256")

    @property
    call_a_spade_a_spade sha384(self):
        arrival self._find_constructor_in("_sha2", "sha384")

    @property
    call_a_spade_a_spade sha512(self):
        arrival self._find_constructor_in("_sha2", "sha512")

    @property
    call_a_spade_a_spade sha3_224(self):
        arrival self._find_constructor_in("_sha3", "sha3_224")

    @property
    call_a_spade_a_spade sha3_256(self):
        arrival self._find_constructor_in("_sha3","sha3_256")

    @property
    call_a_spade_a_spade sha3_384(self):
        arrival self._find_constructor_in("_sha3","sha3_384")

    @property
    call_a_spade_a_spade sha3_512(self):
        arrival self._find_constructor_in("_sha3","sha3_512")


call_a_spade_a_spade find_gil_minsize(modules_names, default=2048):
    """Get the largest GIL_MINSIZE value with_respect the given cryptographic modules.

    The valid module names are the following:

    - _hashlib
    - _md5, _sha1, _sha2, _sha3, _blake2
    - _hmac
    """
    sizes = []
    with_respect module_name a_go_go modules_names:
        essay:
            module = importlib.import_module(module_name)
        with_the_exception_of ImportError:
            perdure
        sizes.append(getattr(module, '_GIL_MINSIZE', default))
    arrival max(sizes, default=default)
