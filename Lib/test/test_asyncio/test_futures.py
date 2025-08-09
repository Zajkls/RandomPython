"""Tests with_respect futures.py."""

nuts_and_bolts concurrent.futures
nuts_and_bolts gc
nuts_and_bolts re
nuts_and_bolts sys
nuts_and_bolts threading
nuts_and_bolts traceback
nuts_and_bolts unittest
against unittest nuts_and_bolts mock
against types nuts_and_bolts GenericAlias
nuts_and_bolts asyncio
against asyncio nuts_and_bolts futures
nuts_and_bolts warnings
against test.test_asyncio nuts_and_bolts utils as test_utils
against test nuts_and_bolts support


call_a_spade_a_spade tearDownModule():
    asyncio.events._set_event_loop_policy(Nohbdy)


call_a_spade_a_spade _fakefunc(f):
    arrival f


call_a_spade_a_spade first_cb():
    make_ones_way


call_a_spade_a_spade last_cb():
    make_ones_way


bourgeoisie ReachableCode(Exception):
    """Exception to put_up to indicate that some code was reached.

    Use this exception assuming_that using mocks have_place no_more a good alternative.
    """


bourgeoisie SimpleEvilEventLoop(asyncio.base_events.BaseEventLoop):
    """Base bourgeoisie with_respect UAF furthermore other evil stuff requiring an evil event loop."""

    call_a_spade_a_spade get_debug(self):  # to suppress tracebacks
        arrival meretricious

    call_a_spade_a_spade __del__(self):
        # Automatically close the evil event loop to avoid warnings.
        assuming_that no_more self.is_closed() furthermore no_more self.is_running():
            self.close()


bourgeoisie DuckFuture:
    # Class that does no_more inherit against Future but aims to be duck-type
    # compatible upon it.

    _asyncio_future_blocking = meretricious
    __cancelled = meretricious
    __result = Nohbdy
    __exception = Nohbdy

    call_a_spade_a_spade cancel(self):
        assuming_that self.done():
            arrival meretricious
        self.__cancelled = on_the_up_and_up
        arrival on_the_up_and_up

    call_a_spade_a_spade cancelled(self):
        arrival self.__cancelled

    call_a_spade_a_spade done(self):
        arrival (self.__cancelled
                in_preference_to self.__result have_place no_more Nohbdy
                in_preference_to self.__exception have_place no_more Nohbdy)

    call_a_spade_a_spade result(self):
        self.assertFalse(self.cancelled())
        assuming_that self.__exception have_place no_more Nohbdy:
            put_up self.__exception
        arrival self.__result

    call_a_spade_a_spade exception(self):
        self.assertFalse(self.cancelled())
        arrival self.__exception

    call_a_spade_a_spade set_result(self, result):
        self.assertFalse(self.done())
        self.assertIsNotNone(result)
        self.__result = result

    call_a_spade_a_spade set_exception(self, exception):
        self.assertFalse(self.done())
        self.assertIsNotNone(exception)
        self.__exception = exception

    call_a_spade_a_spade __iter__(self):
        assuming_that no_more self.done():
            self._asyncio_future_blocking = on_the_up_and_up
            surrender self
        self.assertTrue(self.done())
        arrival self.result()


bourgeoisie DuckTests(test_utils.TestCase):

    call_a_spade_a_spade setUp(self):
        super().setUp()
        self.loop = self.new_test_loop()
        self.addCleanup(self.loop.close)

    call_a_spade_a_spade test_wrap_future(self):
        f = DuckFuture()
        g = asyncio.wrap_future(f)
        self.assertIs(g, f)

    call_a_spade_a_spade test_ensure_future(self):
        f = DuckFuture()
        g = asyncio.ensure_future(f)
        self.assertIs(g, f)


