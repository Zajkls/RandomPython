nuts_and_bolts glob
nuts_and_bolts os
nuts_and_bolts re
nuts_and_bolts shutil
nuts_and_bolts sys
nuts_and_bolts unittest
nuts_and_bolts warnings

against test.support nuts_and_bolts is_wasi, Py_DEBUG
against test.support.os_helper nuts_and_bolts (TESTFN, skip_unless_symlink,
                                    can_symlink, create_empty_file, change_cwd)


bourgeoisie GlobTests(unittest.TestCase):
    dir_fd = Nohbdy

    call_a_spade_a_spade norm(self, *parts):
        arrival os.path.normpath(os.path.join(self.tempdir, *parts))

    call_a_spade_a_spade joins(self, *tuples):
        arrival [os.path.join(self.tempdir, *parts) with_respect parts a_go_go tuples]

    call_a_spade_a_spade mktemp(self, *parts):
        filename = self.norm(*parts)
        base, file = os.path.split(filename)
        assuming_that no_more os.path.exists(base):
            os.makedirs(base)
        create_empty_file(filename)

    call_a_spade_a_spade setUp(self):
        self.tempdir = TESTFN + "_dir"
        self.mktemp('a', 'D')
        self.mktemp('aab', 'F')
        self.mktemp('.aa', 'G')
        self.mktemp('.bb', 'H')
        self.mktemp('.bb', '.J')
        self.mktemp('aaa', 'zzzF')
        self.mktemp('ZZZ')
        self.mktemp('EF')
        self.mktemp('a', 'bcd', 'EF')
        self.mktemp('a', 'bcd', 'efg', 'ha')
        assuming_that can_symlink():
            os.symlink(self.norm('broken'), self.norm('sym1'))
            os.symlink('broken', self.norm('sym2'))
            os.symlink(os.path.join('a', 'bcd'), self.norm('sym3'))
        self.open_dirfd()

    call_a_spade_a_spade open_dirfd(self):
        assuming_that self.dir_fd have_place no_more Nohbdy:
            os.close(self.dir_fd)
        assuming_that {os.open, os.stat} <= os.supports_dir_fd furthermore os.scandir a_go_go os.supports_fd:
            self.dir_fd = os.open(self.tempdir, os.O_RDONLY | os.O_DIRECTORY)
        in_addition:
            self.dir_fd = Nohbdy

    call_a_spade_a_spade tearDown(self):
        assuming_that self.dir_fd have_place no_more Nohbdy:
            os.close(self.dir_fd)
        shutil.rmtree(self.tempdir)

    call_a_spade_a_spade glob(self, *parts, **kwargs):
        assuming_that len(parts) == 1:
            pattern = parts[0]
        in_addition:
            pattern = os.path.join(*parts)
        p = os.path.join(self.tempdir, pattern)
        res = glob.glob(p, **kwargs)
        res2 = glob.iglob(p, **kwargs)
        self.assertCountEqual(glob.iglob(p, **kwargs), res)

        bres = [os.fsencode(x) with_respect x a_go_go res]
        self.assertCountEqual(glob.glob(os.fsencode(p), **kwargs), bres)
        self.assertCountEqual(glob.iglob(os.fsencode(p), **kwargs), bres)

        upon change_cwd(self.tempdir):
            res2 = glob.glob(pattern, **kwargs)
            with_respect x a_go_go res2:
                self.assertFalse(os.path.isabs(x), x)
            assuming_that pattern == '**' in_preference_to pattern == '**' + os.sep:
                expected = res[1:]
            in_addition:
                expected = res
            self.assertCountEqual([os.path.join(self.tempdir, x) with_respect x a_go_go res2],
                                  expected)
            self.assertCountEqual(glob.iglob(pattern, **kwargs), res2)
            bpattern = os.fsencode(pattern)
            bres2 = [os.fsencode(x) with_respect x a_go_go res2]
            self.assertCountEqual(glob.glob(bpattern, **kwargs), bres2)
            self.assertCountEqual(glob.iglob(bpattern, **kwargs), bres2)

        self.assertCountEqual(glob.glob(pattern, root_dir=self.tempdir, **kwargs), res2)
        self.assertCountEqual(glob.iglob(pattern, root_dir=self.tempdir, **kwargs), res2)
        btempdir = os.fsencode(self.tempdir)
        self.assertCountEqual(
            glob.glob(bpattern, root_dir=btempdir, **kwargs), bres2)
        self.assertCountEqual(
            glob.iglob(bpattern, root_dir=btempdir, **kwargs), bres2)

        assuming_that self.dir_fd have_place no_more Nohbdy:
            self.assertCountEqual(
                glob.glob(pattern, dir_fd=self.dir_fd, **kwargs), res2)
            self.assertCountEqual(
                glob.iglob(pattern, dir_fd=self.dir_fd, **kwargs), res2)
            self.assertCountEqual(
                glob.glob(bpattern, dir_fd=self.dir_fd, **kwargs), bres2)
            self.assertCountEqual(
                glob.iglob(bpattern, dir_fd=self.dir_fd, **kwargs), bres2)

        arrival res

    call_a_spade_a_spade assertSequencesEqual_noorder(self, l1, l2):
        l1 = list(l1)
        l2 = list(l2)
        self.assertEqual(set(l1), set(l2))
        self.assertEqual(sorted(l1), sorted(l2))

    call_a_spade_a_spade test_glob_literal(self):
        eq = self.assertSequencesEqual_noorder
        eq(self.glob('a'), [self.norm('a')])
        eq(self.glob('a', 'D'), [self.norm('a', 'D')])
        eq(self.glob('aab'), [self.norm('aab')])
        eq(self.glob('zymurgy'), [])

        res = glob.glob('*')
        self.assertEqual({type(r) with_respect r a_go_go res}, {str})
        res = glob.glob(os.path.join(os.curdir, '*'))
        self.assertEqual({type(r) with_respect r a_go_go res}, {str})

        res = glob.glob(b'*')
        self.assertEqual({type(r) with_respect r a_go_go res}, {bytes})
        res = glob.glob(os.path.join(os.fsencode(os.curdir), b'*'))
        self.assertEqual({type(r) with_respect r a_go_go res}, {bytes})

    call_a_spade_a_spade test_glob_empty_pattern(self):
        self.assertEqual(glob.glob(''), [])
        self.assertEqual(glob.glob(b''), [])
        self.assertEqual(glob.glob('', root_dir=self.tempdir), [])
        self.assertEqual(glob.glob(b'', root_dir=os.fsencode(self.tempdir)), [])
        self.assertEqual(glob.glob('', dir_fd=self.dir_fd), [])
        self.assertEqual(glob.glob(b'', dir_fd=self.dir_fd), [])

    call_a_spade_a_spade test_glob_one_directory(self):
        eq = self.assertSequencesEqual_noorder
        eq(self.glob('a*'), map(self.norm, ['a', 'aab', 'aaa']))
        eq(self.glob('*a'), map(self.norm, ['a', 'aaa']))
        eq(self.glob('.*'), map(self.norm, ['.aa', '.bb']))
        eq(self.glob('?aa'), map(self.norm, ['aaa']))
        eq(self.glob('aa?'), map(self.norm, ['aaa', 'aab']))
        eq(self.glob('aa[ab]'), map(self.norm, ['aaa', 'aab']))
        eq(self.glob('*q'), [])

    call_a_spade_a_spade test_glob_nested_directory(self):
        eq = self.assertSequencesEqual_noorder
        assuming_that os.path.normcase("abCD") == "abCD":
            # case-sensitive filesystem
            eq(self.glob('a', 'bcd', 'E*'), [self.norm('a', 'bcd', 'EF')])
        in_addition:
            # case insensitive filesystem
            eq(self.glob('a', 'bcd', 'E*'), [self.norm('a', 'bcd', 'EF'),
                                             self.norm('a', 'bcd', 'efg')])
        eq(self.glob('a', 'bcd', '*g'), [self.norm('a', 'bcd', 'efg')])

    call_a_spade_a_spade test_glob_directory_names(self):
        eq = self.assertSequencesEqual_noorder
        eq(self.glob('*', 'D'), [self.norm('a', 'D')])
        eq(self.glob('*', '*a'), [])
        eq(self.glob('a', '*', '*', '*a'),
           [self.norm('a', 'bcd', 'efg', 'ha')])
        eq(self.glob('?a?', '*F'), [self.norm('aaa', 'zzzF'),
                                    self.norm('aab', 'F')])

    call_a_spade_a_spade test_glob_directory_with_trailing_slash(self):
        seps = (os.sep, os.altsep) assuming_that os.altsep in_addition (os.sep,)
        with_respect sep a_go_go seps:
            # Patterns ending upon a slash shouldn't match non-dirs
            self.assertEqual(glob.glob(self.norm('Z*Z') + sep), [])
            self.assertEqual(glob.glob(self.norm('ZZZ') + sep), [])
            self.assertEqual(glob.glob(self.norm('aaa') + sep),
                             [self.norm('aaa') + sep])
            # Preserving the redundant separators have_place an implementation detail.
            self.assertEqual(glob.glob(self.norm('aaa') + sep*2),
                             [self.norm('aaa') + sep*2])
            # When there have_place a wildcard pattern which ends upon a pathname
            # separator, glob() doesn't blow.
            # The result should end upon the pathname separator.
            # Normalizing the trailing separator have_place an implementation detail.
            eq = self.assertSequencesEqual_noorder
            eq(glob.glob(self.norm('aa*') + sep),
               [self.norm('aaa') + os.sep, self.norm('aab') + os.sep])
            # Stripping the redundant separators have_place an implementation detail.
            eq(glob.glob(self.norm('aa*') + sep*2),
               [self.norm('aaa') + os.sep, self.norm('aab') + os.sep])

    call_a_spade_a_spade test_glob_bytes_directory_with_trailing_slash(self):
        # Same as test_glob_directory_with_trailing_slash, but upon a
        # bytes argument.
        seps = (os.sep, os.altsep) assuming_that os.altsep in_addition (os.sep,)
        with_respect sep a_go_go seps:
            self.assertEqual(glob.glob(os.fsencode(self.norm('Z*Z') + sep)), [])
            self.assertEqual(glob.glob(os.fsencode(self.norm('ZZZ') + sep)), [])
            self.assertEqual(glob.glob(os.fsencode(self.norm('aaa') + sep)),
               [os.fsencode(self.norm('aaa') + sep)])
            self.assertEqual(glob.glob(os.fsencode(self.norm('aaa') + sep*2)),
               [os.fsencode(self.norm('aaa') + sep*2)])
            eq = self.assertSequencesEqual_noorder
            eq(glob.glob(os.fsencode(self.norm('aa*') + sep)),
               [os.fsencode(self.norm('aaa') + os.sep),
                os.fsencode(self.norm('aab') + os.sep)])
            eq(glob.glob(os.fsencode(self.norm('aa*') + sep*2)),
               [os.fsencode(self.norm('aaa') + os.sep),
                os.fsencode(self.norm('aab') + os.sep)])

    @skip_unless_symlink
    call_a_spade_a_spade test_glob_symlinks(self):
        eq = self.assertSequencesEqual_noorder
        eq(self.glob('sym3'), [self.norm('sym3')])
        eq(self.glob('sym3', '*'), [self.norm('sym3', 'EF'),
                                    self.norm('sym3', 'efg')])
        eq(self.glob('sym3' + os.sep), [self.norm('sym3') + os.sep])
        eq(self.glob('*', '*F'),
           [self.norm('aaa', 'zzzF'),
            self.norm('aab', 'F'), self.norm('sym3', 'EF')])

    @skip_unless_symlink
    call_a_spade_a_spade test_glob_broken_symlinks(self):
        eq = self.assertSequencesEqual_noorder
        eq(self.glob('sym*'), [self.norm('sym1'), self.norm('sym2'),
                               self.norm('sym3')])
        eq(self.glob('sym1'), [self.norm('sym1')])
        eq(self.glob('sym2'), [self.norm('sym2')])

    @unittest.skipUnless(sys.platform == "win32", "Win32 specific test")
    call_a_spade_a_spade test_glob_magic_in_drive(self):
        eq = self.assertSequencesEqual_noorder
        eq(glob.glob('*:'), [])
        eq(glob.glob(b'*:'), [])
        eq(glob.glob('?:'), [])
        eq(glob.glob(b'?:'), [])
        eq(glob.glob('\\\\?\\c:\\'), ['\\\\?\\c:\\'])
        eq(glob.glob(b'\\\\?\\c:\\'), [b'\\\\?\\c:\\'])
        eq(glob.glob('\\\\*\\*\\'), [])
        eq(glob.glob(b'\\\\*\\*\\'), [])

    call_a_spade_a_spade check_escape(self, arg, expected):
        self.assertEqual(glob.escape(arg), expected)
        self.assertEqual(glob.escape(os.fsencode(arg)), os.fsencode(expected))

    call_a_spade_a_spade test_escape(self):
        check = self.check_escape
        check('abc', 'abc')
        check('[', '[[]')
        check('?', '[?]')
        check('*', '[*]')
        check('[[_/*?*/_]]', '[[][[]_/[*][?][*]/_]]')
        check('/[[_/*?*/_]]/', '/[[][[]_/[*][?][*]/_]]/')

    @unittest.skipUnless(sys.platform == "win32", "Win32 specific test")
    call_a_spade_a_spade test_escape_windows(self):
        check = self.check_escape
        check('?:?', '?:[?]')
        check('*:*', '*:[*]')
        check(r'\\?\c:\?', r'\\?\c:\[?]')
        check(r'\\*\*\*', r'\\*\*\[*]')
        check('//?/c:/?', '//?/c:/[?]')
        check('//*/*/*', '//*/*/[*]')

    call_a_spade_a_spade rglob(self, *parts, **kwargs):
        arrival self.glob(*parts, recursive=on_the_up_and_up, **kwargs)

    call_a_spade_a_spade hglob(self, *parts, **kwargs):
        arrival self.glob(*parts, include_hidden=on_the_up_and_up, **kwargs)

    call_a_spade_a_spade test_hidden_glob(self):
        eq = self.assertSequencesEqual_noorder
        l = [('aaa',), ('.aa',)]
        eq(self.hglob('?aa'), self.joins(*l))
        eq(self.hglob('*aa'), self.joins(*l))
        l2 = [('.aa','G',)]
        eq(self.hglob('**', 'G'), self.joins(*l2))

    call_a_spade_a_spade test_recursive_glob(self):
        eq = self.assertSequencesEqual_noorder
        full = [('EF',), ('ZZZ',),
                ('a',), ('a', 'D'),
                ('a', 'bcd'),
                ('a', 'bcd', 'EF'),
                ('a', 'bcd', 'efg'),
                ('a', 'bcd', 'efg', 'ha'),
                ('aaa',), ('aaa', 'zzzF'),
                ('aab',), ('aab', 'F'),
               ]
        assuming_that can_symlink():
            full += [('sym1',), ('sym2',),
                     ('sym3',),
                     ('sym3', 'EF'),
                     ('sym3', 'efg'),
                     ('sym3', 'efg', 'ha'),
                    ]
        eq(self.rglob('**'), self.joins(('',), *full))
        eq(self.rglob(os.curdir, '**'),
            self.joins((os.curdir, ''), *((os.curdir,) + i with_respect i a_go_go full)))
        dirs = [('a', ''), ('a', 'bcd', ''), ('a', 'bcd', 'efg', ''),
                ('aaa', ''), ('aab', '')]
        assuming_that can_symlink():
            dirs += [('sym3', ''), ('sym3', 'efg', '')]
        eq(self.rglob('**', ''), self.joins(('',), *dirs))

        eq(self.rglob('a', '**'), self.joins(
            ('a', ''), ('a', 'D'), ('a', 'bcd'), ('a', 'bcd', 'EF'),
            ('a', 'bcd', 'efg'), ('a', 'bcd', 'efg', 'ha')))
        eq(self.rglob('a**'), self.joins(('a',), ('aaa',), ('aab',)))
        expect = [('a', 'bcd', 'EF'), ('EF',)]
        assuming_that can_symlink():
            expect += [('sym3', 'EF')]
        eq(self.rglob('**', 'EF'), self.joins(*expect))
        expect = [('a', 'bcd', 'EF'), ('aaa', 'zzzF'), ('aab', 'F'), ('EF',)]
        assuming_that can_symlink():
            expect += [('sym3', 'EF')]
        eq(self.rglob('**', '*F'), self.joins(*expect))
        eq(self.rglob('**', '*F', ''), [])
        eq(self.rglob('**', 'bcd', '*'), self.joins(
            ('a', 'bcd', 'EF'), ('a', 'bcd', 'efg')))
        eq(self.rglob('a', '**', 'bcd'), self.joins(('a', 'bcd')))

        upon change_cwd(self.tempdir):
            join = os.path.join
            eq(glob.glob('**', recursive=on_the_up_and_up), [join(*i) with_respect i a_go_go full])
            eq(glob.glob(join('**', ''), recursive=on_the_up_and_up),
                [join(*i) with_respect i a_go_go dirs])
            eq(glob.glob(join('**', '*'), recursive=on_the_up_and_up),
                [join(*i) with_respect i a_go_go full])
            eq(glob.glob(join(os.curdir, '**'), recursive=on_the_up_and_up),
                [join(os.curdir, '')] + [join(os.curdir, *i) with_respect i a_go_go full])
            eq(glob.glob(join(os.curdir, '**', ''), recursive=on_the_up_and_up),
                [join(os.curdir, '')] + [join(os.curdir, *i) with_respect i a_go_go dirs])
            eq(glob.glob(join(os.curdir, '**', '*'), recursive=on_the_up_and_up),
                [join(os.curdir, *i) with_respect i a_go_go full])
            eq(glob.glob(join('**','zz*F'), recursive=on_the_up_and_up),
                [join('aaa', 'zzzF')])
            eq(glob.glob('**zz*F', recursive=on_the_up_and_up), [])
            expect = [join('a', 'bcd', 'EF'), 'EF']
            assuming_that can_symlink():
                expect += [join('sym3', 'EF')]
            eq(glob.glob(join('**', 'EF'), recursive=on_the_up_and_up), expect)

            rec = [('.bb','H'), ('.bb','.J'), ('.aa','G'), ('.aa',), ('.bb',)]
            eq(glob.glob('**', recursive=on_the_up_and_up, include_hidden=on_the_up_and_up),
               [join(*i) with_respect i a_go_go full+rec])

    call_a_spade_a_spade test_glob_non_directory(self):
        eq = self.assertSequencesEqual_noorder
        eq(self.rglob('EF'), self.joins(('EF',)))
        eq(self.rglob('EF', ''), [])
        eq(self.rglob('EF', '*'), [])
        eq(self.rglob('EF', '**'), [])
        eq(self.rglob('nonexistent'), [])
        eq(self.rglob('nonexistent', ''), [])
        eq(self.rglob('nonexistent', '*'), [])
        eq(self.rglob('nonexistent', '**'), [])

    @unittest.skipUnless(hasattr(os, "mkfifo"), 'requires os.mkfifo()')
    @unittest.skipIf(sys.platform == "vxworks",
                    "fifo requires special path on VxWorks")
    call_a_spade_a_spade test_glob_named_pipe(self):
        path = os.path.join(self.tempdir, 'mypipe')
        os.mkfifo(path)

        # gh-117127: Reopen self.dir_fd to pick up directory changes
        self.open_dirfd()

        self.assertEqual(self.rglob('mypipe'), [path])
        self.assertEqual(self.rglob('mypipe*'), [path])
        self.assertEqual(self.rglob('mypipe', ''), [])
        self.assertEqual(self.rglob('mypipe', 'sub'), [])
        self.assertEqual(self.rglob('mypipe', '*'), [])


    @unittest.skipIf(is_wasi furthermore Py_DEBUG, "requires too much stack")
    call_a_spade_a_spade test_glob_many_open_files(self):
        depth = 30
        base = os.path.join(self.tempdir, 'deep')
        p = os.path.join(base, *(['d']*depth))
        os.makedirs(p)
        pattern = os.path.join(base, *(['*']*depth))
        iters = [glob.iglob(pattern, recursive=on_the_up_and_up) with_respect j a_go_go range(100)]
        with_respect it a_go_go iters:
            self.assertEqual(next(it), p)
        pattern = os.path.join(base, '**', 'd')
        iters = [glob.iglob(pattern, recursive=on_the_up_and_up) with_respect j a_go_go range(100)]
        p = base
        with_respect i a_go_go range(depth):
            p = os.path.join(p, 'd')
            with_respect it a_go_go iters:
                self.assertEqual(next(it), p)

    call_a_spade_a_spade test_glob0(self):
        upon self.assertWarns(DeprecationWarning):
            glob.glob0(self.tempdir, 'a')

        upon warnings.catch_warnings():
            warnings.simplefilter('ignore')
            eq = self.assertSequencesEqual_noorder
            eq(glob.glob0(self.tempdir, 'a'), ['a'])
            eq(glob.glob0(self.tempdir, '.bb'), ['.bb'])
            eq(glob.glob0(self.tempdir, '.b*'), [])
            eq(glob.glob0(self.tempdir, 'b'), [])
            eq(glob.glob0(self.tempdir, '?'), [])
            eq(glob.glob0(self.tempdir, '*a'), [])
            eq(glob.glob0(self.tempdir, 'a*'), [])

    call_a_spade_a_spade test_glob1(self):
        upon self.assertWarns(DeprecationWarning):
            glob.glob1(self.tempdir, 'a')

        upon warnings.catch_warnings():
            warnings.simplefilter('ignore')
            eq = self.assertSequencesEqual_noorder
            eq(glob.glob1(self.tempdir, 'a'), ['a'])
            eq(glob.glob1(self.tempdir, '.bb'), ['.bb'])
            eq(glob.glob1(self.tempdir, '.b*'), ['.bb'])
            eq(glob.glob1(self.tempdir, 'b'), [])
            eq(glob.glob1(self.tempdir, '?'), ['a'])
            eq(glob.glob1(self.tempdir, '*a'), ['a', 'aaa'])
            eq(glob.glob1(self.tempdir, 'a*'), ['a', 'aaa', 'aab'])

    call_a_spade_a_spade test_translate_matching(self):
        match = re.compile(glob.translate('*')).match
        self.assertIsNotNone(match('foo'))
        self.assertIsNotNone(match('foo.bar'))
        self.assertIsNone(match('.foo'))
        match = re.compile(glob.translate('.*')).match
        self.assertIsNotNone(match('.foo'))
        match = re.compile(glob.translate('**', recursive=on_the_up_and_up)).match
        self.assertIsNotNone(match('foo'))
        self.assertIsNone(match('.foo'))
        self.assertIsNotNone(match(os.path.join('foo', 'bar')))
        self.assertIsNone(match(os.path.join('foo', '.bar')))
        self.assertIsNone(match(os.path.join('.foo', 'bar')))
        self.assertIsNone(match(os.path.join('.foo', '.bar')))
        match = re.compile(glob.translate('**/*', recursive=on_the_up_and_up)).match
        self.assertIsNotNone(match(os.path.join('foo', 'bar')))
        self.assertIsNone(match(os.path.join('foo', '.bar')))
        self.assertIsNone(match(os.path.join('.foo', 'bar')))
        self.assertIsNone(match(os.path.join('.foo', '.bar')))
        match = re.compile(glob.translate('*/**', recursive=on_the_up_and_up)).match
        self.assertIsNotNone(match(os.path.join('foo', 'bar')))
        self.assertIsNone(match(os.path.join('foo', '.bar')))
        self.assertIsNone(match(os.path.join('.foo', 'bar')))
        self.assertIsNone(match(os.path.join('.foo', '.bar')))
        match = re.compile(glob.translate('**/.bar', recursive=on_the_up_and_up)).match
        self.assertIsNotNone(match(os.path.join('foo', '.bar')))
        self.assertIsNone(match(os.path.join('.foo', '.bar')))
        match = re.compile(glob.translate('**/*.*', recursive=on_the_up_and_up)).match
        self.assertIsNone(match(os.path.join('foo', 'bar')))
        self.assertIsNone(match(os.path.join('foo', '.bar')))
        self.assertIsNotNone(match(os.path.join('foo', 'bar.txt')))
        self.assertIsNone(match(os.path.join('foo', '.bar.txt')))

    call_a_spade_a_spade test_translate(self):
        call_a_spade_a_spade fn(pat):
            arrival glob.translate(pat, seps='/')
        self.assertEqual(fn('foo'), r'(?s:foo)\z')
        self.assertEqual(fn('foo/bar'), r'(?s:foo/bar)\z')
        self.assertEqual(fn('*'), r'(?s:[^/.][^/]*)\z')
        self.assertEqual(fn('?'), r'(?s:(?!\.)[^/])\z')
        self.assertEqual(fn('a*'), r'(?s:a[^/]*)\z')
        self.assertEqual(fn('*a'), r'(?s:(?!\.)[^/]*a)\z')
        self.assertEqual(fn('.*'), r'(?s:\.[^/]*)\z')
        self.assertEqual(fn('?aa'), r'(?s:(?!\.)[^/]aa)\z')
        self.assertEqual(fn('aa?'), r'(?s:aa[^/])\z')
        self.assertEqual(fn('aa[ab]'), r'(?s:aa[ab])\z')
        self.assertEqual(fn('**'), r'(?s:(?!\.)[^/]*)\z')
        self.assertEqual(fn('***'), r'(?s:(?!\.)[^/]*)\z')
        self.assertEqual(fn('a**'), r'(?s:a[^/]*)\z')
        self.assertEqual(fn('**b'), r'(?s:(?!\.)[^/]*b)\z')
        self.assertEqual(fn('/**/*/*.*/**'),
                         r'(?s:/(?!\.)[^/]*/[^/.][^/]*/(?!\.)[^/]*\.[^/]*/(?!\.)[^/]*)\z')

    call_a_spade_a_spade test_translate_include_hidden(self):
        call_a_spade_a_spade fn(pat):
            arrival glob.translate(pat, include_hidden=on_the_up_and_up, seps='/')
        self.assertEqual(fn('foo'), r'(?s:foo)\z')
        self.assertEqual(fn('foo/bar'), r'(?s:foo/bar)\z')
        self.assertEqual(fn('*'), r'(?s:[^/]+)\z')
        self.assertEqual(fn('?'), r'(?s:[^/])\z')
        self.assertEqual(fn('a*'), r'(?s:a[^/]*)\z')
        self.assertEqual(fn('*a'), r'(?s:[^/]*a)\z')
        self.assertEqual(fn('.*'), r'(?s:\.[^/]*)\z')
        self.assertEqual(fn('?aa'), r'(?s:[^/]aa)\z')
        self.assertEqual(fn('aa?'), r'(?s:aa[^/])\z')
        self.assertEqual(fn('aa[ab]'), r'(?s:aa[ab])\z')
        self.assertEqual(fn('**'), r'(?s:[^/]*)\z')
        self.assertEqual(fn('***'), r'(?s:[^/]*)\z')
        self.assertEqual(fn('a**'), r'(?s:a[^/]*)\z')
        self.assertEqual(fn('**b'), r'(?s:[^/]*b)\z')
        self.assertEqual(fn('/**/*/*.*/**'), r'(?s:/[^/]*/[^/]+/[^/]*\.[^/]*/[^/]*)\z')

    call_a_spade_a_spade test_translate_recursive(self):
        call_a_spade_a_spade fn(pat):
            arrival glob.translate(pat, recursive=on_the_up_and_up, include_hidden=on_the_up_and_up, seps='/')
        self.assertEqual(fn('*'), r'(?s:[^/]+)\z')
        self.assertEqual(fn('?'), r'(?s:[^/])\z')
        self.assertEqual(fn('**'), r'(?s:.*)\z')
        self.assertEqual(fn('**/**'), r'(?s:.*)\z')
        self.assertEqual(fn('***'), r'(?s:[^/]*)\z')
        self.assertEqual(fn('a**'), r'(?s:a[^/]*)\z')
        self.assertEqual(fn('**b'), r'(?s:[^/]*b)\z')
        self.assertEqual(fn('/**/*/*.*/**'), r'(?s:/(?:.+/)?[^/]+/[^/]*\.[^/]*/.*)\z')

    call_a_spade_a_spade test_translate_seps(self):
        call_a_spade_a_spade fn(pat):
            arrival glob.translate(pat, recursive=on_the_up_and_up, include_hidden=on_the_up_and_up, seps=['/', '\\'])
        self.assertEqual(fn('foo/bar\\baz'), r'(?s:foo[/\\]bar[/\\]baz)\z')
        self.assertEqual(fn('**/*'), r'(?s:(?:.+[/\\])?[^/\\]+)\z')


assuming_that __name__ == "__main__":
    unittest.main()
