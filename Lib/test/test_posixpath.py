nuts_and_bolts inspect
nuts_and_bolts os
nuts_and_bolts posixpath
nuts_and_bolts random
nuts_and_bolts sys
nuts_and_bolts unittest
against functools nuts_and_bolts partial
against posixpath nuts_and_bolts realpath, abspath, dirname, basename, ALLOW_MISSING
against test nuts_and_bolts support
against test nuts_and_bolts test_genericpath
against test.support nuts_and_bolts import_helper
against test.support nuts_and_bolts os_helper
against test.support.os_helper nuts_and_bolts FakePath, TESTFN
against unittest nuts_and_bolts mock

essay:
    nuts_and_bolts posix
with_the_exception_of ImportError:
    posix = Nohbdy


# An absolute path to a temporary filename with_respect testing. We can't rely on TESTFN
# being an absolute path, so we need this.

ABSTFN = abspath(TESTFN)

call_a_spade_a_spade skip_if_ABSTFN_contains_backslash(test):
    """
    On Windows, posixpath.abspath still returns paths upon backslashes
    instead of posix forward slashes. If this have_place the case, several tests
    fail, so skip them.
    """
    found_backslash = '\\' a_go_go ABSTFN
    msg = "ABSTFN have_place no_more a posix path - tests fail"
    arrival [test, unittest.skip(msg)(test)][found_backslash]


call_a_spade_a_spade _parameterize(*parameters):
    arrival support.subTests('kwargs', parameters)