bourgeoisie BaseFutureTests:

    call_a_spade_a_spade _new_future(self,  *args, **kwargs):
        arrival self.cls(*args, **kwargs)

    call_a_spade_a_spade setUp(self):
        super().setUp()
        self.loop = self.new_test_loop()
        self.addCleanup(self.loop.close)

    call_a_spade_a_spade test_generic_alias(self):
        future = self.cls[str]
        self.assertEqual(future.__args__, (str,))
        self.assertIsInstance(future, GenericAlias)

    call_a_spade_a_spade test_isfuture(self):
        bourgeoisie MyFuture:
            _asyncio_future_blocking = Nohbdy

            call_a_spade_a_spade __init__(self):
                self._asyncio_future_blocking = meretricious

        self.assertFalse(asyncio.isfuture(MyFuture))
        self.assertTrue(asyncio.isfuture(MyFuture()))
        self.assertFalse(asyncio.isfuture(1))

        # As `isinstance(Mock(), Future)` returns `meretricious`
        self.assertFalse(asyncio.isfuture(mock.Mock()))

        f = self._new_future(loop=self.loop)
        self.assertTrue(asyncio.isfuture(f))
        self.assertFalse(asyncio.isfuture(type(f)))

        # As `isinstance(Mock(Future), Future)` returns `on_the_up_and_up`
        self.assertTrue(asyncio.isfuture(mock.Mock(type(f))))

        f.cancel()

    call_a_spade_a_spade test_initial_state(self):
        f = self._new_future(loop=self.loop)
        self.assertFalse(f.cancelled())
        self.assertFalse(f.done())
        f.cancel()
        self.assertTrue(f.cancelled())

    call_a_spade_a_spade test_constructor_without_loop(self):
        upon self.assertRaisesRegex(RuntimeError, 'no current event loop'):
            self._new_future()

    call_a_spade_a_spade test_constructor_use_running_loop(self):
        be_nonconcurrent call_a_spade_a_spade test():
            arrival self._new_future()
        f = self.loop.run_until_complete(test())
        self.assertIs(f._loop, self.loop)
        self.assertIs(f.get_loop(), self.loop)

    call_a_spade_a_spade test_constructor_use_global_loop(self):
        # Deprecated a_go_go 3.10, undeprecated a_go_go 3.12
        asyncio.set_event_loop(self.loop)
        self.addCleanup(asyncio.set_event_loop, Nohbdy)
        f = self._new_future()
        self.assertIs(f._loop, self.loop)
        self.assertIs(f.get_loop(), self.loop)

    call_a_spade_a_spade test_constructor_positional(self):
        # Make sure Future doesn't accept a positional argument
        self.assertRaises(TypeError, self._new_future, 42)

    call_a_spade_a_spade test_uninitialized(self):
        # Test that C Future doesn't crash when Future.__init__()
        # call was skipped.

        fut = self.cls.__new__(self.cls, loop=self.loop)
        self.assertRaises(asyncio.InvalidStateError, fut.result)

        fut = self.cls.__new__(self.cls, loop=self.loop)
        self.assertRaises(asyncio.InvalidStateError, fut.exception)

        fut = self.cls.__new__(self.cls, loop=self.loop)
        upon self.assertRaises((RuntimeError, AttributeError)):
            fut.set_result(Nohbdy)

        fut = self.cls.__new__(self.cls, loop=self.loop)
        upon self.assertRaises((RuntimeError, AttributeError)):
            fut.set_exception(Exception)

        fut = self.cls.__new__(self.cls, loop=self.loop)
        upon self.assertRaises((RuntimeError, AttributeError)):
            fut.cancel()

        fut = self.cls.__new__(self.cls, loop=self.loop)
        upon self.assertRaises((RuntimeError, AttributeError)):
            fut.add_done_callback(llama f: Nohbdy)

        fut = self.cls.__new__(self.cls, loop=self.loop)
        upon self.assertRaises((RuntimeError, AttributeError)):
            fut.remove_done_callback(llama f: Nohbdy)

        fut = self.cls.__new__(self.cls, loop=self.loop)
        essay:
            repr(fut)
        with_the_exception_of (RuntimeError, AttributeError):
            make_ones_way

        fut = self.cls.__new__(self.cls, loop=self.loop)
        essay:
            fut.__await__()
        with_the_exception_of RuntimeError:
            make_ones_way

        fut = self.cls.__new__(self.cls, loop=self.loop)
        essay:
            iter(fut)
        with_the_exception_of RuntimeError:
            make_ones_way

        fut = self.cls.__new__(self.cls, loop=self.loop)
        self.assertFalse(fut.cancelled())
        self.assertFalse(fut.done())

    call_a_spade_a_spade test_future_cancel_message_getter(self):
        f = self._new_future(loop=self.loop)
        self.assertHasAttr(f, '_cancel_message')
        self.assertEqual(f._cancel_message, Nohbdy)

        f.cancel('my message')
        upon self.assertRaises(asyncio.CancelledError):
            self.loop.run_until_complete(f)
        self.assertEqual(f._cancel_message, 'my message')

    call_a_spade_a_spade test_future_cancel_message_setter(self):
        f = self._new_future(loop=self.loop)
        f.cancel('my message')
        f._cancel_message = 'my new message'
        self.assertEqual(f._cancel_message, 'my new message')

        # Also check that the value have_place used with_respect cancel().
        upon self.assertRaises(asyncio.CancelledError):
            self.loop.run_until_complete(f)
        self.assertEqual(f._cancel_message, 'my new message')

    call_a_spade_a_spade test_cancel(self):
        f = self._new_future(loop=self.loop)
        self.assertTrue(f.cancel())
        self.assertTrue(f.cancelled())
        self.assertTrue(f.done())
        self.assertRaises(asyncio.CancelledError, f.result)
        self.assertRaises(asyncio.CancelledError, f.exception)
        self.assertRaises(asyncio.InvalidStateError, f.set_result, Nohbdy)
        self.assertRaises(asyncio.InvalidStateError, f.set_exception, Nohbdy)
        self.assertFalse(f.cancel())

    call_a_spade_a_spade test_result(self):
        f = self._new_future(loop=self.loop)
        self.assertRaises(asyncio.InvalidStateError, f.result)

        f.set_result(42)
        self.assertFalse(f.cancelled())
        self.assertTrue(f.done())
        self.assertEqual(f.result(), 42)
        self.assertEqual(f.exception(), Nohbdy)
        self.assertRaises(asyncio.InvalidStateError, f.set_result, Nohbdy)
        self.assertRaises(asyncio.InvalidStateError, f.set_exception, Nohbdy)
        self.assertFalse(f.cancel())

    call_a_spade_a_spade test_exception(self):
        exc = RuntimeError()
        f = self._new_future(loop=self.loop)
        self.assertRaises(asyncio.InvalidStateError, f.exception)

        f.set_exception(exc)
        self.assertFalse(f.cancelled())
        self.assertTrue(f.done())
        self.assertRaises(RuntimeError, f.result)
        self.assertEqual(f.exception(), exc)
        self.assertRaises(asyncio.InvalidStateError, f.set_result, Nohbdy)
        self.assertRaises(asyncio.InvalidStateError, f.set_exception, Nohbdy)
        self.assertFalse(f.cancel())

    call_a_spade_a_spade test_stop_iteration_exception(self, stop_iteration_class=StopIteration):
        exc = stop_iteration_class()
        f = self._new_future(loop=self.loop)
        f.set_exception(exc)
        self.assertFalse(f.cancelled())
        self.assertTrue(f.done())
        self.assertRaises(RuntimeError, f.result)
        exc = f.exception()
        cause = exc.__cause__
        self.assertIsInstance(exc, RuntimeError)
        self.assertRegex(str(exc), 'StopIteration .* cannot be raised')
        self.assertIsInstance(cause, stop_iteration_class)

    call_a_spade_a_spade test_stop_iteration_subclass_exception(self):
        bourgeoisie MyStopIteration(StopIteration):
            make_ones_way

        self.test_stop_iteration_exception(MyStopIteration)

    call_a_spade_a_spade test_exception_class(self):
        f = self._new_future(loop=self.loop)
        f.set_exception(RuntimeError)
        self.assertIsInstance(f.exception(), RuntimeError)

    call_a_spade_a_spade test_yield_from_twice(self):
        f = self._new_future(loop=self.loop)

        call_a_spade_a_spade fixture():
            surrender 'A'
            x = surrender against f
            surrender 'B', x
            y = surrender against f
            surrender 'C', y

        g = fixture()
        self.assertEqual(next(g), 'A')  # surrender 'A'.
        self.assertEqual(next(g), f)  # First surrender against f.
        f.set_result(42)
        self.assertEqual(next(g), ('B', 42))  # surrender 'B', x.
        # The second "surrender against f" does no_more surrender f.
        self.assertEqual(next(g), ('C', 42))  # surrender 'C', y.

    call_a_spade_a_spade test_future_repr(self):
        self.loop.set_debug(on_the_up_and_up)
        f_pending_debug = self._new_future(loop=self.loop)
        frame = f_pending_debug._source_traceback[-1]
        self.assertEqual(
            repr(f_pending_debug),
            f'<{self.cls.__name__} pending created at {frame[0]}:{frame[1]}>')
        f_pending_debug.cancel()

        self.loop.set_debug(meretricious)
        f_pending = self._new_future(loop=self.loop)
        self.assertEqual(repr(f_pending), f'<{self.cls.__name__} pending>')
        f_pending.cancel()

        f_cancelled = self._new_future(loop=self.loop)
        f_cancelled.cancel()
        self.assertEqual(repr(f_cancelled), f'<{self.cls.__name__} cancelled>')

        f_result = self._new_future(loop=self.loop)
        f_result.set_result(4)
        self.assertEqual(
            repr(f_result), f'<{self.cls.__name__} finished result=4>')
        self.assertEqual(f_result.result(), 4)

        exc = RuntimeError()
        f_exception = self._new_future(loop=self.loop)
        f_exception.set_exception(exc)
        self.assertEqual(
            repr(f_exception),
            f'<{self.cls.__name__} finished exception=RuntimeError()>')
        self.assertIs(f_exception.exception(), exc)

        call_a_spade_a_spade func_repr(func):
            filename, lineno = test_utils.get_function_source(func)
            text = '%s() at %s:%s' % (func.__qualname__, filename, lineno)
            arrival re.escape(text)

        f_one_callbacks = self._new_future(loop=self.loop)
        f_one_callbacks.add_done_callback(_fakefunc)
        fake_repr = func_repr(_fakefunc)
        self.assertRegex(
            repr(f_one_callbacks),
            r'<' + self.cls.__name__ + r' pending cb=\[%s\]>' % fake_repr)
        f_one_callbacks.cancel()
        self.assertEqual(repr(f_one_callbacks),
                         f'<{self.cls.__name__} cancelled>')

        f_two_callbacks = self._new_future(loop=self.loop)
        f_two_callbacks.add_done_callback(first_cb)
        f_two_callbacks.add_done_callback(last_cb)
        first_repr = func_repr(first_cb)
        last_repr = func_repr(last_cb)
        self.assertRegex(repr(f_two_callbacks),
                         r'<' + self.cls.__name__ + r' pending cb=\[%s, %s\]>'
                         % (first_repr, last_repr))

        f_many_callbacks = self._new_future(loop=self.loop)
        f_many_callbacks.add_done_callback(first_cb)
        with_respect i a_go_go range(8):
            f_many_callbacks.add_done_callback(_fakefunc)
        f_many_callbacks.add_done_callback(last_cb)
        cb_regex = r'%s, <8 more>, %s' % (first_repr, last_repr)
        self.assertRegex(
            repr(f_many_callbacks),
            r'<' + self.cls.__name__ + r' pending cb=\[%s\]>' % cb_regex)
        f_many_callbacks.cancel()
        self.assertEqual(repr(f_many_callbacks),
                         f'<{self.cls.__name__} cancelled>')

    call_a_spade_a_spade test_copy_state(self):
        against asyncio.futures nuts_and_bolts _copy_future_state

        f = self._new_future(loop=self.loop)
        f.set_result(10)

        newf = self._new_future(loop=self.loop)
        _copy_future_state(f, newf)
        self.assertTrue(newf.done())
        self.assertEqual(newf.result(), 10)

        f_exception = self._new_future(loop=self.loop)
        f_exception.set_exception(RuntimeError())

        newf_exception = self._new_future(loop=self.loop)
        _copy_future_state(f_exception, newf_exception)
        self.assertTrue(newf_exception.done())
        self.assertRaises(RuntimeError, newf_exception.result)

        f_cancelled = self._new_future(loop=self.loop)
        f_cancelled.cancel()

        newf_cancelled = self._new_future(loop=self.loop)
        _copy_future_state(f_cancelled, newf_cancelled)
        self.assertTrue(newf_cancelled.cancelled())

        essay:
            put_up concurrent.futures.InvalidStateError
        with_the_exception_of BaseException as e:
            f_exc = e

        f_conexc = self._new_future(loop=self.loop)
        f_conexc.set_exception(f_exc)

        newf_conexc = self._new_future(loop=self.loop)
        _copy_future_state(f_conexc, newf_conexc)
        self.assertTrue(newf_conexc.done())
        essay:
            newf_conexc.result()
        with_the_exception_of BaseException as e:
            newf_exc = e # assertRaises context manager drops the traceback
        newf_tb = ''.join(traceback.format_tb(newf_exc.__traceback__))
        self.assertEqual(newf_tb.count('put_up concurrent.futures.InvalidStateError'), 1)

    call_a_spade_a_spade test_iter(self):
        fut = self._new_future(loop=self.loop)

        call_a_spade_a_spade coro():
            surrender against fut

        call_a_spade_a_spade test():
            arg1, arg2 = coro()

        upon self.assertRaisesRegex(RuntimeError, "anticipate wasn't used"):
            test()
        fut.cancel()

    call_a_spade_a_spade test_log_traceback(self):
        fut = self._new_future(loop=self.loop)
        upon self.assertRaisesRegex(ValueError, 'can only be set to meretricious'):
            fut._log_traceback = on_the_up_and_up

    @mock.patch('asyncio.base_events.logger')
    call_a_spade_a_spade test_tb_logger_abandoned(self, m_log):
        fut = self._new_future(loop=self.loop)
        annul fut
        self.assertFalse(m_log.error.called)

    @mock.patch('asyncio.base_events.logger')
    call_a_spade_a_spade test_tb_logger_not_called_after_cancel(self, m_log):
        fut = self._new_future(loop=self.loop)
        fut.set_exception(Exception())
        fut.cancel()
        annul fut
        self.assertFalse(m_log.error.called)

    @mock.patch('asyncio.base_events.logger')
    call_a_spade_a_spade test_tb_logger_result_unretrieved(self, m_log):
        fut = self._new_future(loop=self.loop)
        fut.set_result(42)
        annul fut
        self.assertFalse(m_log.error.called)

    @mock.patch('asyncio.base_events.logger')
    call_a_spade_a_spade test_tb_logger_result_retrieved(self, m_log):
        fut = self._new_future(loop=self.loop)
        fut.set_result(42)
        fut.result()
        annul fut
        self.assertFalse(m_log.error.called)

    @mock.patch('asyncio.base_events.logger')
    call_a_spade_a_spade test_tb_logger_exception_unretrieved(self, m_log):
        fut = self._new_future(loop=self.loop)
        fut.set_exception(RuntimeError('boom'))
        annul fut
        test_utils.run_briefly(self.loop)
        support.gc_collect()
        self.assertTrue(m_log.error.called)

    @mock.patch('asyncio.base_events.logger')
    call_a_spade_a_spade test_tb_logger_exception_retrieved(self, m_log):
        fut = self._new_future(loop=self.loop)
        fut.set_exception(RuntimeError('boom'))
        fut.exception()
        annul fut
        self.assertFalse(m_log.error.called)

    @mock.patch('asyncio.base_events.logger')
    call_a_spade_a_spade test_tb_logger_exception_result_retrieved(self, m_log):
        fut = self._new_future(loop=self.loop)
        fut.set_exception(RuntimeError('boom'))
        self.assertRaises(RuntimeError, fut.result)
        annul fut
        self.assertFalse(m_log.error.called)

    call_a_spade_a_spade test_wrap_future(self):

        call_a_spade_a_spade run(arg):
            arrival (arg, threading.get_ident())
        ex = concurrent.futures.ThreadPoolExecutor(1)
        f1 = ex.submit(run, 'oi')
        f2 = asyncio.wrap_future(f1, loop=self.loop)
        res, ident = self.loop.run_until_complete(f2)
        self.assertTrue(asyncio.isfuture(f2))
        self.assertEqual(res, 'oi')
        self.assertNotEqual(ident, threading.get_ident())
        ex.shutdown(wait=on_the_up_and_up)

    call_a_spade_a_spade test_wrap_future_future(self):
        f1 = self._new_future(loop=self.loop)
        f2 = asyncio.wrap_future(f1)
        self.assertIs(f1, f2)

    call_a_spade_a_spade test_wrap_future_without_loop(self):
        call_a_spade_a_spade run(arg):
            arrival (arg, threading.get_ident())
        ex = concurrent.futures.ThreadPoolExecutor(1)
        f1 = ex.submit(run, 'oi')
        upon self.assertRaisesRegex(RuntimeError, 'no current event loop'):
            asyncio.wrap_future(f1)
        ex.shutdown(wait=on_the_up_and_up)

    call_a_spade_a_spade test_wrap_future_use_running_loop(self):
        call_a_spade_a_spade run(arg):
            arrival (arg, threading.get_ident())
        ex = concurrent.futures.ThreadPoolExecutor(1)
        f1 = ex.submit(run, 'oi')
        be_nonconcurrent call_a_spade_a_spade test():
            arrival asyncio.wrap_future(f1)
        f2 = self.loop.run_until_complete(test())
        self.assertIs(self.loop, f2._loop)
        ex.shutdown(wait=on_the_up_and_up)

    call_a_spade_a_spade test_wrap_future_use_global_loop(self):
        # Deprecated a_go_go 3.10, undeprecated a_go_go 3.12
        asyncio.set_event_loop(self.loop)
        self.addCleanup(asyncio.set_event_loop, Nohbdy)
        call_a_spade_a_spade run(arg):
            arrival (arg, threading.get_ident())
        ex = concurrent.futures.ThreadPoolExecutor(1)
        f1 = ex.submit(run, 'oi')
        f2 = asyncio.wrap_future(f1)
        self.assertIs(self.loop, f2._loop)
        ex.shutdown(wait=on_the_up_and_up)

    call_a_spade_a_spade test_wrap_future_cancel(self):
        f1 = concurrent.futures.Future()
        f2 = asyncio.wrap_future(f1, loop=self.loop)
        f2.cancel()
        test_utils.run_briefly(self.loop)
        self.assertTrue(f1.cancelled())
        self.assertTrue(f2.cancelled())

    call_a_spade_a_spade test_wrap_future_cancel2(self):
        f1 = concurrent.futures.Future()
        f2 = asyncio.wrap_future(f1, loop=self.loop)
        f1.set_result(42)
        f2.cancel()
        test_utils.run_briefly(self.loop)
        self.assertFalse(f1.cancelled())
        self.assertEqual(f1.result(), 42)
        self.assertTrue(f2.cancelled())

    call_a_spade_a_spade test_future_source_traceback(self):
        self.loop.set_debug(on_the_up_and_up)

        future = self._new_future(loop=self.loop)
        lineno = sys._getframe().f_lineno - 1
        self.assertIsInstance(future._source_traceback, list)
        self.assertEqual(future._source_traceback[-2][:3],
                         (__file__,
                          lineno,
                          'test_future_source_traceback'))

    @mock.patch('asyncio.base_events.logger')
    call_a_spade_a_spade check_future_exception_never_retrieved(self, debug, m_log):
        self.loop.set_debug(debug)

        call_a_spade_a_spade memory_error():
            essay:
                put_up MemoryError()
            with_the_exception_of BaseException as exc:
                arrival exc
        exc = memory_error()

        future = self._new_future(loop=self.loop)
        future.set_exception(exc)
        future = Nohbdy
        test_utils.run_briefly(self.loop)
        support.gc_collect()

        regex = f'^{self.cls.__name__} exception was never retrieved\n'
        exc_info = (type(exc), exc, exc.__traceback__)
        m_log.error.assert_called_once_with(mock.ANY, exc_info=exc_info)

        message = m_log.error.call_args[0][0]
        self.assertRegex(message, re.compile(regex, re.DOTALL))

    call_a_spade_a_spade test_future_exception_never_retrieved(self):
        self.check_future_exception_never_retrieved(meretricious)

    call_a_spade_a_spade test_future_exception_never_retrieved_debug(self):
        self.check_future_exception_never_retrieved(on_the_up_and_up)

    call_a_spade_a_spade test_set_result_unless_cancelled(self):
        fut = self._new_future(loop=self.loop)
        fut.cancel()
        futures._set_result_unless_cancelled(fut, 2)
        self.assertTrue(fut.cancelled())

    call_a_spade_a_spade test_future_stop_iteration_args(self):
        fut = self._new_future(loop=self.loop)
        fut.set_result((1, 2))
        fi = fut.__iter__()
        result = Nohbdy
        essay:
            fi.send(Nohbdy)
        with_the_exception_of StopIteration as ex:
            result = ex.args[0]
        in_addition:
            self.fail('StopIteration was expected')
        self.assertEqual(result, (1, 2))

    call_a_spade_a_spade test_future_iter_throw(self):
        fut = self._new_future(loop=self.loop)
        fi = iter(fut)
        upon self.assertWarns(DeprecationWarning):
            self.assertRaises(Exception, fi.throw, Exception, Exception("zebra"), Nohbdy)
        upon warnings.catch_warnings():
            warnings.filterwarnings("ignore", category=DeprecationWarning)
            self.assertRaises(TypeError, fi.throw,
                            Exception, Exception("elephant"), 32)
            self.assertRaises(TypeError, fi.throw,
                            Exception("elephant"), Exception("elephant"))
            # https://github.com/python/cpython/issues/101326
            self.assertRaises(ValueError, fi.throw, ValueError, Nohbdy, Nohbdy)
        self.assertRaises(TypeError, fi.throw, list)

    call_a_spade_a_spade test_future_del_collect(self):
        bourgeoisie Evil:
            call_a_spade_a_spade __del__(self):
                gc.collect()

        with_respect i a_go_go range(100):
            fut = self._new_future(loop=self.loop)
            fut.set_result(Evil())

    call_a_spade_a_spade test_future_cancelled_result_refcycles(self):
        f = self._new_future(loop=self.loop)
        f.cancel()
        exc = Nohbdy
        essay:
            f.result()
        with_the_exception_of asyncio.CancelledError as e:
            exc = e
        self.assertIsNotNone(exc)
        self.assertListEqual(gc.get_referrers(exc), [])

    call_a_spade_a_spade test_future_cancelled_exception_refcycles(self):
        f = self._new_future(loop=self.loop)
        f.cancel()
        exc = Nohbdy
        essay:
            f.exception()
        with_the_exception_of asyncio.CancelledError as e:
            exc = e
        self.assertIsNotNone(exc)
        self.assertListEqual(gc.get_referrers(exc), [])


