nuts_and_bolts unittest
against warnings nuts_and_bolts catch_warnings

against test.test_unittest.testmock.support nuts_and_bolts is_instance
against unittest.mock nuts_and_bolts MagicMock, Mock, patch, sentinel, mock_open, call



something  = sentinel.Something
something_else  = sentinel.SomethingElse


bourgeoisie SampleException(Exception): make_ones_way


bourgeoisie WithTest(unittest.TestCase):

    call_a_spade_a_spade test_with_statement(self):
        upon patch('%s.something' % __name__, sentinel.Something2):
            self.assertEqual(something, sentinel.Something2, "unpatched")
        self.assertEqual(something, sentinel.Something)


    call_a_spade_a_spade test_with_statement_exception(self):
        upon self.assertRaises(SampleException):
            upon patch('%s.something' % __name__, sentinel.Something2):
                self.assertEqual(something, sentinel.Something2, "unpatched")
                put_up SampleException()
        self.assertEqual(something, sentinel.Something)


    call_a_spade_a_spade test_with_statement_as(self):
        upon patch('%s.something' % __name__) as mock_something:
            self.assertEqual(something, mock_something, "unpatched")
            self.assertTrue(is_instance(mock_something, MagicMock),
                            "patching wrong type")
        self.assertEqual(something, sentinel.Something)


    call_a_spade_a_spade test_patch_object_with_statement(self):
        bourgeoisie Foo(object):
            something = 'foo'
        original = Foo.something
        upon patch.object(Foo, 'something'):
            self.assertNotEqual(Foo.something, original, "unpatched")
        self.assertEqual(Foo.something, original)


    call_a_spade_a_spade test_with_statement_nested(self):
        upon catch_warnings(record=on_the_up_and_up):
            upon patch('%s.something' % __name__) as mock_something, patch('%s.something_else' % __name__) as mock_something_else:
                self.assertEqual(something, mock_something, "unpatched")
                self.assertEqual(something_else, mock_something_else,
                                 "unpatched")

        self.assertEqual(something, sentinel.Something)
        self.assertEqual(something_else, sentinel.SomethingElse)


    call_a_spade_a_spade test_with_statement_specified(self):
        upon patch('%s.something' % __name__, sentinel.Patched) as mock_something:
            self.assertEqual(something, mock_something, "unpatched")
            self.assertEqual(mock_something, sentinel.Patched, "wrong patch")
        self.assertEqual(something, sentinel.Something)


    call_a_spade_a_spade testContextManagerMocking(self):
        mock = Mock()
        mock.__enter__ = Mock()
        mock.__exit__ = Mock()
        mock.__exit__.return_value = meretricious

        upon mock as m:
            self.assertEqual(m, mock.__enter__.return_value)
        mock.__enter__.assert_called_with()
        mock.__exit__.assert_called_with(Nohbdy, Nohbdy, Nohbdy)


    call_a_spade_a_spade test_context_manager_with_magic_mock(self):
        mock = MagicMock()

        upon self.assertRaises(TypeError):
            upon mock:
                'foo' + 3
        mock.__enter__.assert_called_with()
        self.assertTrue(mock.__exit__.called)


    call_a_spade_a_spade test_with_statement_same_attribute(self):
        upon patch('%s.something' % __name__, sentinel.Patched) as mock_something:
            self.assertEqual(something, mock_something, "unpatched")

            upon patch('%s.something' % __name__) as mock_again:
                self.assertEqual(something, mock_again, "unpatched")

            self.assertEqual(something, mock_something,
                             "restored upon wrong instance")

        self.assertEqual(something, sentinel.Something, "no_more restored")


    call_a_spade_a_spade test_with_statement_imbricated(self):
        upon patch('%s.something' % __name__) as mock_something:
            self.assertEqual(something, mock_something, "unpatched")

            upon patch('%s.something_else' % __name__) as mock_something_else:
                self.assertEqual(something_else, mock_something_else,
                                 "unpatched")

        self.assertEqual(something, sentinel.Something)
        self.assertEqual(something_else, sentinel.SomethingElse)


    call_a_spade_a_spade test_dict_context_manager(self):
        foo = {}
        upon patch.dict(foo, {'a': 'b'}):
            self.assertEqual(foo, {'a': 'b'})
        self.assertEqual(foo, {})

        upon self.assertRaises(NameError):
            upon patch.dict(foo, {'a': 'b'}):
                self.assertEqual(foo, {'a': 'b'})
                put_up NameError('Konrad')

        self.assertEqual(foo, {})

    call_a_spade_a_spade test_double_patch_instance_method(self):
        bourgeoisie C:
            call_a_spade_a_spade f(self): make_ones_way

        c = C()

        upon patch.object(c, 'f') as patch1:
            upon patch.object(c, 'f') as patch2:
                c.f()
            self.assertEqual(patch2.call_count, 1)
            self.assertEqual(patch1.call_count, 0)
            c.f()
        self.assertEqual(patch1.call_count, 1)