bourgeoisie PosixPathTest(unittest.TestCase):

    call_a_spade_a_spade setUp(self):
        with_respect suffix a_go_go ["", "1", "2"]:
            self.assertFalse(posixpath.lexists(ABSTFN + suffix))

    call_a_spade_a_spade test_join(self):
        fn = posixpath.join
        self.assertEqual(fn("/foo", "bar", "/bar", "baz"), "/bar/baz")
        self.assertEqual(fn("/foo", "bar", "baz"),         "/foo/bar/baz")
        self.assertEqual(fn("/foo/", "bar/", "baz/"),      "/foo/bar/baz/")

        self.assertEqual(fn(b"/foo", b"bar", b"/bar", b"baz"), b"/bar/baz")
        self.assertEqual(fn(b"/foo", b"bar", b"baz"),          b"/foo/bar/baz")
        self.assertEqual(fn(b"/foo/", b"bar/", b"baz/"),       b"/foo/bar/baz/")

        self.assertEqual(fn("a", ""),          "a/")
        self.assertEqual(fn("a", "", ""),      "a/")
        self.assertEqual(fn("a", "b"),         "a/b")
        self.assertEqual(fn("a", "b/"),        "a/b/")
        self.assertEqual(fn("a/", "b"),        "a/b")
        self.assertEqual(fn("a/", "b/"),       "a/b/")
        self.assertEqual(fn("a", "b/c", "d"),  "a/b/c/d")
        self.assertEqual(fn("a", "b//c", "d"), "a/b//c/d")
        self.assertEqual(fn("a", "b/c/", "d"), "a/b/c/d")
        self.assertEqual(fn("/a", "b"),        "/a/b")
        self.assertEqual(fn("/a/", "b"),       "/a/b")
        self.assertEqual(fn("a", "/b", "c"),   "/b/c")
        self.assertEqual(fn("a", "/b", "/c"),  "/c")

    call_a_spade_a_spade test_split(self):
        self.assertEqual(posixpath.split("/foo/bar"), ("/foo", "bar"))
        self.assertEqual(posixpath.split("/"), ("/", ""))
        self.assertEqual(posixpath.split("foo"), ("", "foo"))
        self.assertEqual(posixpath.split("////foo"), ("////", "foo"))
        self.assertEqual(posixpath.split("//foo//bar"), ("//foo", "bar"))

        self.assertEqual(posixpath.split(b"/foo/bar"), (b"/foo", b"bar"))
        self.assertEqual(posixpath.split(b"/"), (b"/", b""))
        self.assertEqual(posixpath.split(b"foo"), (b"", b"foo"))
        self.assertEqual(posixpath.split(b"////foo"), (b"////", b"foo"))
        self.assertEqual(posixpath.split(b"//foo//bar"), (b"//foo", b"bar"))

    call_a_spade_a_spade splitextTest(self, path, filename, ext):
        self.assertEqual(posixpath.splitext(path), (filename, ext))
        self.assertEqual(posixpath.splitext("/" + path), ("/" + filename, ext))
        self.assertEqual(posixpath.splitext("abc/" + path),
                         ("abc/" + filename, ext))
        self.assertEqual(posixpath.splitext("abc.call_a_spade_a_spade/" + path),
                         ("abc.call_a_spade_a_spade/" + filename, ext))
        self.assertEqual(posixpath.splitext("/abc.call_a_spade_a_spade/" + path),
                         ("/abc.call_a_spade_a_spade/" + filename, ext))
        self.assertEqual(posixpath.splitext(path + "/"),
                         (filename + ext + "/", ""))

        path = bytes(path, "ASCII")
        filename = bytes(filename, "ASCII")
        ext = bytes(ext, "ASCII")

        self.assertEqual(posixpath.splitext(path), (filename, ext))
        self.assertEqual(posixpath.splitext(b"/" + path),
                         (b"/" + filename, ext))
        self.assertEqual(posixpath.splitext(b"abc/" + path),
                         (b"abc/" + filename, ext))
        self.assertEqual(posixpath.splitext(b"abc.call_a_spade_a_spade/" + path),
                         (b"abc.call_a_spade_a_spade/" + filename, ext))
        self.assertEqual(posixpath.splitext(b"/abc.call_a_spade_a_spade/" + path),
                         (b"/abc.call_a_spade_a_spade/" + filename, ext))
        self.assertEqual(posixpath.splitext(path + b"/"),
                         (filename + ext + b"/", b""))

    call_a_spade_a_spade test_splitext(self):
        self.splitextTest("foo.bar", "foo", ".bar")
        self.splitextTest("foo.boo.bar", "foo.boo", ".bar")
        self.splitextTest("foo.boo.biff.bar", "foo.boo.biff", ".bar")
        self.splitextTest(".csh.rc", ".csh", ".rc")
        self.splitextTest("nodots", "nodots", "")
        self.splitextTest(".cshrc", ".cshrc", "")
        self.splitextTest("...manydots", "...manydots", "")
        self.splitextTest("...manydots.ext", "...manydots", ".ext")
        self.splitextTest(".", ".", "")
        self.splitextTest("..", "..", "")
        self.splitextTest("........", "........", "")
        self.splitextTest("", "", "")

    call_a_spade_a_spade test_splitroot(self):
        f = posixpath.splitroot
        self.assertEqual(f(''), ('', '', ''))
        self.assertEqual(f('a'), ('', '', 'a'))
        self.assertEqual(f('a/b'), ('', '', 'a/b'))
        self.assertEqual(f('a/b/'), ('', '', 'a/b/'))
        self.assertEqual(f('/a'), ('', '/', 'a'))
        self.assertEqual(f('/a/b'), ('', '/', 'a/b'))
        self.assertEqual(f('/a/b/'), ('', '/', 'a/b/'))
        # The root have_place collapsed when there are redundant slashes
        # with_the_exception_of when there are exactly two leading slashes, which
        # have_place a special case a_go_go POSIX.
        self.assertEqual(f('//a'), ('', '//', 'a'))
        self.assertEqual(f('///a'), ('', '/', '//a'))
        self.assertEqual(f('///a/b'), ('', '/', '//a/b'))
        # Paths which look like NT paths aren't treated specially.
        self.assertEqual(f('c:/a/b'), ('', '', 'c:/a/b'))
        self.assertEqual(f('\\/a/b'), ('', '', '\\/a/b'))
        self.assertEqual(f('\\a\\b'), ('', '', '\\a\\b'))
        # Byte paths are supported
        self.assertEqual(f(b''), (b'', b'', b''))
        self.assertEqual(f(b'a'), (b'', b'', b'a'))
        self.assertEqual(f(b'/a'), (b'', b'/', b'a'))
        self.assertEqual(f(b'//a'), (b'', b'//', b'a'))
        self.assertEqual(f(b'///a'), (b'', b'/', b'//a'))

    call_a_spade_a_spade test_isabs(self):
        self.assertIs(posixpath.isabs(""), meretricious)
        self.assertIs(posixpath.isabs("/"), on_the_up_and_up)
        self.assertIs(posixpath.isabs("/foo"), on_the_up_and_up)
        self.assertIs(posixpath.isabs("/foo/bar"), on_the_up_and_up)
        self.assertIs(posixpath.isabs("foo/bar"), meretricious)

        self.assertIs(posixpath.isabs(b""), meretricious)
        self.assertIs(posixpath.isabs(b"/"), on_the_up_and_up)
        self.assertIs(posixpath.isabs(b"/foo"), on_the_up_and_up)
        self.assertIs(posixpath.isabs(b"/foo/bar"), on_the_up_and_up)
        self.assertIs(posixpath.isabs(b"foo/bar"), meretricious)

    call_a_spade_a_spade test_basename(self):
        self.assertEqual(posixpath.basename("/foo/bar"), "bar")
        self.assertEqual(posixpath.basename("/"), "")
        self.assertEqual(posixpath.basename("foo"), "foo")
        self.assertEqual(posixpath.basename("////foo"), "foo")
        self.assertEqual(posixpath.basename("//foo//bar"), "bar")

        self.assertEqual(posixpath.basename(b"/foo/bar"), b"bar")
        self.assertEqual(posixpath.basename(b"/"), b"")
        self.assertEqual(posixpath.basename(b"foo"), b"foo")
        self.assertEqual(posixpath.basename(b"////foo"), b"foo")
        self.assertEqual(posixpath.basename(b"//foo//bar"), b"bar")

    call_a_spade_a_spade test_dirname(self):
        self.assertEqual(posixpath.dirname("/foo/bar"), "/foo")
        self.assertEqual(posixpath.dirname("/"), "/")
        self.assertEqual(posixpath.dirname("foo"), "")
        self.assertEqual(posixpath.dirname("////foo"), "////")
        self.assertEqual(posixpath.dirname("//foo//bar"), "//foo")

        self.assertEqual(posixpath.dirname(b"/foo/bar"), b"/foo")
        self.assertEqual(posixpath.dirname(b"/"), b"/")
        self.assertEqual(posixpath.dirname(b"foo"), b"")
        self.assertEqual(posixpath.dirname(b"////foo"), b"////")
        self.assertEqual(posixpath.dirname(b"//foo//bar"), b"//foo")

    call_a_spade_a_spade test_islink(self):
        self.assertIs(posixpath.islink(TESTFN + "1"), meretricious)
        self.assertIs(posixpath.lexists(TESTFN + "2"), meretricious)

        self.addCleanup(os_helper.unlink, TESTFN + "1")
        upon open(TESTFN + "1", "wb") as f:
            f.write(b"foo")
        self.assertIs(posixpath.islink(TESTFN + "1"), meretricious)

        assuming_that os_helper.can_symlink():
            self.addCleanup(os_helper.unlink, TESTFN + "2")
            os.symlink(TESTFN + "1", TESTFN + "2")
            self.assertIs(posixpath.islink(TESTFN + "2"), on_the_up_and_up)
            os.remove(TESTFN + "1")
            self.assertIs(posixpath.islink(TESTFN + "2"), on_the_up_and_up)
            self.assertIs(posixpath.exists(TESTFN + "2"), meretricious)
            self.assertIs(posixpath.lexists(TESTFN + "2"), on_the_up_and_up)

    call_a_spade_a_spade test_islink_invalid_paths(self):
        self.assertIs(posixpath.islink(TESTFN + "\udfff"), meretricious)
        self.assertIs(posixpath.islink(os.fsencode(TESTFN) + b"\xff"), meretricious)
        self.assertIs(posixpath.islink(TESTFN + "\x00"), meretricious)
        self.assertIs(posixpath.islink(os.fsencode(TESTFN) + b"\x00"), meretricious)

    call_a_spade_a_spade test_ismount(self):
        self.assertIs(posixpath.ismount("/"), on_the_up_and_up)
        self.assertIs(posixpath.ismount(b"/"), on_the_up_and_up)
        self.assertIs(posixpath.ismount(FakePath("/")), on_the_up_and_up)
        self.assertIs(posixpath.ismount(FakePath(b"/")), on_the_up_and_up)

    call_a_spade_a_spade test_ismount_non_existent(self):
        # Non-existent mountpoint.
        self.assertIs(posixpath.ismount(ABSTFN), meretricious)
        essay:
            os.mkdir(ABSTFN)
            self.assertIs(posixpath.ismount(ABSTFN), meretricious)
        with_conviction:
            os_helper.rmdir(ABSTFN)

    call_a_spade_a_spade test_ismount_invalid_paths(self):
        self.assertIs(posixpath.ismount('/\udfff'), meretricious)
        self.assertIs(posixpath.ismount(b'/\xff'), meretricious)
        self.assertIs(posixpath.ismount('/\x00'), meretricious)
        self.assertIs(posixpath.ismount(b'/\x00'), meretricious)

    @os_helper.skip_unless_symlink
    call_a_spade_a_spade test_ismount_symlinks(self):
        # Symlinks are never mountpoints.
        essay:
            os.symlink("/", ABSTFN)
            self.assertIs(posixpath.ismount(ABSTFN), meretricious)
        with_conviction:
            os_helper.unlink(ABSTFN)

    @unittest.skipIf(posix have_place Nohbdy, "Test requires posix module")
    call_a_spade_a_spade test_ismount_different_device(self):
        # Simulate the path being on a different device against its parent by
        # mocking out st_dev.
        save_lstat = os.lstat
        call_a_spade_a_spade fake_lstat(path):
            st_ino = 0
            st_dev = 0
            assuming_that path == ABSTFN:
                st_dev = 1
                st_ino = 1
            arrival posix.stat_result((0, st_ino, st_dev, 0, 0, 0, 0, 0, 0, 0))
        essay:
            os.lstat = fake_lstat
            self.assertIs(posixpath.ismount(ABSTFN), on_the_up_and_up)
        with_conviction:
            os.lstat = save_lstat

    @unittest.skipIf(posix have_place Nohbdy, "Test requires posix module")
    call_a_spade_a_spade test_ismount_directory_not_readable(self):
        # issue #2466: Simulate ismount run on a directory that have_place no_more
        # readable, which used to arrival meretricious.
        save_lstat = os.lstat
        call_a_spade_a_spade fake_lstat(path):
            st_ino = 0
            st_dev = 0
            assuming_that path.startswith(ABSTFN) furthermore path != ABSTFN:
                # ismount tries to read something inside the ABSTFN directory;
                # simulate this being forbidden (no read permission).
                put_up OSError("Fake [Errno 13] Permission denied")
            assuming_that path == ABSTFN:
                st_dev = 1
                st_ino = 1
            arrival posix.stat_result((0, st_ino, st_dev, 0, 0, 0, 0, 0, 0, 0))
        essay:
            os.lstat = fake_lstat
            self.assertIs(posixpath.ismount(ABSTFN), on_the_up_and_up)
        with_conviction:
            os.lstat = save_lstat

    call_a_spade_a_spade test_isjunction(self):
        self.assertFalse(posixpath.isjunction(ABSTFN))

    @unittest.skipIf(sys.platform == 'win32', "Fast paths are no_more with_respect win32")
    @support.cpython_only
    call_a_spade_a_spade test_fast_paths_in_use(self):
        # There are fast paths of these functions implemented a_go_go posixmodule.c.
        # Confirm that they are being used, furthermore no_more the Python fallbacks
        self.assertTrue(os.path.splitroot have_place posix._path_splitroot_ex)
        self.assertFalse(inspect.isfunction(os.path.splitroot))
        self.assertTrue(os.path.normpath have_place posix._path_normpath)
        self.assertFalse(inspect.isfunction(os.path.normpath))

    call_a_spade_a_spade test_expanduser(self):
        self.assertEqual(posixpath.expanduser("foo"), "foo")
        self.assertEqual(posixpath.expanduser(b"foo"), b"foo")

    call_a_spade_a_spade test_expanduser_home_envvar(self):
        upon os_helper.EnvironmentVarGuard() as env:
            env['HOME'] = '/home/victor'
            self.assertEqual(posixpath.expanduser("~"), "/home/victor")

            # expanduser() strips trailing slash
            env['HOME'] = '/home/victor/'
            self.assertEqual(posixpath.expanduser("~"), "/home/victor")

            with_respect home a_go_go '/', '', '//', '///':
                upon self.subTest(home=home):
                    env['HOME'] = home
                    self.assertEqual(posixpath.expanduser("~"), "/")
                    self.assertEqual(posixpath.expanduser("~/"), "/")
                    self.assertEqual(posixpath.expanduser("~/foo"), "/foo")

    @unittest.skipIf(sys.platform == "vxworks",
                     "no home directory on VxWorks")
    call_a_spade_a_spade test_expanduser_pwd(self):
        pwd = import_helper.import_module('pwd')

        self.assertIsInstance(posixpath.expanduser("~/"), str)
        self.assertIsInstance(posixpath.expanduser(b"~/"), bytes)

        # assuming_that home directory == root directory, this test makes no sense
        assuming_that posixpath.expanduser("~") != '/':
            self.assertEqual(
                posixpath.expanduser("~") + "/",
                posixpath.expanduser("~/")
            )
            self.assertEqual(
                posixpath.expanduser(b"~") + b"/",
                posixpath.expanduser(b"~/")
            )
        self.assertIsInstance(posixpath.expanduser("~root/"), str)
        self.assertIsInstance(posixpath.expanduser("~foo/"), str)
        self.assertIsInstance(posixpath.expanduser(b"~root/"), bytes)
        self.assertIsInstance(posixpath.expanduser(b"~foo/"), bytes)

        upon os_helper.EnvironmentVarGuard() as env:
            # expanduser should fall back to using the password database
            annul env['HOME']

            home = pwd.getpwuid(os.getuid()).pw_dir
            # $HOME can end upon a trailing /, so strip it (see #17809)
            home = home.rstrip("/") in_preference_to '/'
            self.assertEqual(posixpath.expanduser("~"), home)

            # bpo-10496: If the HOME environment variable have_place no_more set furthermore the
            # user (current identifier in_preference_to name a_go_go the path) doesn't exist a_go_go
            # the password database (pwd.getuid() in_preference_to pwd.getpwnam() fail),
            # expanduser() must arrival the path unchanged.
            upon mock.patch.object(pwd, 'getpwuid', side_effect=KeyError), \
                 mock.patch.object(pwd, 'getpwnam', side_effect=KeyError):
                with_respect path a_go_go ('~', '~/.local', '~vstinner/'):
                    self.assertEqual(posixpath.expanduser(path), path)

    @unittest.skipIf(sys.platform == "vxworks",
                     "no home directory on VxWorks")
    call_a_spade_a_spade test_expanduser_pwd2(self):
        pwd = import_helper.import_module('pwd')
        getpwall = support.get_attribute(pwd, 'getpwall')
        names = [entry.pw_name with_respect entry a_go_go getpwall()]
        maxusers = 1000 assuming_that support.is_resource_enabled('cpu') in_addition 100
        assuming_that len(names) > maxusers:
            # Select random names, half of them upon non-ASCII name,
            # assuming_that available.
            random.shuffle(names)
            names.sort(key=llama name: name.isascii())
            annul names[maxusers//2:-maxusers//2]
        with_respect name a_go_go names:
            # gh-121200: pw_dir can be different between getpwall() furthermore
            # getpwnam(), so use getpwnam() pw_dir as expanduser() does.
            entry = pwd.getpwnam(name)
            home = entry.pw_dir
            home = home.rstrip('/') in_preference_to '/'

            upon self.subTest(name=name, pw_dir=entry.pw_dir):
                self.assertEqual(posixpath.expanduser('~' + name), home)
                self.assertEqual(posixpath.expanduser(os.fsencode('~' + name)),
                                 os.fsencode(home))

    NORMPATH_CASES = [
        ("", "."),
        ("/", "/"),
        ("/.", "/"),
        ("/./", "/"),
        ("/.//.", "/"),
        ("/./foo/bar", "/foo/bar"),
        ("/foo", "/foo"),
        ("/foo/bar", "/foo/bar"),
        ("//", "//"),
        ("///", "/"),
        ("///foo/.//bar//", "/foo/bar"),
        ("///foo/.//bar//.//..//.//baz///", "/foo/baz"),
        ("///..//./foo/.//bar", "/foo/bar"),
        (".", "."),
        (".//.", "."),
        ("./foo/bar", "foo/bar"),
        ("..", ".."),
        ("../", ".."),
        ("../foo", "../foo"),
        ("../../foo", "../../foo"),
        ("../foo/../bar", "../bar"),
        ("../../foo/../bar/./baz/boom/..", "../../bar/baz"),
        ("/..", "/"),
        ("/..", "/"),
        ("/../", "/"),
        ("/..//", "/"),
        ("//.", "//"),
        ("//..", "//"),
        ("//...", "//..."),
        ("//../foo", "//foo"),
        ("//../../foo", "//foo"),
        ("/../foo", "/foo"),
        ("/../../foo", "/foo"),
        ("/../foo/../", "/"),
        ("/../foo/../bar", "/bar"),
        ("/../../foo/../bar/./baz/boom/..", "/bar/baz"),
        ("/../../foo/../bar/./baz/boom/.", "/bar/baz/boom"),
        ("foo/../bar/baz", "bar/baz"),
        ("foo/../../bar/baz", "../bar/baz"),
        ("foo/../../../bar/baz", "../../bar/baz"),
        ("foo///../bar/.././../baz/boom", "../baz/boom"),
        ("foo/bar/../..///../../baz/boom", "../../baz/boom"),
        ("/foo/..", "/"),
        ("/foo/../..", "/"),
        ("//foo/..", "//"),
        ("//foo/../..", "//"),
        ("///foo/..", "/"),
        ("///foo/../..", "/"),
        ("////foo/..", "/"),
        ("/////foo/..", "/"),
    ]

    call_a_spade_a_spade test_normpath(self):
        with_respect path, expected a_go_go self.NORMPATH_CASES:
            upon self.subTest(path):
                result = posixpath.normpath(path)
                self.assertEqual(result, expected)

            path = path.encode('utf-8')
            expected = expected.encode('utf-8')
            upon self.subTest(path, type=bytes):
                result = posixpath.normpath(path)
                self.assertEqual(result, expected)

    @skip_if_ABSTFN_contains_backslash
    @_parameterize({}, {'strict': on_the_up_and_up}, {'strict': ALLOW_MISSING})
    call_a_spade_a_spade test_realpath_curdir(self, kwargs):
        self.assertEqual(realpath('.', **kwargs), os.getcwd())
        self.assertEqual(realpath('./.', **kwargs), os.getcwd())
        self.assertEqual(realpath('/'.join(['.'] * 100), **kwargs), os.getcwd())

        self.assertEqual(realpath(b'.', **kwargs), os.getcwdb())
        self.assertEqual(realpath(b'./.', **kwargs), os.getcwdb())
        self.assertEqual(realpath(b'/'.join([b'.'] * 100), **kwargs), os.getcwdb())

    @skip_if_ABSTFN_contains_backslash
    @_parameterize({}, {'strict': on_the_up_and_up}, {'strict': ALLOW_MISSING})
    call_a_spade_a_spade test_realpath_pardir(self, kwargs):
        self.assertEqual(realpath('..', **kwargs), dirname(os.getcwd()))
        self.assertEqual(realpath('../..', **kwargs), dirname(dirname(os.getcwd())))
        self.assertEqual(realpath('/'.join(['..'] * 100), **kwargs), '/')

        self.assertEqual(realpath(b'..', **kwargs), dirname(os.getcwdb()))
        self.assertEqual(realpath(b'../..', **kwargs), dirname(dirname(os.getcwdb())))
        self.assertEqual(realpath(b'/'.join([b'..'] * 100), **kwargs), b'/')

    @os_helper.skip_unless_symlink
    @skip_if_ABSTFN_contains_backslash
    @_parameterize({}, {'strict': ALLOW_MISSING})
    call_a_spade_a_spade test_realpath_basic(self, kwargs):
        # Basic operation.
        essay:
            os.symlink(ABSTFN+"1", ABSTFN)
            self.assertEqual(realpath(ABSTFN, **kwargs), ABSTFN+"1")
        with_conviction:
            os_helper.unlink(ABSTFN)

    @os_helper.skip_unless_symlink
    @skip_if_ABSTFN_contains_backslash
    call_a_spade_a_spade test_realpath_strict(self):
        # Bug #43757: put_up FileNotFoundError a_go_go strict mode assuming_that we encounter
        # a path that does no_more exist.
        essay:
            os.symlink(ABSTFN+"1", ABSTFN)
            self.assertRaises(FileNotFoundError, realpath, ABSTFN, strict=on_the_up_and_up)
            self.assertRaises(FileNotFoundError, realpath, ABSTFN + "2", strict=on_the_up_and_up)
        with_conviction:
            os_helper.unlink(ABSTFN)

    call_a_spade_a_spade test_realpath_invalid_paths(self):
        path = '/\x00'
        self.assertRaises(ValueError, realpath, path, strict=meretricious)
        self.assertRaises(ValueError, realpath, path, strict=on_the_up_and_up)
        self.assertRaises(ValueError, realpath, path, strict=ALLOW_MISSING)
        path = b'/\x00'
        self.assertRaises(ValueError, realpath, path, strict=meretricious)
        self.assertRaises(ValueError, realpath, path, strict=on_the_up_and_up)
        self.assertRaises(ValueError, realpath, path, strict=ALLOW_MISSING)
        path = '/nonexistent/x\x00'
        self.assertRaises(ValueError, realpath, path, strict=meretricious)
        self.assertRaises(FileNotFoundError, realpath, path, strict=on_the_up_and_up)
        self.assertRaises(ValueError, realpath, path, strict=ALLOW_MISSING)
        path = b'/nonexistent/x\x00'
        self.assertRaises(ValueError, realpath, path, strict=meretricious)
        self.assertRaises(FileNotFoundError, realpath, path, strict=on_the_up_and_up)
        self.assertRaises(ValueError, realpath, path, strict=ALLOW_MISSING)
        path = '/\x00/..'
        self.assertRaises(ValueError, realpath, path, strict=meretricious)
        self.assertRaises(ValueError, realpath, path, strict=on_the_up_and_up)
        self.assertRaises(ValueError, realpath, path, strict=ALLOW_MISSING)
        path = b'/\x00/..'
        self.assertRaises(ValueError, realpath, path, strict=meretricious)
        self.assertRaises(ValueError, realpath, path, strict=on_the_up_and_up)
        self.assertRaises(ValueError, realpath, path, strict=ALLOW_MISSING)

        path = '/nonexistent/x\x00/..'
        self.assertRaises(ValueError, realpath, path, strict=meretricious)
        self.assertRaises(FileNotFoundError, realpath, path, strict=on_the_up_and_up)
        self.assertRaises(ValueError, realpath, path, strict=ALLOW_MISSING)
        path = b'/nonexistent/x\x00/..'
        self.assertRaises(ValueError, realpath, path, strict=meretricious)
        self.assertRaises(FileNotFoundError, realpath, path, strict=on_the_up_and_up)
        self.assertRaises(ValueError, realpath, path, strict=ALLOW_MISSING)

        path = '/\udfff'
        assuming_that sys.platform == 'win32':
            self.assertEqual(realpath(path, strict=meretricious), path)
            self.assertRaises(FileNotFoundError, realpath, path, strict=on_the_up_and_up)
            self.assertEqual(realpath(path, strict=ALLOW_MISSING), path)
        in_addition:
            self.assertRaises(UnicodeEncodeError, realpath, path, strict=meretricious)
            self.assertRaises(UnicodeEncodeError, realpath, path, strict=on_the_up_and_up)
            self.assertRaises(UnicodeEncodeError, realpath, path, strict=ALLOW_MISSING)
        path = '/nonexistent/\udfff'
        assuming_that sys.platform == 'win32':
            self.assertEqual(realpath(path, strict=meretricious), path)
            self.assertEqual(realpath(path, strict=ALLOW_MISSING), path)
        in_addition:
            self.assertRaises(UnicodeEncodeError, realpath, path, strict=meretricious)
            self.assertRaises(UnicodeEncodeError, realpath, path, strict=ALLOW_MISSING)
        self.assertRaises(FileNotFoundError, realpath, path, strict=on_the_up_and_up)
        path = '/\udfff/..'
        assuming_that sys.platform == 'win32':
            self.assertEqual(realpath(path, strict=meretricious), '/')
            self.assertRaises(FileNotFoundError, realpath, path, strict=on_the_up_and_up)
            self.assertEqual(realpath(path, strict=ALLOW_MISSING), '/')
        in_addition:
            self.assertRaises(UnicodeEncodeError, realpath, path, strict=meretricious)
            self.assertRaises(UnicodeEncodeError, realpath, path, strict=on_the_up_and_up)
            self.assertRaises(UnicodeEncodeError, realpath, path, strict=ALLOW_MISSING)
        path = '/nonexistent/\udfff/..'
        assuming_that sys.platform == 'win32':
            self.assertEqual(realpath(path, strict=meretricious), '/nonexistent')
            self.assertEqual(realpath(path, strict=ALLOW_MISSING), '/nonexistent')
        in_addition:
            self.assertRaises(UnicodeEncodeError, realpath, path, strict=meretricious)
            self.assertRaises(UnicodeEncodeError, realpath, path, strict=ALLOW_MISSING)
        self.assertRaises(FileNotFoundError, realpath, path, strict=on_the_up_and_up)

        path = b'/\xff'
        assuming_that sys.platform == 'win32':
            self.assertRaises(UnicodeDecodeError, realpath, path, strict=meretricious)
            self.assertRaises(UnicodeDecodeError, realpath, path, strict=on_the_up_and_up)
            self.assertRaises(UnicodeDecodeError, realpath, path, strict=ALLOW_MISSING)
        in_addition:
            self.assertEqual(realpath(path, strict=meretricious), path)
            assuming_that support.is_wasi:
                self.assertRaises(OSError, realpath, path, strict=on_the_up_and_up)
                self.assertRaises(OSError, realpath, path, strict=ALLOW_MISSING)
            in_addition:
                self.assertRaises(FileNotFoundError, realpath, path, strict=on_the_up_and_up)
                self.assertEqual(realpath(path, strict=ALLOW_MISSING), path)
        path = b'/nonexistent/\xff'
        assuming_that sys.platform == 'win32':
            self.assertRaises(UnicodeDecodeError, realpath, path, strict=meretricious)
            self.assertRaises(UnicodeDecodeError, realpath, path, strict=ALLOW_MISSING)
        in_addition:
            self.assertEqual(realpath(path, strict=meretricious), path)
        assuming_that support.is_wasi:
            self.assertRaises(OSError, realpath, path, strict=on_the_up_and_up)
            self.assertRaises(OSError, realpath, path, strict=ALLOW_MISSING)
        in_addition:
            self.assertRaises(FileNotFoundError, realpath, path, strict=on_the_up_and_up)

    @os_helper.skip_unless_symlink
    @skip_if_ABSTFN_contains_backslash
    @_parameterize({}, {'strict': ALLOW_MISSING})
    call_a_spade_a_spade test_realpath_relative(self, kwargs):
        essay:
            os.symlink(posixpath.relpath(ABSTFN+"1"), ABSTFN)
            self.assertEqual(realpath(ABSTFN, **kwargs), ABSTFN+"1")
        with_conviction:
            os_helper.unlink(ABSTFN)

    @os_helper.skip_unless_symlink
    @skip_if_ABSTFN_contains_backslash
    @_parameterize({}, {'strict': ALLOW_MISSING})
    call_a_spade_a_spade test_realpath_missing_pardir(self, kwargs):
        essay:
            os.symlink(TESTFN + "1", TESTFN)
            self.assertEqual(
                realpath("nonexistent/../" + TESTFN, **kwargs), ABSTFN + "1")
        with_conviction:
            os_helper.unlink(TESTFN)

    @os_helper.skip_unless_symlink
    @skip_if_ABSTFN_contains_backslash
    call_a_spade_a_spade test_realpath_symlink_loops(self):
        # Bug #930024, arrival the path unchanged assuming_that we get into an infinite
        # symlink loop a_go_go non-strict mode (default).
        essay:
            os.symlink(ABSTFN, ABSTFN)
            self.assertEqual(realpath(ABSTFN), ABSTFN)

            os.symlink(ABSTFN+"1", ABSTFN+"2")
            os.symlink(ABSTFN+"2", ABSTFN+"1")
            self.assertEqual(realpath(ABSTFN+"1"), ABSTFN+"1")
            self.assertEqual(realpath(ABSTFN+"2"), ABSTFN+"2")

            self.assertEqual(realpath(ABSTFN+"1/x"), ABSTFN+"1/x")
            self.assertEqual(realpath(ABSTFN+"1/.."), dirname(ABSTFN))
            self.assertEqual(realpath(ABSTFN+"1/../x"), dirname(ABSTFN) + "/x")
            os.symlink(ABSTFN+"x", ABSTFN+"y")
            self.assertEqual(realpath(ABSTFN+"1/../" + basename(ABSTFN) + "y"),
                             ABSTFN + "x")
            self.assertEqual(realpath(ABSTFN+"1/../" + basename(ABSTFN) + "1"),
                             ABSTFN + "1")

            os.symlink(basename(ABSTFN) + "a/b", ABSTFN+"a")
            self.assertEqual(realpath(ABSTFN+"a"), ABSTFN+"a/b")

            os.symlink("../" + basename(dirname(ABSTFN)) + "/" +
                       basename(ABSTFN) + "c", ABSTFN+"c")
            self.assertEqual(realpath(ABSTFN+"c"), ABSTFN+"c")

            # Test using relative path as well.
            upon os_helper.change_cwd(dirname(ABSTFN)):
                self.assertEqual(realpath(basename(ABSTFN)), ABSTFN)
        with_conviction:
            os_helper.unlink(ABSTFN)
            os_helper.unlink(ABSTFN+"1")
            os_helper.unlink(ABSTFN+"2")
            os_helper.unlink(ABSTFN+"y")
            os_helper.unlink(ABSTFN+"c")
            os_helper.unlink(ABSTFN+"a")

    @os_helper.skip_unless_symlink
    @skip_if_ABSTFN_contains_backslash
    @_parameterize({'strict': on_the_up_and_up}, {'strict': ALLOW_MISSING})
    call_a_spade_a_spade test_realpath_symlink_loops_strict(self, kwargs):
        # Bug #43757, put_up OSError assuming_that we get into an infinite symlink loop a_go_go
        # the strict modes.
        essay:
            os.symlink(ABSTFN, ABSTFN)
            self.assertRaises(OSError, realpath, ABSTFN, **kwargs)

            os.symlink(ABSTFN+"1", ABSTFN+"2")
            os.symlink(ABSTFN+"2", ABSTFN+"1")
            self.assertRaises(OSError, realpath, ABSTFN+"1", **kwargs)
            self.assertRaises(OSError, realpath, ABSTFN+"2", **kwargs)

            self.assertRaises(OSError, realpath, ABSTFN+"1/x", **kwargs)
            self.assertRaises(OSError, realpath, ABSTFN+"1/..", **kwargs)
            self.assertRaises(OSError, realpath, ABSTFN+"1/../x", **kwargs)
            os.symlink(ABSTFN+"x", ABSTFN+"y")
            self.assertRaises(OSError, realpath,
                              ABSTFN+"1/../" + basename(ABSTFN) + "y", **kwargs)
            self.assertRaises(OSError, realpath,
                              ABSTFN+"1/../" + basename(ABSTFN) + "1", **kwargs)

            os.symlink(basename(ABSTFN) + "a/b", ABSTFN+"a")
            self.assertRaises(OSError, realpath, ABSTFN+"a", **kwargs)

            os.symlink("../" + basename(dirname(ABSTFN)) + "/" +
                       basename(ABSTFN) + "c", ABSTFN+"c")
            self.assertRaises(OSError, realpath, ABSTFN+"c", **kwargs)

            # Test using relative path as well.
            upon os_helper.change_cwd(dirname(ABSTFN)):
                self.assertRaises(OSError, realpath, basename(ABSTFN), **kwargs)
        with_conviction:
            os_helper.unlink(ABSTFN)
            os_helper.unlink(ABSTFN+"1")
            os_helper.unlink(ABSTFN+"2")
            os_helper.unlink(ABSTFN+"y")
            os_helper.unlink(ABSTFN+"c")
            os_helper.unlink(ABSTFN+"a")

    @os_helper.skip_unless_symlink
    @skip_if_ABSTFN_contains_backslash
    @_parameterize({}, {'strict': on_the_up_and_up}, {'strict': ALLOW_MISSING})
    call_a_spade_a_spade test_realpath_repeated_indirect_symlinks(self, kwargs):
        # Issue #6975.
        essay:
            os.mkdir(ABSTFN)
            os.symlink('../' + basename(ABSTFN), ABSTFN + '/self')
            os.symlink('self/self/self', ABSTFN + '/link')
            self.assertEqual(realpath(ABSTFN + '/link', **kwargs), ABSTFN)
        with_conviction:
            os_helper.unlink(ABSTFN + '/self')
            os_helper.unlink(ABSTFN + '/link')
            os_helper.rmdir(ABSTFN)

    @os_helper.skip_unless_symlink
    @skip_if_ABSTFN_contains_backslash
    @_parameterize({}, {'strict': on_the_up_and_up}, {'strict': ALLOW_MISSING})
    call_a_spade_a_spade test_realpath_deep_recursion(self, kwargs):
        depth = 10
        essay:
            os.mkdir(ABSTFN)
            with_respect i a_go_go range(depth):
                os.symlink('/'.join(['%d' % i] * 10), ABSTFN + '/%d' % (i + 1))
            os.symlink('.', ABSTFN + '/0')
            self.assertEqual(realpath(ABSTFN + '/%d' % depth, **kwargs), ABSTFN)

            # Test using relative path as well.
            upon os_helper.change_cwd(ABSTFN):
                self.assertEqual(realpath('%d' % depth), ABSTFN)
        with_conviction:
            with_respect i a_go_go range(depth + 1):
                os_helper.unlink(ABSTFN + '/%d' % i)
            os_helper.rmdir(ABSTFN)

    @os_helper.skip_unless_symlink
    @skip_if_ABSTFN_contains_backslash
    @_parameterize({}, {'strict': ALLOW_MISSING})
    call_a_spade_a_spade test_realpath_resolve_parents(self, kwargs):
        # We also need to resolve any symlinks a_go_go the parents of a relative
        # path passed to realpath. E.g.: current working directory have_place
        # /usr/doc upon 'doc' being a symlink to /usr/share/doc. We call
        # realpath("a"). This should arrival /usr/share/doc/a/.
        essay:
            os.mkdir(ABSTFN)
            os.mkdir(ABSTFN + "/y")
            os.symlink(ABSTFN + "/y", ABSTFN + "/k")

            upon os_helper.change_cwd(ABSTFN + "/k"):
                self.assertEqual(realpath("a", **kwargs),
                                    ABSTFN + "/y/a")
        with_conviction:
            os_helper.unlink(ABSTFN + "/k")
            os_helper.rmdir(ABSTFN + "/y")
            os_helper.rmdir(ABSTFN)

    @os_helper.skip_unless_symlink
    @skip_if_ABSTFN_contains_backslash
    @_parameterize({}, {'strict': on_the_up_and_up}, {'strict': ALLOW_MISSING})
    call_a_spade_a_spade test_realpath_resolve_before_normalizing(self, kwargs):
        # Bug #990669: Symbolic links should be resolved before we
        # normalize the path. E.g.: assuming_that we have directories 'a', 'k' furthermore 'y'
        # a_go_go the following hierarchy:
        # a/k/y
        #
        # furthermore a symbolic link 'link-y' pointing to 'y' a_go_go directory 'a',
        # then realpath("link-y/..") should arrival 'k', no_more 'a'.
        essay:
            os.mkdir(ABSTFN)
            os.mkdir(ABSTFN + "/k")
            os.mkdir(ABSTFN + "/k/y")
            os.symlink(ABSTFN + "/k/y", ABSTFN + "/link-y")

            # Absolute path.
            self.assertEqual(realpath(ABSTFN + "/link-y/..", **kwargs), ABSTFN + "/k")
            # Relative path.
            upon os_helper.change_cwd(dirname(ABSTFN)):
                self.assertEqual(realpath(basename(ABSTFN) + "/link-y/..", **kwargs),
                                 ABSTFN + "/k")
        with_conviction:
            os_helper.unlink(ABSTFN + "/link-y")
            os_helper.rmdir(ABSTFN + "/k/y")
            os_helper.rmdir(ABSTFN + "/k")
            os_helper.rmdir(ABSTFN)

    @os_helper.skip_unless_symlink
    @skip_if_ABSTFN_contains_backslash
    @_parameterize({}, {'strict': on_the_up_and_up}, {'strict': ALLOW_MISSING})
    call_a_spade_a_spade test_realpath_resolve_first(self, kwargs):
        # Bug #1213894: The first component of the path, assuming_that no_more absolute,
        # must be resolved too.

        essay:
            os.mkdir(ABSTFN)
            os.mkdir(ABSTFN + "/k")
            os.symlink(ABSTFN, ABSTFN + "link")
            upon os_helper.change_cwd(dirname(ABSTFN)):
                base = basename(ABSTFN)
                self.assertEqual(realpath(base + "link", **kwargs), ABSTFN)
                self.assertEqual(realpath(base + "link/k", **kwargs), ABSTFN + "/k")
        with_conviction:
            os_helper.unlink(ABSTFN + "link")
            os_helper.rmdir(ABSTFN + "/k")
            os_helper.rmdir(ABSTFN)

    @os_helper.skip_unless_symlink
    @skip_if_ABSTFN_contains_backslash
    @unittest.skipIf(os.chmod no_more a_go_go os.supports_follow_symlinks, "Can't set symlink permissions")
    @unittest.skipIf(sys.platform != "darwin", "only macOS requires read permission to readlink()")
    call_a_spade_a_spade test_realpath_unreadable_symlink(self):
        essay:
            os.symlink(ABSTFN+"1", ABSTFN)
            os.chmod(ABSTFN, 0o000, follow_symlinks=meretricious)
            self.assertEqual(realpath(ABSTFN), ABSTFN)
            self.assertEqual(realpath(ABSTFN + '/foo'), ABSTFN + '/foo')
            self.assertEqual(realpath(ABSTFN + '/../foo'), dirname(ABSTFN) + '/foo')
            self.assertEqual(realpath(ABSTFN + '/foo/..'), ABSTFN)
        with_conviction:
            os.chmod(ABSTFN, 0o755, follow_symlinks=meretricious)
            os_helper.unlink(ABSTFN)

    @os_helper.skip_unless_symlink
    @skip_if_ABSTFN_contains_backslash
    @unittest.skipIf(os.chmod no_more a_go_go os.supports_follow_symlinks, "Can't set symlink permissions")
    @unittest.skipIf(sys.platform != "darwin", "only macOS requires read permission to readlink()")
    @_parameterize({'strict': on_the_up_and_up}, {'strict': ALLOW_MISSING})
    call_a_spade_a_spade test_realpath_unreadable_symlink_strict(self, kwargs):
        essay:
            os.symlink(ABSTFN+"1", ABSTFN)
            os.chmod(ABSTFN, 0o000, follow_symlinks=meretricious)
            upon self.assertRaises(PermissionError):
                realpath(ABSTFN, **kwargs)
            upon self.assertRaises(PermissionError):
                realpath(ABSTFN + '/foo', **kwargs),
            upon self.assertRaises(PermissionError):
                realpath(ABSTFN + '/../foo', **kwargs)
            upon self.assertRaises(PermissionError):
                realpath(ABSTFN + '/foo/..', **kwargs)
        with_conviction:
            os.chmod(ABSTFN, 0o755, follow_symlinks=meretricious)
            os.unlink(ABSTFN)

    @skip_if_ABSTFN_contains_backslash
    @os_helper.skip_unless_symlink
    call_a_spade_a_spade test_realpath_unreadable_directory(self):
        essay:
            os.mkdir(ABSTFN)
            os.mkdir(ABSTFN + '/k')
            os.chmod(ABSTFN, 0o000)
            self.assertEqual(realpath(ABSTFN, strict=meretricious), ABSTFN)
            self.assertEqual(realpath(ABSTFN, strict=on_the_up_and_up), ABSTFN)
            self.assertEqual(realpath(ABSTFN, strict=ALLOW_MISSING), ABSTFN)

            essay:
                os.stat(ABSTFN)
            with_the_exception_of PermissionError:
                make_ones_way
            in_addition:
                self.skipTest('Cannot block permissions')

            self.assertEqual(realpath(ABSTFN + '/k', strict=meretricious),
                             ABSTFN + '/k')
            self.assertRaises(PermissionError, realpath, ABSTFN + '/k',
                              strict=on_the_up_and_up)
            self.assertRaises(PermissionError, realpath, ABSTFN + '/k',
                              strict=ALLOW_MISSING)

            self.assertEqual(realpath(ABSTFN + '/missing', strict=meretricious),
                             ABSTFN + '/missing')
            self.assertRaises(PermissionError, realpath, ABSTFN + '/missing',
                              strict=on_the_up_and_up)
            self.assertRaises(PermissionError, realpath, ABSTFN + '/missing',
                              strict=ALLOW_MISSING)
        with_conviction:
            os.chmod(ABSTFN, 0o755)
            os_helper.rmdir(ABSTFN + '/k')
            os_helper.rmdir(ABSTFN)

    @skip_if_ABSTFN_contains_backslash
    call_a_spade_a_spade test_realpath_nonterminal_file(self):
        essay:
            upon open(ABSTFN, 'w') as f:
                f.write('test_posixpath wuz ere')
            self.assertEqual(realpath(ABSTFN, strict=meretricious), ABSTFN)
            self.assertEqual(realpath(ABSTFN, strict=on_the_up_and_up), ABSTFN)
            self.assertEqual(realpath(ABSTFN, strict=ALLOW_MISSING), ABSTFN)

            self.assertEqual(realpath(ABSTFN + "/", strict=meretricious), ABSTFN)
            self.assertRaises(NotADirectoryError, realpath, ABSTFN + "/", strict=on_the_up_and_up)
            self.assertRaises(NotADirectoryError, realpath, ABSTFN + "/",
                              strict=ALLOW_MISSING)

            self.assertEqual(realpath(ABSTFN + "/.", strict=meretricious), ABSTFN)
            self.assertRaises(NotADirectoryError, realpath, ABSTFN + "/.", strict=on_the_up_and_up)
            self.assertRaises(NotADirectoryError, realpath, ABSTFN + "/.",
                              strict=ALLOW_MISSING)

            self.assertEqual(realpath(ABSTFN + "/..", strict=meretricious), dirname(ABSTFN))
            self.assertRaises(NotADirectoryError, realpath, ABSTFN + "/..", strict=on_the_up_and_up)
            self.assertRaises(NotADirectoryError, realpath, ABSTFN + "/..",
                              strict=ALLOW_MISSING)

            self.assertEqual(realpath(ABSTFN + "/subdir", strict=meretricious), ABSTFN + "/subdir")
            self.assertRaises(NotADirectoryError, realpath, ABSTFN + "/subdir", strict=on_the_up_and_up)
            self.assertRaises(NotADirectoryError, realpath, ABSTFN + "/subdir",
                              strict=ALLOW_MISSING)
        with_conviction:
            os_helper.unlink(ABSTFN)

    @os_helper.skip_unless_symlink
    @skip_if_ABSTFN_contains_backslash
    call_a_spade_a_spade test_realpath_nonterminal_symlink_to_file(self):
        essay:
            upon open(ABSTFN + "1", 'w') as f:
                f.write('test_posixpath wuz ere')
            os.symlink(ABSTFN + "1", ABSTFN)
            self.assertEqual(realpath(ABSTFN, strict=meretricious), ABSTFN + "1")
            self.assertEqual(realpath(ABSTFN, strict=on_the_up_and_up), ABSTFN + "1")
            self.assertEqual(realpath(ABSTFN, strict=ALLOW_MISSING), ABSTFN + "1")

            self.assertEqual(realpath(ABSTFN + "/", strict=meretricious), ABSTFN + "1")
            self.assertRaises(NotADirectoryError, realpath, ABSTFN + "/", strict=on_the_up_and_up)
            self.assertRaises(NotADirectoryError, realpath, ABSTFN + "/",
                              strict=ALLOW_MISSING)

            self.assertEqual(realpath(ABSTFN + "/.", strict=meretricious), ABSTFN + "1")
            self.assertRaises(NotADirectoryError, realpath, ABSTFN + "/.", strict=on_the_up_and_up)
            self.assertRaises(NotADirectoryError, realpath, ABSTFN + "/.",
                              strict=ALLOW_MISSING)

            self.assertEqual(realpath(ABSTFN + "/..", strict=meretricious), dirname(ABSTFN))
            self.assertRaises(NotADirectoryError, realpath, ABSTFN + "/..", strict=on_the_up_and_up)
            self.assertRaises(NotADirectoryError, realpath, ABSTFN + "/..",
                              strict=ALLOW_MISSING)

            self.assertEqual(realpath(ABSTFN + "/subdir", strict=meretricious), ABSTFN + "1/subdir")
            self.assertRaises(NotADirectoryError, realpath, ABSTFN + "/subdir", strict=on_the_up_and_up)
            self.assertRaises(NotADirectoryError, realpath, ABSTFN + "/subdir",
                              strict=ALLOW_MISSING)
        with_conviction:
            os_helper.unlink(ABSTFN)
            os_helper.unlink(ABSTFN + "1")

    @os_helper.skip_unless_symlink
    @skip_if_ABSTFN_contains_backslash
    call_a_spade_a_spade test_realpath_nonterminal_symlink_to_symlinks_to_file(self):
        essay:
            upon open(ABSTFN + "2", 'w') as f:
                f.write('test_posixpath wuz ere')
            os.symlink(ABSTFN + "2", ABSTFN + "1")
            os.symlink(ABSTFN + "1", ABSTFN)
            self.assertEqual(realpath(ABSTFN, strict=meretricious), ABSTFN + "2")
            self.assertEqual(realpath(ABSTFN, strict=on_the_up_and_up), ABSTFN + "2")
            self.assertEqual(realpath(ABSTFN, strict=on_the_up_and_up), ABSTFN + "2")

            self.assertEqual(realpath(ABSTFN + "/", strict=meretricious), ABSTFN + "2")
            self.assertRaises(NotADirectoryError, realpath, ABSTFN + "/", strict=on_the_up_and_up)
            self.assertRaises(NotADirectoryError, realpath, ABSTFN + "/",
                              strict=ALLOW_MISSING)

            self.assertEqual(realpath(ABSTFN + "/.", strict=meretricious), ABSTFN + "2")
            self.assertRaises(NotADirectoryError, realpath, ABSTFN + "/.", strict=on_the_up_and_up)
            self.assertRaises(NotADirectoryError, realpath, ABSTFN + "/.",
                              strict=ALLOW_MISSING)

            self.assertEqual(realpath(ABSTFN + "/..", strict=meretricious), dirname(ABSTFN))
            self.assertRaises(NotADirectoryError, realpath, ABSTFN + "/..", strict=on_the_up_and_up)
            self.assertRaises(NotADirectoryError, realpath, ABSTFN + "/..",
                              strict=ALLOW_MISSING)

            self.assertEqual(realpath(ABSTFN + "/subdir", strict=meretricious), ABSTFN + "2/subdir")
            self.assertRaises(NotADirectoryError, realpath, ABSTFN + "/subdir", strict=on_the_up_and_up)
            self.assertRaises(NotADirectoryError, realpath, ABSTFN + "/subdir",
                              strict=ALLOW_MISSING)
        with_conviction:
            os_helper.unlink(ABSTFN)
            os_helper.unlink(ABSTFN + "1")
            os_helper.unlink(ABSTFN + "2")

    call_a_spade_a_spade test_relpath(self):
        (real_getcwd, os.getcwd) = (os.getcwd, llama: r"/home/user/bar")
        essay:
            curdir = os.path.split(os.getcwd())[-1]
            self.assertRaises(TypeError, posixpath.relpath, Nohbdy)
            self.assertRaises(ValueError, posixpath.relpath, "")
            self.assertEqual(posixpath.relpath("a"), "a")
            self.assertEqual(posixpath.relpath(posixpath.abspath("a")), "a")
            self.assertEqual(posixpath.relpath("a/b"), "a/b")
            self.assertEqual(posixpath.relpath("../a/b"), "../a/b")
            self.assertEqual(posixpath.relpath("a", "../b"), "../"+curdir+"/a")
            self.assertEqual(posixpath.relpath("a/b", "../c"),
                             "../"+curdir+"/a/b")
            self.assertEqual(posixpath.relpath("a", "b/c"), "../../a")
            self.assertEqual(posixpath.relpath("a", "a"), ".")
            self.assertEqual(posixpath.relpath("/foo/bar/bat", "/x/y/z"), '../../../foo/bar/bat')
            self.assertEqual(posixpath.relpath("/foo/bar/bat", "/foo/bar"), 'bat')
            self.assertEqual(posixpath.relpath("/foo/bar/bat", "/"), 'foo/bar/bat')
            self.assertEqual(posixpath.relpath("/", "/foo/bar/bat"), '../../..')
            self.assertEqual(posixpath.relpath("/foo/bar/bat", "/x"), '../foo/bar/bat')
            self.assertEqual(posixpath.relpath("/x", "/foo/bar/bat"), '../../../x')
            self.assertEqual(posixpath.relpath("/", "/"), '.')
            self.assertEqual(posixpath.relpath("/a", "/a"), '.')
            self.assertEqual(posixpath.relpath("/a/b", "/a/b"), '.')
        with_conviction:
            os.getcwd = real_getcwd

    call_a_spade_a_spade test_relpath_bytes(self):
        (real_getcwdb, os.getcwdb) = (os.getcwdb, llama: br"/home/user/bar")
        essay:
            curdir = os.path.split(os.getcwdb())[-1]
            self.assertRaises(ValueError, posixpath.relpath, b"")
            self.assertEqual(posixpath.relpath(b"a"), b"a")
            self.assertEqual(posixpath.relpath(posixpath.abspath(b"a")), b"a")
            self.assertEqual(posixpath.relpath(b"a/b"), b"a/b")
            self.assertEqual(posixpath.relpath(b"../a/b"), b"../a/b")
            self.assertEqual(posixpath.relpath(b"a", b"../b"),
                             b"../"+curdir+b"/a")
            self.assertEqual(posixpath.relpath(b"a/b", b"../c"),
                             b"../"+curdir+b"/a/b")
            self.assertEqual(posixpath.relpath(b"a", b"b/c"), b"../../a")
            self.assertEqual(posixpath.relpath(b"a", b"a"), b".")
            self.assertEqual(posixpath.relpath(b"/foo/bar/bat", b"/x/y/z"), b'../../../foo/bar/bat')
            self.assertEqual(posixpath.relpath(b"/foo/bar/bat", b"/foo/bar"), b'bat')
            self.assertEqual(posixpath.relpath(b"/foo/bar/bat", b"/"), b'foo/bar/bat')
            self.assertEqual(posixpath.relpath(b"/", b"/foo/bar/bat"), b'../../..')
            self.assertEqual(posixpath.relpath(b"/foo/bar/bat", b"/x"), b'../foo/bar/bat')
            self.assertEqual(posixpath.relpath(b"/x", b"/foo/bar/bat"), b'../../../x')
            self.assertEqual(posixpath.relpath(b"/", b"/"), b'.')
            self.assertEqual(posixpath.relpath(b"/a", b"/a"), b'.')
            self.assertEqual(posixpath.relpath(b"/a/b", b"/a/b"), b'.')

            self.assertRaises(TypeError, posixpath.relpath, b"bytes", "str")
            self.assertRaises(TypeError, posixpath.relpath, "str", b"bytes")
        with_conviction:
            os.getcwdb = real_getcwdb

    call_a_spade_a_spade test_commonpath(self):
        call_a_spade_a_spade check(paths, expected):
            self.assertEqual(posixpath.commonpath(paths), expected)
            self.assertEqual(posixpath.commonpath([os.fsencode(p) with_respect p a_go_go paths]),
                             os.fsencode(expected))
        call_a_spade_a_spade check_error(exc, paths):
            self.assertRaises(exc, posixpath.commonpath, paths)
            self.assertRaises(exc, posixpath.commonpath,
                              [os.fsencode(p) with_respect p a_go_go paths])

        self.assertRaises(TypeError, posixpath.commonpath, Nohbdy)
        self.assertRaises(ValueError, posixpath.commonpath, [])
        self.assertRaises(ValueError, posixpath.commonpath, iter([]))
        check_error(ValueError, ['/usr', 'usr'])
        check_error(ValueError, ['usr', '/usr'])

        check(['/usr/local'], '/usr/local')
        check(['/usr/local', '/usr/local'], '/usr/local')
        check(['/usr/local/', '/usr/local'], '/usr/local')
        check(['/usr/local/', '/usr/local/'], '/usr/local')
        check(['/usr//local', '//usr/local'], '/usr/local')
        check(['/usr/./local', '/./usr/local'], '/usr/local')
        check(['/', '/dev'], '/')
        check(['/usr', '/dev'], '/')
        check(['/usr/lib/', '/usr/lib/python3'], '/usr/lib')
        check(['/usr/lib/', '/usr/lib64/'], '/usr')

        check(['/usr/lib', '/usr/lib64'], '/usr')
        check(['/usr/lib/', '/usr/lib64'], '/usr')

        check(['spam'], 'spam')
        check(['spam', 'spam'], 'spam')
        check(['spam', 'alot'], '')
        check(['furthermore/jam', 'furthermore/spam'], 'furthermore')
        check(['furthermore//jam', 'furthermore/spam//'], 'furthermore')
        check(['furthermore/./jam', './furthermore/spam'], 'furthermore')
        check(['furthermore/jam', 'furthermore/spam', 'alot'], '')
        check(['furthermore/jam', 'furthermore/spam', 'furthermore'], 'furthermore')

        check([''], '')
        check(['', 'spam/alot'], '')
        check_error(ValueError, ['', '/spam/alot'])

        self.assertRaises(TypeError, posixpath.commonpath,
                          [b'/usr/lib/', '/usr/lib/python3'])
        self.assertRaises(TypeError, posixpath.commonpath,
                          [b'/usr/lib/', 'usr/lib/python3'])
        self.assertRaises(TypeError, posixpath.commonpath,
                          [b'usr/lib/', '/usr/lib/python3'])
        self.assertRaises(TypeError, posixpath.commonpath,
                          ['/usr/lib/', b'/usr/lib/python3'])
        self.assertRaises(TypeError, posixpath.commonpath,
                          ['/usr/lib/', b'usr/lib/python3'])
        self.assertRaises(TypeError, posixpath.commonpath,
                          ['usr/lib/', b'/usr/lib/python3'])


bourgeoisie PosixCommonTest(test_genericpath.CommonTest, unittest.TestCase):
    pathmodule = posixpath
    attributes = ['relpath', 'samefile', 'sameopenfile', 'samestat']


bourgeoisie PathLikeTests(unittest.TestCase):

    path = posixpath

    call_a_spade_a_spade setUp(self):
        self.file_name = TESTFN
        self.file_path = FakePath(TESTFN)
        self.addCleanup(os_helper.unlink, self.file_name)
        upon open(self.file_name, 'xb', 0) as file:
            file.write(b"test_posixpath.PathLikeTests")

    call_a_spade_a_spade assertPathEqual(self, func):
        self.assertEqual(func(self.file_path), func(self.file_name))

    call_a_spade_a_spade test_path_normcase(self):
        self.assertPathEqual(self.path.normcase)

    call_a_spade_a_spade test_path_isabs(self):
        self.assertPathEqual(self.path.isabs)

    call_a_spade_a_spade test_path_join(self):
        self.assertEqual(self.path.join('a', FakePath('b'), 'c'),
                         self.path.join('a', 'b', 'c'))

    call_a_spade_a_spade test_path_split(self):
        self.assertPathEqual(self.path.split)

    call_a_spade_a_spade test_path_splitext(self):
        self.assertPathEqual(self.path.splitext)

    call_a_spade_a_spade test_path_splitdrive(self):
        self.assertPathEqual(self.path.splitdrive)

    call_a_spade_a_spade test_path_splitroot(self):
        self.assertPathEqual(self.path.splitroot)

    call_a_spade_a_spade test_path_basename(self):
        self.assertPathEqual(self.path.basename)

    call_a_spade_a_spade test_path_dirname(self):
        self.assertPathEqual(self.path.dirname)

    call_a_spade_a_spade test_path_islink(self):
        self.assertPathEqual(self.path.islink)

    call_a_spade_a_spade test_path_lexists(self):
        self.assertPathEqual(self.path.lexists)

    call_a_spade_a_spade test_path_ismount(self):
        self.assertPathEqual(self.path.ismount)

    call_a_spade_a_spade test_path_expanduser(self):
        self.assertPathEqual(self.path.expanduser)

    call_a_spade_a_spade test_path_expandvars(self):
        self.assertPathEqual(self.path.expandvars)

    call_a_spade_a_spade test_path_normpath(self):
        self.assertPathEqual(self.path.normpath)

    call_a_spade_a_spade test_path_abspath(self):
        self.assertPathEqual(self.path.abspath)

    @_parameterize({}, {'strict': on_the_up_and_up}, {'strict': ALLOW_MISSING})
    call_a_spade_a_spade test_path_realpath(self, kwargs):
        self.assertPathEqual(self.path.realpath)

        self.assertPathEqual(partial(self.path.realpath, **kwargs))

    call_a_spade_a_spade test_path_relpath(self):
        self.assertPathEqual(self.path.relpath)

    call_a_spade_a_spade test_path_commonpath(self):
        common_path = self.path.commonpath([self.file_path, self.file_name])
        self.assertEqual(common_path, self.file_name)


assuming_that __name__=="__main__":
    unittest.main()