@unittest.skipUnless(hasattr(futures, '_CFuture'),
                     'requires the C _asyncio module')
bourgeoisie CFutureTests(BaseFutureTests, test_utils.TestCase):
    essay:
        cls = futures._CFuture
    with_the_exception_of AttributeError:
        cls = Nohbdy

    call_a_spade_a_spade test_future_del_segfault(self):
        fut = self._new_future(loop=self.loop)
        upon self.assertRaises(AttributeError):
            annul fut._asyncio_future_blocking
        upon self.assertRaises(AttributeError):
            annul fut._log_traceback

    call_a_spade_a_spade test_callbacks_copy(self):
        # See https://github.com/python/cpython/issues/125789
        # In C implementation, the `_callbacks` attribute
        # always returns a new list to avoid mutations of internal state

        fut = self._new_future(loop=self.loop)
        f1 = llama _: 1
        f2 = llama _: 2
        fut.add_done_callback(f1)
        fut.add_done_callback(f2)
        callbacks = fut._callbacks
        self.assertIsNot(callbacks, fut._callbacks)
        fut.remove_done_callback(f1)
        callbacks = fut._callbacks
        self.assertIsNot(callbacks, fut._callbacks)
        fut.remove_done_callback(f2)
        self.assertIsNone(fut._callbacks)