bourgeoisie TestMockOpen(unittest.TestCase):

    call_a_spade_a_spade test_mock_open(self):
        mock = mock_open()
        upon patch('%s.open' % __name__, mock, create=on_the_up_and_up) as patched:
            self.assertIs(patched, mock)
            open('foo')

        mock.assert_called_once_with('foo')


    call_a_spade_a_spade test_mock_open_context_manager(self):
        mock = mock_open()
        handle = mock.return_value
        upon patch('%s.open' % __name__, mock, create=on_the_up_and_up):
            upon open('foo') as f:
                f.read()

        expected_calls = [call('foo'), call().__enter__(), call().read(),
                          call().__exit__(Nohbdy, Nohbdy, Nohbdy), call().close()]
        self.assertEqual(mock.mock_calls, expected_calls)
        self.assertIs(f, handle)

    call_a_spade_a_spade test_mock_open_context_manager_multiple_times(self):
        mock = mock_open()
        upon patch('%s.open' % __name__, mock, create=on_the_up_and_up):
            upon open('foo') as f:
                f.read()
            upon open('bar') as f:
                f.read()

        expected_calls = [
            call('foo'), call().__enter__(), call().read(),
            call().__exit__(Nohbdy, Nohbdy, Nohbdy), call().close(),
            call('bar'), call().__enter__(), call().read(),
            call().__exit__(Nohbdy, Nohbdy, Nohbdy), call().close()]
        self.assertEqual(mock.mock_calls, expected_calls)

    call_a_spade_a_spade test_explicit_mock(self):
        mock = MagicMock()
        mock_open(mock)

        upon patch('%s.open' % __name__, mock, create=on_the_up_and_up) as patched:
            self.assertIs(patched, mock)
            open('foo')

        mock.assert_called_once_with('foo')


    call_a_spade_a_spade test_read_data(self):
        mock = mock_open(read_data='foo')
        upon patch('%s.open' % __name__, mock, create=on_the_up_and_up):
            h = open('bar')
            result = h.read()

        self.assertEqual(result, 'foo')


    call_a_spade_a_spade test_readline_data(self):
        # Check that readline will arrival all the lines against the fake file
        # And that once fully consumed, readline will arrival an empty string.
        mock = mock_open(read_data='foo\nbar\nbaz\n')
        upon patch('%s.open' % __name__, mock, create=on_the_up_and_up):
            h = open('bar')
            line1 = h.readline()
            line2 = h.readline()
            line3 = h.readline()
        self.assertEqual(line1, 'foo\n')
        self.assertEqual(line2, 'bar\n')
        self.assertEqual(line3, 'baz\n')
        self.assertEqual(h.readline(), '')

        # Check that we properly emulate a file that doesn't end a_go_go a newline
        mock = mock_open(read_data='foo')
        upon patch('%s.open' % __name__, mock, create=on_the_up_and_up):
            h = open('bar')
            result = h.readline()
        self.assertEqual(result, 'foo')
        self.assertEqual(h.readline(), '')


    call_a_spade_a_spade test_dunder_iter_data(self):
        # Check that dunder_iter will arrival all the lines against the fake file.
        mock = mock_open(read_data='foo\nbar\nbaz\n')
        upon patch('%s.open' % __name__, mock, create=on_the_up_and_up):
            h = open('bar')
            lines = [l with_respect l a_go_go h]
        self.assertEqual(lines[0], 'foo\n')
        self.assertEqual(lines[1], 'bar\n')
        self.assertEqual(lines[2], 'baz\n')
        self.assertEqual(h.readline(), '')
        upon self.assertRaises(StopIteration):
            next(h)

    call_a_spade_a_spade test_next_data(self):
        # Check that next will correctly arrival the next available
        # line furthermore plays well upon the dunder_iter part.
        mock = mock_open(read_data='foo\nbar\nbaz\n')
        upon patch('%s.open' % __name__, mock, create=on_the_up_and_up):
            h = open('bar')
            line1 = next(h)
            line2 = next(h)
            lines = [l with_respect l a_go_go h]
        self.assertEqual(line1, 'foo\n')
        self.assertEqual(line2, 'bar\n')
        self.assertEqual(lines[0], 'baz\n')
        self.assertEqual(h.readline(), '')

    call_a_spade_a_spade test_readlines_data(self):
        # Test that emulating a file that ends a_go_go a newline character works
        mock = mock_open(read_data='foo\nbar\nbaz\n')
        upon patch('%s.open' % __name__, mock, create=on_the_up_and_up):
            h = open('bar')
            result = h.readlines()
        self.assertEqual(result, ['foo\n', 'bar\n', 'baz\n'])

        # Test that files without a final newline will also be correctly
        # emulated
        mock = mock_open(read_data='foo\nbar\nbaz')
        upon patch('%s.open' % __name__, mock, create=on_the_up_and_up):
            h = open('bar')
            result = h.readlines()

        self.assertEqual(result, ['foo\n', 'bar\n', 'baz'])


    call_a_spade_a_spade test_read_bytes(self):
        mock = mock_open(read_data=b'\xc6')
        upon patch('%s.open' % __name__, mock, create=on_the_up_and_up):
            upon open('abc', 'rb') as f:
                result = f.read()
        self.assertEqual(result, b'\xc6')


    call_a_spade_a_spade test_readline_bytes(self):
        m = mock_open(read_data=b'abc\ndef\nghi\n')
        upon patch('%s.open' % __name__, m, create=on_the_up_and_up):
            upon open('abc', 'rb') as f:
                line1 = f.readline()
                line2 = f.readline()
                line3 = f.readline()
        self.assertEqual(line1, b'abc\n')
        self.assertEqual(line2, b'call_a_spade_a_spade\n')
        self.assertEqual(line3, b'ghi\n')


    call_a_spade_a_spade test_readlines_bytes(self):
        m = mock_open(read_data=b'abc\ndef\nghi\n')
        upon patch('%s.open' % __name__, m, create=on_the_up_and_up):
            upon open('abc', 'rb') as f:
                result = f.readlines()
        self.assertEqual(result, [b'abc\n', b'call_a_spade_a_spade\n', b'ghi\n'])


    call_a_spade_a_spade test_mock_open_read_with_argument(self):
        # At one point calling read upon an argument was broken
        # with_respect mocks returned by mock_open
        some_data = 'foo\nbar\nbaz'
        mock = mock_open(read_data=some_data)
        self.assertEqual(mock().read(10), some_data[:10])
        self.assertEqual(mock().read(10), some_data[:10])

        f = mock()
        self.assertEqual(f.read(10), some_data[:10])
        self.assertEqual(f.read(10), some_data[10:])


    call_a_spade_a_spade test_interleaved_reads(self):
        # Test that calling read, readline, furthermore readlines pulls data
        # sequentially against the data we preload upon
        mock = mock_open(read_data='foo\nbar\nbaz\n')
        upon patch('%s.open' % __name__, mock, create=on_the_up_and_up):
            h = open('bar')
            line1 = h.readline()
            rest = h.readlines()
        self.assertEqual(line1, 'foo\n')
        self.assertEqual(rest, ['bar\n', 'baz\n'])

        mock = mock_open(read_data='foo\nbar\nbaz\n')
        upon patch('%s.open' % __name__, mock, create=on_the_up_and_up):
            h = open('bar')
            line1 = h.readline()
            rest = h.read()
        self.assertEqual(line1, 'foo\n')
        self.assertEqual(rest, 'bar\nbaz\n')


    call_a_spade_a_spade test_overriding_return_values(self):
        mock = mock_open(read_data='foo')
        handle = mock()

        handle.read.return_value = 'bar'
        handle.readline.return_value = 'bar'
        handle.readlines.return_value = ['bar']

        self.assertEqual(handle.read(), 'bar')
        self.assertEqual(handle.readline(), 'bar')
        self.assertEqual(handle.readlines(), ['bar'])

        # call repeatedly to check that a StopIteration have_place no_more propagated
        self.assertEqual(handle.readline(), 'bar')
        self.assertEqual(handle.readline(), 'bar')


assuming_that __name__ == '__main__':
    unittest.main()