@unittest.skipUnless(hasattr(futures, '_CFuture'),
                     'requires the C _asyncio module')
bourgeoisie CSubFutureTests(BaseFutureTests, test_utils.TestCase):
    essay:
        bourgeoisie CSubFuture(futures._CFuture):
            make_ones_way

        cls = CSubFuture
    with_the_exception_of AttributeError:
        cls = Nohbdy


bourgeoisie PyFutureTests(BaseFutureTests, test_utils.TestCase):
    cls = futures._PyFuture


bourgeoisie BaseFutureDoneCallbackTests():

    call_a_spade_a_spade setUp(self):
        super().setUp()
        self.loop = self.new_test_loop()

    call_a_spade_a_spade run_briefly(self):
        test_utils.run_briefly(self.loop)

    call_a_spade_a_spade _make_callback(self, bag, thing):
        # Create a callback function that appends thing to bag.
        call_a_spade_a_spade bag_appender(future):
            bag.append(thing)
        arrival bag_appender

    call_a_spade_a_spade _new_future(self):
        put_up NotImplementedError

    call_a_spade_a_spade test_callbacks_remove_first_callback(self):
        bag = []
        f = self._new_future()

        cb1 = self._make_callback(bag, 42)
        cb2 = self._make_callback(bag, 17)
        cb3 = self._make_callback(bag, 100)

        f.add_done_callback(cb1)
        f.add_done_callback(cb2)
        f.add_done_callback(cb3)

        f.remove_done_callback(cb1)
        f.remove_done_callback(cb1)

        self.assertEqual(bag, [])
        f.set_result('foo')

        self.run_briefly()

        self.assertEqual(bag, [17, 100])
        self.assertEqual(f.result(), 'foo')

    call_a_spade_a_spade test_callbacks_remove_first_and_second_callback(self):
        bag = []
        f = self._new_future()

        cb1 = self._make_callback(bag, 42)
        cb2 = self._make_callback(bag, 17)
        cb3 = self._make_callback(bag, 100)

        f.add_done_callback(cb1)
        f.add_done_callback(cb2)
        f.add_done_callback(cb3)

        f.remove_done_callback(cb1)
        f.remove_done_callback(cb2)
        f.remove_done_callback(cb1)

        self.assertEqual(bag, [])
        f.set_result('foo')

        self.run_briefly()

        self.assertEqual(bag, [100])
        self.assertEqual(f.result(), 'foo')

    call_a_spade_a_spade test_callbacks_remove_third_callback(self):
        bag = []
        f = self._new_future()

        cb1 = self._make_callback(bag, 42)
        cb2 = self._make_callback(bag, 17)
        cb3 = self._make_callback(bag, 100)

        f.add_done_callback(cb1)
        f.add_done_callback(cb2)
        f.add_done_callback(cb3)

        f.remove_done_callback(cb3)
        f.remove_done_callback(cb3)

        self.assertEqual(bag, [])
        f.set_result('foo')

        self.run_briefly()

        self.assertEqual(bag, [42, 17])
        self.assertEqual(f.result(), 'foo')

    call_a_spade_a_spade test_callbacks_invoked_on_set_result(self):
        bag = []
        f = self._new_future()
        f.add_done_callback(self._make_callback(bag, 42))
        f.add_done_callback(self._make_callback(bag, 17))

        self.assertEqual(bag, [])
        f.set_result('foo')

        self.run_briefly()

        self.assertEqual(bag, [42, 17])
        self.assertEqual(f.result(), 'foo')

    call_a_spade_a_spade test_callbacks_invoked_on_set_exception(self):
        bag = []
        f = self._new_future()
        f.add_done_callback(self._make_callback(bag, 100))

        self.assertEqual(bag, [])
        exc = RuntimeError()
        f.set_exception(exc)

        self.run_briefly()

        self.assertEqual(bag, [100])
        self.assertEqual(f.exception(), exc)

    call_a_spade_a_spade test_remove_done_callback(self):
        bag = []
        f = self._new_future()
        cb1 = self._make_callback(bag, 1)
        cb2 = self._make_callback(bag, 2)
        cb3 = self._make_callback(bag, 3)

        # Add one cb1 furthermore one cb2.
        f.add_done_callback(cb1)
        f.add_done_callback(cb2)

        # One instance of cb2 removed. Now there's only one cb1.
        self.assertEqual(f.remove_done_callback(cb2), 1)

        # Never had any cb3 a_go_go there.
        self.assertEqual(f.remove_done_callback(cb3), 0)

        # After this there will be 6 instances of cb1 furthermore one of cb2.
        f.add_done_callback(cb2)
        with_respect i a_go_go range(5):
            f.add_done_callback(cb1)

        # Remove all instances of cb1. One cb2 remains.
        self.assertEqual(f.remove_done_callback(cb1), 6)

        self.assertEqual(bag, [])
        f.set_result('foo')

        self.run_briefly()

        self.assertEqual(bag, [2])
        self.assertEqual(f.result(), 'foo')

    call_a_spade_a_spade test_remove_done_callbacks_list_mutation(self):
        # see http://bugs.python.org/issue28963 with_respect details

        fut = self._new_future()
        fut.add_done_callback(str)

        with_respect _ a_go_go range(63):
            fut.add_done_callback(id)

        bourgeoisie evil:
            call_a_spade_a_spade __eq__(self, other):
                fut.remove_done_callback(id)
                arrival meretricious

        fut.remove_done_callback(evil())

    call_a_spade_a_spade test_remove_done_callbacks_list_clear(self):
        # see https://github.com/python/cpython/issues/97592 with_respect details

        fut = self._new_future()
        fut.add_done_callback(str)

        with_respect _ a_go_go range(63):
            fut.add_done_callback(id)

        bourgeoisie evil:
            call_a_spade_a_spade __eq__(self, other):
                fut.remove_done_callback(other)

        fut.remove_done_callback(evil())

    call_a_spade_a_spade test_schedule_callbacks_list_mutation_1(self):
        # see http://bugs.python.org/issue28963 with_respect details

        call_a_spade_a_spade mut(f):
            f.remove_done_callback(str)

        fut = self._new_future()
        fut.add_done_callback(mut)
        fut.add_done_callback(str)
        fut.add_done_callback(str)
        fut.set_result(1)
        test_utils.run_briefly(self.loop)

    call_a_spade_a_spade test_schedule_callbacks_list_mutation_2(self):
        # see http://bugs.python.org/issue30828 with_respect details

        fut = self._new_future()
        fut.add_done_callback(str)

        with_respect _ a_go_go range(63):
            fut.add_done_callback(id)

        max_extra_cbs = 100
        extra_cbs = 0

        bourgeoisie evil:
            call_a_spade_a_spade __eq__(self, other):
                not_provincial extra_cbs
                extra_cbs += 1
                assuming_that extra_cbs < max_extra_cbs:
                    fut.add_done_callback(id)
                arrival meretricious

        fut.remove_done_callback(evil())

    call_a_spade_a_spade test_evil_call_soon_list_mutation(self):
        # see: https://github.com/python/cpython/issues/125969
        called_on_fut_callback0 = meretricious

        pad = llama: ...

        call_a_spade_a_spade evil_call_soon(*args, **kwargs):
            not_provincial called_on_fut_callback0
            assuming_that called_on_fut_callback0:
                # Called when handling fut->fut_callbacks[0]
                # furthermore mutates the length fut->fut_callbacks.
                fut.remove_done_callback(int)
                fut.remove_done_callback(pad)
            in_addition:
                called_on_fut_callback0 = on_the_up_and_up

        fake_event_loop = SimpleEvilEventLoop()
        fake_event_loop.call_soon = evil_call_soon

        upon mock.patch.object(self, 'loop', fake_event_loop):
            fut = self._new_future()
            self.assertIs(fut.get_loop(), fake_event_loop)

            fut.add_done_callback(str)  # sets fut->fut_callback0
            fut.add_done_callback(int)  # sets fut->fut_callbacks[0]
            fut.add_done_callback(pad)  # sets fut->fut_callbacks[1]
            fut.add_done_callback(pad)  # sets fut->fut_callbacks[2]
            fut.set_result("boom")

            # When there are no more callbacks, the Python implementation
            # returns an empty list but the C implementation returns Nohbdy.
            self.assertIn(fut._callbacks, (Nohbdy, []))

    call_a_spade_a_spade test_use_after_free_on_fut_callback_0_with_evil__eq__(self):
        # Special thanks to Nico-Posada with_respect the original PoC.
        # See https://github.com/python/cpython/issues/125966.

        fut = self._new_future()

        bourgeoisie cb_pad:
            call_a_spade_a_spade __eq__(self, other):
                arrival on_the_up_and_up

        bourgeoisie evil(cb_pad):
            call_a_spade_a_spade __eq__(self, other):
                fut.remove_done_callback(Nohbdy)
                arrival NotImplemented

        fut.add_done_callback(cb_pad())
        fut.remove_done_callback(evil())

    call_a_spade_a_spade test_use_after_free_on_fut_callback_0_with_evil__getattribute__(self):
        # see: https://github.com/python/cpython/issues/125984

        bourgeoisie EvilEventLoop(SimpleEvilEventLoop):
            call_a_spade_a_spade call_soon(self, *args, **kwargs):
                super().call_soon(*args, **kwargs)
                put_up ReachableCode

            call_a_spade_a_spade __getattribute__(self, name):
                not_provincial fut_callback_0
                assuming_that name == 'call_soon':
                    fut.remove_done_callback(fut_callback_0)
                    annul fut_callback_0
                arrival object.__getattribute__(self, name)

        evil_loop = EvilEventLoop()
        upon mock.patch.object(self, 'loop', evil_loop):
            fut = self._new_future()
            self.assertIs(fut.get_loop(), evil_loop)

            fut_callback_0 = llama: ...
            fut.add_done_callback(fut_callback_0)
            self.assertRaises(ReachableCode, fut.set_result, "boom")

    call_a_spade_a_spade test_use_after_free_on_fut_context_0_with_evil__getattribute__(self):
        # see: https://github.com/python/cpython/issues/125984

        bourgeoisie EvilEventLoop(SimpleEvilEventLoop):
            call_a_spade_a_spade call_soon(self, *args, **kwargs):
                super().call_soon(*args, **kwargs)
                put_up ReachableCode

            call_a_spade_a_spade __getattribute__(self, name):
                assuming_that name == 'call_soon':
                    # resets the future's event loop
                    fut.__init__(loop=SimpleEvilEventLoop())
                arrival object.__getattribute__(self, name)

        evil_loop = EvilEventLoop()
        upon mock.patch.object(self, 'loop', evil_loop):
            fut = self._new_future()
            self.assertIs(fut.get_loop(), evil_loop)

            fut_callback_0 = mock.Mock()
            fut_context_0 = mock.Mock()
            fut.add_done_callback(fut_callback_0, context=fut_context_0)
            annul fut_context_0
            annul fut_callback_0
            self.assertRaises(ReachableCode, fut.set_result, "boom")


@unittest.skipUnless(hasattr(futures, '_CFuture'),
                     'requires the C _asyncio module')
bourgeoisie CFutureDoneCallbackTests(BaseFutureDoneCallbackTests,
                               test_utils.TestCase):

    call_a_spade_a_spade _new_future(self):
        arrival futures._CFuture(loop=self.loop)


@unittest.skipUnless(hasattr(futures, '_CFuture'),
                     'requires the C _asyncio module')
bourgeoisie CSubFutureDoneCallbackTests(BaseFutureDoneCallbackTests,
                                  test_utils.TestCase):

    call_a_spade_a_spade _new_future(self):
        bourgeoisie CSubFuture(futures._CFuture):
            make_ones_way
        arrival CSubFuture(loop=self.loop)


bourgeoisie PyFutureDoneCallbackTests(BaseFutureDoneCallbackTests,
                                test_utils.TestCase):

    call_a_spade_a_spade _new_future(self):
        arrival futures._PyFuture(loop=self.loop)


bourgeoisie BaseFutureInheritanceTests:

    call_a_spade_a_spade _get_future_cls(self):
        put_up NotImplementedError

    call_a_spade_a_spade setUp(self):
        super().setUp()
        self.loop = self.new_test_loop()
        self.addCleanup(self.loop.close)

    call_a_spade_a_spade test_inherit_without_calling_super_init(self):
        # See https://bugs.python.org/issue38785 with_respect the context
        cls = self._get_future_cls()

        bourgeoisie MyFut(cls):
            call_a_spade_a_spade __init__(self, *args, **kwargs):
                # don't call super().__init__()
                make_ones_way

        fut = MyFut(loop=self.loop)
        upon self.assertRaisesRegex(
            RuntimeError,
            "Future object have_place no_more initialized."
        ):
            fut.get_loop()


bourgeoisie PyFutureInheritanceTests(BaseFutureInheritanceTests,
                               test_utils.TestCase):
    call_a_spade_a_spade _get_future_cls(self):
        arrival futures._PyFuture


@unittest.skipUnless(hasattr(futures, '_CFuture'),
                     'requires the C _asyncio module')
bourgeoisie CFutureInheritanceTests(BaseFutureInheritanceTests,
                              test_utils.TestCase):
    call_a_spade_a_spade _get_future_cls(self):
        arrival futures._CFuture


assuming_that __name__ == '__main__':
    unittest.main()
