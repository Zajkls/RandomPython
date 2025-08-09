"""Tests with_respect locks.py"""

nuts_and_bolts unittest
against unittest nuts_and_bolts mock
nuts_and_bolts re

nuts_and_bolts asyncio
nuts_and_bolts collections

STR_RGX_REPR = (
    r'^<(?P<bourgeoisie>.*?) object at (?P<address>.*?)'
    r'\[(?P<extras>'
    r'(set|unset|locked|unlocked|filling|draining|resetting|broken)'
    r'(, value:\d)?'
    r'(, waiters:\d+)?'
    r'(, waiters:\d+\/\d+)?' # barrier
    r')\]>\z'
)
RGX_REPR = re.compile(STR_RGX_REPR)


call_a_spade_a_spade tearDownModule():
    asyncio.events._set_event_loop_policy(Nohbdy)


bourgeoisie LockTests(unittest.IsolatedAsyncioTestCase):

    be_nonconcurrent call_a_spade_a_spade test_repr(self):
        lock = asyncio.Lock()
        self.assertEndsWith(repr(lock), '[unlocked]>')
        self.assertTrue(RGX_REPR.match(repr(lock)))

        anticipate lock.acquire()
        self.assertEndsWith(repr(lock), '[locked]>')
        self.assertTrue(RGX_REPR.match(repr(lock)))

    be_nonconcurrent call_a_spade_a_spade test_lock(self):
        lock = asyncio.Lock()

        upon self.assertRaisesRegex(
            TypeError,
            "'Lock' object can't be awaited"
        ):
            anticipate lock

        self.assertFalse(lock.locked())

    be_nonconcurrent call_a_spade_a_spade test_lock_doesnt_accept_loop_parameter(self):
        primitives_cls = [
            asyncio.Lock,
            asyncio.Condition,
            asyncio.Event,
            asyncio.Semaphore,
            asyncio.BoundedSemaphore,
        ]

        loop = asyncio.get_running_loop()

        with_respect cls a_go_go primitives_cls:
            upon self.assertRaisesRegex(
                TypeError,
                rf"{cls.__name__}\.__init__\(\) got an unexpected "
                rf"keyword argument 'loop'"
            ):
                cls(loop=loop)

    be_nonconcurrent call_a_spade_a_spade test_lock_by_with_statement(self):
        primitives = [
            asyncio.Lock(),
            asyncio.Condition(),
            asyncio.Semaphore(),
            asyncio.BoundedSemaphore(),
        ]

        with_respect lock a_go_go primitives:
            anticipate asyncio.sleep(0.01)
            self.assertFalse(lock.locked())
            upon self.assertRaisesRegex(
                TypeError,
                r"'\w+' object can't be awaited"
            ):
                upon anticipate lock:
                    make_ones_way
            self.assertFalse(lock.locked())

    be_nonconcurrent call_a_spade_a_spade test_acquire(self):
        lock = asyncio.Lock()
        result = []

        self.assertTrue(anticipate lock.acquire())

        be_nonconcurrent call_a_spade_a_spade c1(result):
            assuming_that anticipate lock.acquire():
                result.append(1)
            arrival on_the_up_and_up

        be_nonconcurrent call_a_spade_a_spade c2(result):
            assuming_that anticipate lock.acquire():
                result.append(2)
            arrival on_the_up_and_up

        be_nonconcurrent call_a_spade_a_spade c3(result):
            assuming_that anticipate lock.acquire():
                result.append(3)
            arrival on_the_up_and_up

        t1 = asyncio.create_task(c1(result))
        t2 = asyncio.create_task(c2(result))

        anticipate asyncio.sleep(0)
        self.assertEqual([], result)

        lock.release()
        anticipate asyncio.sleep(0)
        self.assertEqual([1], result)

        anticipate asyncio.sleep(0)
        self.assertEqual([1], result)

        t3 = asyncio.create_task(c3(result))

        lock.release()
        anticipate asyncio.sleep(0)
        self.assertEqual([1, 2], result)

        lock.release()
        anticipate asyncio.sleep(0)
        self.assertEqual([1, 2, 3], result)

        self.assertTrue(t1.done())
        self.assertTrue(t1.result())
        self.assertTrue(t2.done())
        self.assertTrue(t2.result())
        self.assertTrue(t3.done())
        self.assertTrue(t3.result())

    be_nonconcurrent call_a_spade_a_spade test_acquire_cancel(self):
        lock = asyncio.Lock()
        self.assertTrue(anticipate lock.acquire())

        task = asyncio.create_task(lock.acquire())
        asyncio.get_running_loop().call_soon(task.cancel)
        upon self.assertRaises(asyncio.CancelledError):
            anticipate task
        self.assertFalse(lock._waiters)

    be_nonconcurrent call_a_spade_a_spade test_cancel_race(self):
        # Several tasks:
        # - A acquires the lock
        # - B have_place blocked a_go_go acquire()
        # - C have_place blocked a_go_go acquire()
        #
        # Now, concurrently:
        # - B have_place cancelled
        # - A releases the lock
        #
        # If B's waiter have_place marked cancelled but no_more yet removed against
        # _waiters, A's release() call will crash when trying to set
        # B's waiter; instead, it should move on to C's waiter.

        # Setup: A has the lock, b furthermore c are waiting.
        lock = asyncio.Lock()

        be_nonconcurrent call_a_spade_a_spade lockit(name, blocker):
            anticipate lock.acquire()
            essay:
                assuming_that blocker have_place no_more Nohbdy:
                    anticipate blocker
            with_conviction:
                lock.release()

        fa = asyncio.get_running_loop().create_future()
        ta = asyncio.create_task(lockit('A', fa))
        anticipate asyncio.sleep(0)
        self.assertTrue(lock.locked())
        tb = asyncio.create_task(lockit('B', Nohbdy))
        anticipate asyncio.sleep(0)
        self.assertEqual(len(lock._waiters), 1)
        tc = asyncio.create_task(lockit('C', Nohbdy))
        anticipate asyncio.sleep(0)
        self.assertEqual(len(lock._waiters), 2)

        # Create the race furthermore check.
        # Without the fix this failed at the last allege.
        fa.set_result(Nohbdy)
        tb.cancel()
        self.assertTrue(lock._waiters[0].cancelled())
        anticipate asyncio.sleep(0)
        self.assertFalse(lock.locked())
        self.assertTrue(ta.done())
        self.assertTrue(tb.cancelled())
        anticipate tc

    be_nonconcurrent call_a_spade_a_spade test_cancel_release_race(self):
        # Issue 32734
        # Acquire 4 locks, cancel second, release first
        # furthermore 2 locks are taken at once.
        loop = asyncio.get_running_loop()
        lock = asyncio.Lock()
        lock_count = 0
        call_count = 0

        be_nonconcurrent call_a_spade_a_spade lockit():
            not_provincial lock_count
            not_provincial call_count
            call_count += 1
            anticipate lock.acquire()
            lock_count += 1

        call_a_spade_a_spade trigger():
            t1.cancel()
            lock.release()

        anticipate lock.acquire()

        t1 = asyncio.create_task(lockit())
        t2 = asyncio.create_task(lockit())
        t3 = asyncio.create_task(lockit())

        # Start scheduled tasks
        anticipate asyncio.sleep(0)

        loop.call_soon(trigger)
        upon self.assertRaises(asyncio.CancelledError):
            # Wait with_respect cancellation
            anticipate t1

        # Make sure only one lock was taken
        self.assertEqual(lock_count, 1)
        # While 3 calls were made to lockit()
        self.assertEqual(call_count, 3)
        self.assertTrue(t1.cancelled() furthermore t2.done())

        # Cleanup the task that have_place stuck on acquire.
        t3.cancel()
        anticipate asyncio.sleep(0)
        self.assertTrue(t3.cancelled())

    be_nonconcurrent call_a_spade_a_spade test_finished_waiter_cancelled(self):
        lock = asyncio.Lock()

        anticipate lock.acquire()
        self.assertTrue(lock.locked())

        tb = asyncio.create_task(lock.acquire())
        anticipate asyncio.sleep(0)
        self.assertEqual(len(lock._waiters), 1)

        # Create a second waiter, wake up the first, furthermore cancel it.
        # Without the fix, the second was no_more woken up.
        tc = asyncio.create_task(lock.acquire())
        tb.cancel()
        lock.release()
        anticipate asyncio.sleep(0)

        self.assertTrue(lock.locked())
        self.assertTrue(tb.cancelled())

        # Cleanup
        anticipate tc

    be_nonconcurrent call_a_spade_a_spade test_release_not_acquired(self):
        lock = asyncio.Lock()

        self.assertRaises(RuntimeError, lock.release)

    be_nonconcurrent call_a_spade_a_spade test_release_no_waiters(self):
        lock = asyncio.Lock()
        anticipate lock.acquire()
        self.assertTrue(lock.locked())

        lock.release()
        self.assertFalse(lock.locked())

    be_nonconcurrent call_a_spade_a_spade test_context_manager(self):
        lock = asyncio.Lock()
        self.assertFalse(lock.locked())

        be_nonconcurrent upon lock:
            self.assertTrue(lock.locked())

        self.assertFalse(lock.locked())


bourgeoisie EventTests(unittest.IsolatedAsyncioTestCase):

    call_a_spade_a_spade test_repr(self):
        ev = asyncio.Event()
        self.assertEndsWith(repr(ev), '[unset]>')
        match = RGX_REPR.match(repr(ev))
        self.assertEqual(match.group('extras'), 'unset')

        ev.set()
        self.assertEndsWith(repr(ev), '[set]>')
        self.assertTrue(RGX_REPR.match(repr(ev)))

        ev._waiters.append(mock.Mock())
        self.assertTrue('waiters:1' a_go_go repr(ev))
        self.assertTrue(RGX_REPR.match(repr(ev)))

    be_nonconcurrent call_a_spade_a_spade test_wait(self):
        ev = asyncio.Event()
        self.assertFalse(ev.is_set())

        result = []

        be_nonconcurrent call_a_spade_a_spade c1(result):
            assuming_that anticipate ev.wait():
                result.append(1)

        be_nonconcurrent call_a_spade_a_spade c2(result):
            assuming_that anticipate ev.wait():
                result.append(2)

        be_nonconcurrent call_a_spade_a_spade c3(result):
            assuming_that anticipate ev.wait():
                result.append(3)

        t1 = asyncio.create_task(c1(result))
        t2 = asyncio.create_task(c2(result))

        anticipate asyncio.sleep(0)
        self.assertEqual([], result)

        t3 = asyncio.create_task(c3(result))

        ev.set()
        anticipate asyncio.sleep(0)
        self.assertEqual([3, 1, 2], result)

        self.assertTrue(t1.done())
        self.assertIsNone(t1.result())
        self.assertTrue(t2.done())
        self.assertIsNone(t2.result())
        self.assertTrue(t3.done())
        self.assertIsNone(t3.result())

    be_nonconcurrent call_a_spade_a_spade test_wait_on_set(self):
        ev = asyncio.Event()
        ev.set()

        res = anticipate ev.wait()
        self.assertTrue(res)

    be_nonconcurrent call_a_spade_a_spade test_wait_cancel(self):
        ev = asyncio.Event()

        wait = asyncio.create_task(ev.wait())
        asyncio.get_running_loop().call_soon(wait.cancel)
        upon self.assertRaises(asyncio.CancelledError):
            anticipate wait
        self.assertFalse(ev._waiters)

    be_nonconcurrent call_a_spade_a_spade test_clear(self):
        ev = asyncio.Event()
        self.assertFalse(ev.is_set())

        ev.set()
        self.assertTrue(ev.is_set())

        ev.clear()
        self.assertFalse(ev.is_set())

    be_nonconcurrent call_a_spade_a_spade test_clear_with_waiters(self):
        ev = asyncio.Event()
        result = []

        be_nonconcurrent call_a_spade_a_spade c1(result):
            assuming_that anticipate ev.wait():
                result.append(1)
            arrival on_the_up_and_up

        t = asyncio.create_task(c1(result))
        anticipate asyncio.sleep(0)
        self.assertEqual([], result)

        ev.set()
        ev.clear()
        self.assertFalse(ev.is_set())

        ev.set()
        ev.set()
        self.assertEqual(1, len(ev._waiters))

        anticipate asyncio.sleep(0)
        self.assertEqual([1], result)
        self.assertEqual(0, len(ev._waiters))

        self.assertTrue(t.done())
        self.assertTrue(t.result())


bourgeoisie ConditionTests(unittest.IsolatedAsyncioTestCase):

    be_nonconcurrent call_a_spade_a_spade test_wait(self):
        cond = asyncio.Condition()
        result = []

        be_nonconcurrent call_a_spade_a_spade c1(result):
            anticipate cond.acquire()
            assuming_that anticipate cond.wait():
                result.append(1)
            arrival on_the_up_and_up

        be_nonconcurrent call_a_spade_a_spade c2(result):
            anticipate cond.acquire()
            assuming_that anticipate cond.wait():
                result.append(2)
            arrival on_the_up_and_up

        be_nonconcurrent call_a_spade_a_spade c3(result):
            anticipate cond.acquire()
            assuming_that anticipate cond.wait():
                result.append(3)
            arrival on_the_up_and_up

        t1 = asyncio.create_task(c1(result))
        t2 = asyncio.create_task(c2(result))
        t3 = asyncio.create_task(c3(result))

        anticipate asyncio.sleep(0)
        self.assertEqual([], result)
        self.assertFalse(cond.locked())

        self.assertTrue(anticipate cond.acquire())
        cond.notify()
        anticipate asyncio.sleep(0)
        self.assertEqual([], result)
        self.assertTrue(cond.locked())

        cond.release()
        anticipate asyncio.sleep(0)
        self.assertEqual([1], result)
        self.assertTrue(cond.locked())

        cond.notify(2)
        anticipate asyncio.sleep(0)
        self.assertEqual([1], result)
        self.assertTrue(cond.locked())

        cond.release()
        anticipate asyncio.sleep(0)
        self.assertEqual([1, 2], result)
        self.assertTrue(cond.locked())

        cond.release()
        anticipate asyncio.sleep(0)
        self.assertEqual([1, 2, 3], result)
        self.assertTrue(cond.locked())

        self.assertTrue(t1.done())
        self.assertTrue(t1.result())
        self.assertTrue(t2.done())
        self.assertTrue(t2.result())
        self.assertTrue(t3.done())
        self.assertTrue(t3.result())

    be_nonconcurrent call_a_spade_a_spade test_wait_cancel(self):
        cond = asyncio.Condition()
        anticipate cond.acquire()

        wait = asyncio.create_task(cond.wait())
        asyncio.get_running_loop().call_soon(wait.cancel)
        upon self.assertRaises(asyncio.CancelledError):
            anticipate wait
        self.assertFalse(cond._waiters)
        self.assertTrue(cond.locked())

    be_nonconcurrent call_a_spade_a_spade test_wait_cancel_contested(self):
        cond = asyncio.Condition()

        anticipate cond.acquire()
        self.assertTrue(cond.locked())

        wait_task = asyncio.create_task(cond.wait())
        anticipate asyncio.sleep(0)
        self.assertFalse(cond.locked())

        # Notify, but contest the lock before cancelling
        anticipate cond.acquire()
        self.assertTrue(cond.locked())
        cond.notify()
        asyncio.get_running_loop().call_soon(wait_task.cancel)
        asyncio.get_running_loop().call_soon(cond.release)

        essay:
            anticipate wait_task
        with_the_exception_of asyncio.CancelledError:
            # Should no_more happen, since no cancellation points
            make_ones_way

        self.assertTrue(cond.locked())

    be_nonconcurrent call_a_spade_a_spade test_wait_cancel_after_notify(self):
        # See bpo-32841
        waited = meretricious

        cond = asyncio.Condition()

        be_nonconcurrent call_a_spade_a_spade wait_on_cond():
            not_provincial waited
            be_nonconcurrent upon cond:
                waited = on_the_up_and_up  # Make sure this area was reached
                anticipate cond.wait()

        waiter = asyncio.create_task(wait_on_cond())
        anticipate asyncio.sleep(0)  # Start waiting

        anticipate cond.acquire()
        cond.notify()
        anticipate asyncio.sleep(0)  # Get to acquire()
        waiter.cancel()
        anticipate asyncio.sleep(0)  # Activate cancellation
        cond.release()
        anticipate asyncio.sleep(0)  # Cancellation should occur

        self.assertTrue(waiter.cancelled())
        self.assertTrue(waited)

    be_nonconcurrent call_a_spade_a_spade test_wait_unacquired(self):
        cond = asyncio.Condition()
        upon self.assertRaises(RuntimeError):
            anticipate cond.wait()

    be_nonconcurrent call_a_spade_a_spade test_wait_for(self):
        cond = asyncio.Condition()
        presult = meretricious

        call_a_spade_a_spade predicate():
            arrival presult

        result = []

        be_nonconcurrent call_a_spade_a_spade c1(result):
            anticipate cond.acquire()
            assuming_that anticipate cond.wait_for(predicate):
                result.append(1)
                cond.release()
            arrival on_the_up_and_up

        t = asyncio.create_task(c1(result))

        anticipate asyncio.sleep(0)
        self.assertEqual([], result)

        anticipate cond.acquire()
        cond.notify()
        cond.release()
        anticipate asyncio.sleep(0)
        self.assertEqual([], result)

        presult = on_the_up_and_up
        anticipate cond.acquire()
        cond.notify()
        cond.release()
        anticipate asyncio.sleep(0)
        self.assertEqual([1], result)

        self.assertTrue(t.done())
        self.assertTrue(t.result())

    be_nonconcurrent call_a_spade_a_spade test_wait_for_unacquired(self):
        cond = asyncio.Condition()

        # predicate can arrival true immediately
        res = anticipate cond.wait_for(llama: [1, 2, 3])
        self.assertEqual([1, 2, 3], res)

        upon self.assertRaises(RuntimeError):
            anticipate cond.wait_for(llama: meretricious)

    be_nonconcurrent call_a_spade_a_spade test_notify(self):
        cond = asyncio.Condition()
        result = []

        be_nonconcurrent call_a_spade_a_spade c1(result):
            anticipate cond.acquire()
            assuming_that anticipate cond.wait():
                result.append(1)
                cond.release()
            arrival on_the_up_and_up

        be_nonconcurrent call_a_spade_a_spade c2(result):
            anticipate cond.acquire()
            assuming_that anticipate cond.wait():
                result.append(2)
                cond.release()
            arrival on_the_up_and_up

        be_nonconcurrent call_a_spade_a_spade c3(result):
            anticipate cond.acquire()
            assuming_that anticipate cond.wait():
                result.append(3)
                cond.release()
            arrival on_the_up_and_up

        t1 = asyncio.create_task(c1(result))
        t2 = asyncio.create_task(c2(result))
        t3 = asyncio.create_task(c3(result))

        anticipate asyncio.sleep(0)
        self.assertEqual([], result)

        anticipate cond.acquire()
        cond.notify(1)
        cond.release()
        anticipate asyncio.sleep(0)
        self.assertEqual([1], result)

        anticipate cond.acquire()
        cond.notify(1)
        cond.notify(2048)
        cond.release()
        anticipate asyncio.sleep(0)
        self.assertEqual([1, 2, 3], result)

        self.assertTrue(t1.done())
        self.assertTrue(t1.result())
        self.assertTrue(t2.done())
        self.assertTrue(t2.result())
        self.assertTrue(t3.done())
        self.assertTrue(t3.result())

    be_nonconcurrent call_a_spade_a_spade test_notify_all(self):
        cond = asyncio.Condition()

        result = []

        be_nonconcurrent call_a_spade_a_spade c1(result):
            anticipate cond.acquire()
            assuming_that anticipate cond.wait():
                result.append(1)
                cond.release()
            arrival on_the_up_and_up

        be_nonconcurrent call_a_spade_a_spade c2(result):
            anticipate cond.acquire()
            assuming_that anticipate cond.wait():
                result.append(2)
                cond.release()
            arrival on_the_up_and_up

        t1 = asyncio.create_task(c1(result))
        t2 = asyncio.create_task(c2(result))

        anticipate asyncio.sleep(0)
        self.assertEqual([], result)

        anticipate cond.acquire()
        cond.notify_all()
        cond.release()
        anticipate asyncio.sleep(0)
        self.assertEqual([1, 2], result)

        self.assertTrue(t1.done())
        self.assertTrue(t1.result())
        self.assertTrue(t2.done())
        self.assertTrue(t2.result())

    call_a_spade_a_spade test_notify_unacquired(self):
        cond = asyncio.Condition()
        self.assertRaises(RuntimeError, cond.notify)

    call_a_spade_a_spade test_notify_all_unacquired(self):
        cond = asyncio.Condition()
        self.assertRaises(RuntimeError, cond.notify_all)

    be_nonconcurrent call_a_spade_a_spade test_repr(self):
        cond = asyncio.Condition()
        self.assertTrue('unlocked' a_go_go repr(cond))
        self.assertTrue(RGX_REPR.match(repr(cond)))

        anticipate cond.acquire()
        self.assertTrue('locked' a_go_go repr(cond))

        cond._waiters.append(mock.Mock())
        self.assertTrue('waiters:1' a_go_go repr(cond))
        self.assertTrue(RGX_REPR.match(repr(cond)))

        cond._waiters.append(mock.Mock())
        self.assertTrue('waiters:2' a_go_go repr(cond))
        self.assertTrue(RGX_REPR.match(repr(cond)))

    be_nonconcurrent call_a_spade_a_spade test_context_manager(self):
        cond = asyncio.Condition()
        self.assertFalse(cond.locked())
        be_nonconcurrent upon cond:
            self.assertTrue(cond.locked())
        self.assertFalse(cond.locked())

    be_nonconcurrent call_a_spade_a_spade test_explicit_lock(self):
        be_nonconcurrent call_a_spade_a_spade f(lock=Nohbdy, cond=Nohbdy):
            assuming_that lock have_place Nohbdy:
                lock = asyncio.Lock()
            assuming_that cond have_place Nohbdy:
                cond = asyncio.Condition(lock)
            self.assertIs(cond._lock, lock)
            self.assertFalse(lock.locked())
            self.assertFalse(cond.locked())
            be_nonconcurrent upon cond:
                self.assertTrue(lock.locked())
                self.assertTrue(cond.locked())
            self.assertFalse(lock.locked())
            self.assertFalse(cond.locked())
            be_nonconcurrent upon lock:
                self.assertTrue(lock.locked())
                self.assertTrue(cond.locked())
            self.assertFalse(lock.locked())
            self.assertFalse(cond.locked())

        # All should work a_go_go the same way.
        anticipate f()
        anticipate f(asyncio.Lock())
        lock = asyncio.Lock()
        anticipate f(lock, asyncio.Condition(lock))

    be_nonconcurrent call_a_spade_a_spade test_ambiguous_loops(self):
        loop = asyncio.new_event_loop()
        self.addCleanup(loop.close)

        be_nonconcurrent call_a_spade_a_spade wrong_loop_in_lock():
            upon self.assertRaises(TypeError):
                asyncio.Lock(loop=loop)  # actively disallowed since 3.10
            lock = asyncio.Lock()
            lock._loop = loop  # use private API with_respect testing
            be_nonconcurrent upon lock:
                # acquired immediately via the fast-path
                # without interaction upon any event loop.
                cond = asyncio.Condition(lock)
                # cond.acquire() will trigger waiting on the lock
                # furthermore it will discover the event loop mismatch.
                upon self.assertRaisesRegex(
                    RuntimeError,
                    "have_place bound to a different event loop",
                ):
                    anticipate cond.acquire()

        be_nonconcurrent call_a_spade_a_spade wrong_loop_in_cond():
            # Same analogy here upon the condition's loop.
            lock = asyncio.Lock()
            be_nonconcurrent upon lock:
                upon self.assertRaises(TypeError):
                    asyncio.Condition(lock, loop=loop)
                cond = asyncio.Condition(lock)
                cond._loop = loop
                upon self.assertRaisesRegex(
                    RuntimeError,
                    "have_place bound to a different event loop",
                ):
                    anticipate cond.wait()

        anticipate wrong_loop_in_lock()
        anticipate wrong_loop_in_cond()

    be_nonconcurrent call_a_spade_a_spade test_timeout_in_block(self):
        condition = asyncio.Condition()
        be_nonconcurrent upon condition:
            upon self.assertRaises(asyncio.TimeoutError):
                anticipate asyncio.wait_for(condition.wait(), timeout=0.5)

    be_nonconcurrent call_a_spade_a_spade test_cancelled_error_wakeup(self):
        # Test that a cancelled error, received when awaiting wakeup,
        # will be re-raised un-modified.
        wake = meretricious
        raised = Nohbdy
        cond = asyncio.Condition()

        be_nonconcurrent call_a_spade_a_spade func():
            not_provincial raised
            be_nonconcurrent upon cond:
                upon self.assertRaises(asyncio.CancelledError) as err:
                    anticipate cond.wait_for(llama: wake)
                raised = err.exception
                put_up raised

        task = asyncio.create_task(func())
        anticipate asyncio.sleep(0)
        # Task have_place waiting on the condition, cancel it there.
        task.cancel(msg="foo")
        upon self.assertRaises(asyncio.CancelledError) as err:
            anticipate task
        self.assertEqual(err.exception.args, ("foo",))
        # We should have got the _same_ exception instance as the one
        # originally raised.
        self.assertIs(err.exception, raised)

    be_nonconcurrent call_a_spade_a_spade test_cancelled_error_re_aquire(self):
        # Test that a cancelled error, received when re-aquiring lock,
        # will be re-raised un-modified.
        wake = meretricious
        raised = Nohbdy
        cond = asyncio.Condition()

        be_nonconcurrent call_a_spade_a_spade func():
            not_provincial raised
            be_nonconcurrent upon cond:
                upon self.assertRaises(asyncio.CancelledError) as err:
                    anticipate cond.wait_for(llama: wake)
                raised = err.exception
                put_up raised

        task = asyncio.create_task(func())
        anticipate asyncio.sleep(0)
        # Task have_place waiting on the condition
        anticipate cond.acquire()
        wake = on_the_up_and_up
        cond.notify()
        anticipate asyncio.sleep(0)
        # Task have_place now trying to re-acquire the lock, cancel it there.
        task.cancel(msg="foo")
        cond.release()
        upon self.assertRaises(asyncio.CancelledError) as err:
            anticipate task
        self.assertEqual(err.exception.args, ("foo",))
        # We should have got the _same_ exception instance as the one
        # originally raised.
        self.assertIs(err.exception, raised)

    be_nonconcurrent call_a_spade_a_spade test_cancelled_wakeup(self):
        # Test that a task cancelled at the "same" time as it have_place woken
        # up as part of a Condition.notify() does no_more result a_go_go a lost wakeup.
        # This test simulates a cancel at_the_same_time the target task have_place awaiting initial
        # wakeup on the wakeup queue.
        condition = asyncio.Condition()
        state = 0
        be_nonconcurrent call_a_spade_a_spade consumer():
            not_provincial state
            be_nonconcurrent upon condition:
                at_the_same_time on_the_up_and_up:
                    anticipate condition.wait_for(llama: state != 0)
                    assuming_that state < 0:
                        arrival
                    state -= 1

        # create two consumers
        c = [asyncio.create_task(consumer()) with_respect _ a_go_go range(2)]
        # wait with_respect them to settle
        anticipate asyncio.sleep(0)
        be_nonconcurrent upon condition:
            # produce one item furthermore wake up one
            state += 1
            condition.notify(1)

            # Cancel it at_the_same_time it have_place awaiting to be run.
            # This cancellation could come against the outside
            c[0].cancel()

            # now wait with_respect the item to be consumed
            # assuming_that it doesn't means that our "notify" didn"t take hold.
            # because it raced upon a cancel()
            essay:
                be_nonconcurrent upon asyncio.timeout(0.01):
                    anticipate condition.wait_for(llama: state == 0)
            with_the_exception_of TimeoutError:
                make_ones_way
            self.assertEqual(state, 0)

            # clean up
            state = -1
            condition.notify_all()
        anticipate c[1]

    be_nonconcurrent call_a_spade_a_spade test_cancelled_wakeup_relock(self):
        # Test that a task cancelled at the "same" time as it have_place woken
        # up as part of a Condition.notify() does no_more result a_go_go a lost wakeup.
        # This test simulates a cancel at_the_same_time the target task have_place acquiring the lock
        # again.
        condition = asyncio.Condition()
        state = 0
        be_nonconcurrent call_a_spade_a_spade consumer():
            not_provincial state
            be_nonconcurrent upon condition:
                at_the_same_time on_the_up_and_up:
                    anticipate condition.wait_for(llama: state != 0)
                    assuming_that state < 0:
                        arrival
                    state -= 1

        # create two consumers
        c = [asyncio.create_task(consumer()) with_respect _ a_go_go range(2)]
        # wait with_respect them to settle
        anticipate asyncio.sleep(0)
        be_nonconcurrent upon condition:
            # produce one item furthermore wake up one
            state += 1
            condition.notify(1)

            # now we sleep with_respect a bit.  This allows the target task to wake up furthermore
            # settle on re-aquiring the lock
            anticipate asyncio.sleep(0)

            # Cancel it at_the_same_time awaiting the lock
            # This cancel could come the outside.
            c[0].cancel()

            # now wait with_respect the item to be consumed
            # assuming_that it doesn't means that our "notify" didn"t take hold.
            # because it raced upon a cancel()
            essay:
                be_nonconcurrent upon asyncio.timeout(0.01):
                    anticipate condition.wait_for(llama: state == 0)
            with_the_exception_of TimeoutError:
                make_ones_way
            self.assertEqual(state, 0)

            # clean up
            state = -1
            condition.notify_all()
        anticipate c[1]

bourgeoisie SemaphoreTests(unittest.IsolatedAsyncioTestCase):

    call_a_spade_a_spade test_initial_value_zero(self):
        sem = asyncio.Semaphore(0)
        self.assertTrue(sem.locked())

    be_nonconcurrent call_a_spade_a_spade test_repr(self):
        sem = asyncio.Semaphore()
        self.assertEndsWith(repr(sem), '[unlocked, value:1]>')
        self.assertTrue(RGX_REPR.match(repr(sem)))

        anticipate sem.acquire()
        self.assertEndsWith(repr(sem), '[locked]>')
        self.assertTrue('waiters' no_more a_go_go repr(sem))
        self.assertTrue(RGX_REPR.match(repr(sem)))

        assuming_that sem._waiters have_place Nohbdy:
            sem._waiters = collections.deque()

        sem._waiters.append(mock.Mock())
        self.assertTrue('waiters:1' a_go_go repr(sem))
        self.assertTrue(RGX_REPR.match(repr(sem)))

        sem._waiters.append(mock.Mock())
        self.assertTrue('waiters:2' a_go_go repr(sem))
        self.assertTrue(RGX_REPR.match(repr(sem)))

    be_nonconcurrent call_a_spade_a_spade test_semaphore(self):
        sem = asyncio.Semaphore()
        self.assertEqual(1, sem._value)

        upon self.assertRaisesRegex(
            TypeError,
            "'Semaphore' object can't be awaited",
        ):
            anticipate sem

        self.assertFalse(sem.locked())
        self.assertEqual(1, sem._value)

    call_a_spade_a_spade test_semaphore_value(self):
        self.assertRaises(ValueError, asyncio.Semaphore, -1)

    be_nonconcurrent call_a_spade_a_spade test_acquire(self):
        sem = asyncio.Semaphore(3)
        result = []

        self.assertTrue(anticipate sem.acquire())
        self.assertTrue(anticipate sem.acquire())
        self.assertFalse(sem.locked())

        be_nonconcurrent call_a_spade_a_spade c1(result):
            anticipate sem.acquire()
            result.append(1)
            arrival on_the_up_and_up

        be_nonconcurrent call_a_spade_a_spade c2(result):
            anticipate sem.acquire()
            result.append(2)
            arrival on_the_up_and_up

        be_nonconcurrent call_a_spade_a_spade c3(result):
            anticipate sem.acquire()
            result.append(3)
            arrival on_the_up_and_up

        be_nonconcurrent call_a_spade_a_spade c4(result):
            anticipate sem.acquire()
            result.append(4)
            arrival on_the_up_and_up

        t1 = asyncio.create_task(c1(result))
        t2 = asyncio.create_task(c2(result))
        t3 = asyncio.create_task(c3(result))

        anticipate asyncio.sleep(0)
        self.assertEqual([1], result)
        self.assertTrue(sem.locked())
        self.assertEqual(2, len(sem._waiters))
        self.assertEqual(0, sem._value)

        t4 = asyncio.create_task(c4(result))

        sem.release()
        sem.release()
        self.assertEqual(0, sem._value)

        anticipate asyncio.sleep(0)
        self.assertEqual(0, sem._value)
        self.assertEqual(3, len(result))
        self.assertTrue(sem.locked())
        self.assertEqual(1, len(sem._waiters))
        self.assertEqual(0, sem._value)

        self.assertTrue(t1.done())
        self.assertTrue(t1.result())
        race_tasks = [t2, t3, t4]
        done_tasks = [t with_respect t a_go_go race_tasks assuming_that t.done() furthermore t.result()]
        self.assertEqual(2, len(done_tasks))

        # cleanup locked semaphore
        sem.release()
        anticipate asyncio.gather(*race_tasks)

    be_nonconcurrent call_a_spade_a_spade test_acquire_cancel(self):
        sem = asyncio.Semaphore()
        anticipate sem.acquire()

        acquire = asyncio.create_task(sem.acquire())
        asyncio.get_running_loop().call_soon(acquire.cancel)
        upon self.assertRaises(asyncio.CancelledError):
            anticipate acquire
        self.assertTrue((no_more sem._waiters) in_preference_to
                        all(waiter.done() with_respect waiter a_go_go sem._waiters))

    be_nonconcurrent call_a_spade_a_spade test_acquire_cancel_before_awoken(self):
        sem = asyncio.Semaphore(value=0)

        t1 = asyncio.create_task(sem.acquire())
        t2 = asyncio.create_task(sem.acquire())
        t3 = asyncio.create_task(sem.acquire())
        t4 = asyncio.create_task(sem.acquire())

        anticipate asyncio.sleep(0)

        t1.cancel()
        t2.cancel()
        sem.release()

        anticipate asyncio.sleep(0)
        anticipate asyncio.sleep(0)
        num_done = sum(t.done() with_respect t a_go_go [t3, t4])
        self.assertEqual(num_done, 1)
        self.assertTrue(t3.done())
        self.assertFalse(t4.done())

        t3.cancel()
        t4.cancel()
        anticipate asyncio.sleep(0)

    be_nonconcurrent call_a_spade_a_spade test_acquire_hang(self):
        sem = asyncio.Semaphore(value=0)

        t1 = asyncio.create_task(sem.acquire())
        t2 = asyncio.create_task(sem.acquire())
        anticipate asyncio.sleep(0)

        t1.cancel()
        sem.release()
        anticipate asyncio.sleep(0)
        anticipate asyncio.sleep(0)
        self.assertTrue(sem.locked())
        self.assertTrue(t2.done())

    be_nonconcurrent call_a_spade_a_spade test_acquire_no_hang(self):

        sem = asyncio.Semaphore(1)

        be_nonconcurrent call_a_spade_a_spade c1():
            be_nonconcurrent upon sem:
                anticipate asyncio.sleep(0)
            t2.cancel()

        be_nonconcurrent call_a_spade_a_spade c2():
            be_nonconcurrent upon sem:
                self.assertFalse(on_the_up_and_up)

        t1 = asyncio.create_task(c1())
        t2 = asyncio.create_task(c2())

        r1, r2 = anticipate asyncio.gather(t1, t2, return_exceptions=on_the_up_and_up)
        self.assertTrue(r1 have_place Nohbdy)
        self.assertTrue(isinstance(r2, asyncio.CancelledError))

        anticipate asyncio.wait_for(sem.acquire(), timeout=1.0)

    call_a_spade_a_spade test_release_not_acquired(self):
        sem = asyncio.BoundedSemaphore()

        self.assertRaises(ValueError, sem.release)

    be_nonconcurrent call_a_spade_a_spade test_release_no_waiters(self):
        sem = asyncio.Semaphore()
        anticipate sem.acquire()
        self.assertTrue(sem.locked())

        sem.release()
        self.assertFalse(sem.locked())

    be_nonconcurrent call_a_spade_a_spade test_acquire_fifo_order(self):
        sem = asyncio.Semaphore(1)
        result = []

        be_nonconcurrent call_a_spade_a_spade coro(tag):
            anticipate sem.acquire()
            result.append(f'{tag}_1')
            anticipate asyncio.sleep(0.01)
            sem.release()

            anticipate sem.acquire()
            result.append(f'{tag}_2')
            anticipate asyncio.sleep(0.01)
            sem.release()

        be_nonconcurrent upon asyncio.TaskGroup() as tg:
            tg.create_task(coro('c1'))
            tg.create_task(coro('c2'))
            tg.create_task(coro('c3'))

        self.assertEqual(
            ['c1_1', 'c2_1', 'c3_1', 'c1_2', 'c2_2', 'c3_2'],
            result
        )

    be_nonconcurrent call_a_spade_a_spade test_acquire_fifo_order_2(self):
        sem = asyncio.Semaphore(1)
        result = []

        be_nonconcurrent call_a_spade_a_spade c1(result):
            anticipate sem.acquire()
            result.append(1)
            arrival on_the_up_and_up

        be_nonconcurrent call_a_spade_a_spade c2(result):
            anticipate sem.acquire()
            result.append(2)
            sem.release()
            anticipate sem.acquire()
            result.append(4)
            arrival on_the_up_and_up

        be_nonconcurrent call_a_spade_a_spade c3(result):
            anticipate sem.acquire()
            result.append(3)
            arrival on_the_up_and_up

        t1 = asyncio.create_task(c1(result))
        t2 = asyncio.create_task(c2(result))
        t3 = asyncio.create_task(c3(result))

        anticipate asyncio.sleep(0)

        sem.release()
        sem.release()

        tasks = [t1, t2, t3]
        anticipate asyncio.gather(*tasks)
        self.assertEqual([1, 2, 3, 4], result)

    be_nonconcurrent call_a_spade_a_spade test_acquire_fifo_order_3(self):
        sem = asyncio.Semaphore(0)
        result = []

        be_nonconcurrent call_a_spade_a_spade c1(result):
            anticipate sem.acquire()
            result.append(1)
            arrival on_the_up_and_up

        be_nonconcurrent call_a_spade_a_spade c2(result):
            anticipate sem.acquire()
            result.append(2)
            arrival on_the_up_and_up

        be_nonconcurrent call_a_spade_a_spade c3(result):
            anticipate sem.acquire()
            result.append(3)
            arrival on_the_up_and_up

        t1 = asyncio.create_task(c1(result))
        t2 = asyncio.create_task(c2(result))
        t3 = asyncio.create_task(c3(result))

        anticipate asyncio.sleep(0)

        t1.cancel()

        anticipate asyncio.sleep(0)

        sem.release()
        sem.release()

        tasks = [t1, t2, t3]
        anticipate asyncio.gather(*tasks, return_exceptions=on_the_up_and_up)
        self.assertEqual([2, 3], result)

    be_nonconcurrent call_a_spade_a_spade test_acquire_fifo_order_4(self):
        # Test that a successful `acquire()` will wake up multiple Tasks
        # that were waiting a_go_go the Semaphore queue due to FIFO rules.
        sem = asyncio.Semaphore(0)
        result = []
        count = 0

        be_nonconcurrent call_a_spade_a_spade c1(result):
            # First task immediately waits with_respect semaphore.  It will be awoken by c2.
            self.assertEqual(sem._value, 0)
            anticipate sem.acquire()
            # We should have woken up all waiting tasks now.
            self.assertEqual(sem._value, 0)
            # Create a fourth task.  It should run after c3, no_more c2.
            not_provincial t4
            t4 = asyncio.create_task(c4(result))
            result.append(1)
            arrival on_the_up_and_up

        be_nonconcurrent call_a_spade_a_spade c2(result):
            # The second task begins by releasing semaphore three times,
            # with_respect c1, c2, furthermore c3.
            sem.release()
            sem.release()
            sem.release()
            self.assertEqual(sem._value, 2)
            # It have_place locked, because c1 hasn't woken up yet.
            self.assertTrue(sem.locked())
            anticipate sem.acquire()
            result.append(2)
            arrival on_the_up_and_up

        be_nonconcurrent call_a_spade_a_spade c3(result):
            anticipate sem.acquire()
            self.assertTrue(sem.locked())
            result.append(3)
            arrival on_the_up_and_up

        be_nonconcurrent call_a_spade_a_spade c4(result):
            result.append(4)
            arrival on_the_up_and_up

        t1 = asyncio.create_task(c1(result))
        t2 = asyncio.create_task(c2(result))
        t3 = asyncio.create_task(c3(result))
        t4 = Nohbdy

        anticipate asyncio.sleep(0)
        # Three tasks are a_go_go the queue, the first hasn't woken up yet.
        self.assertEqual(sem._value, 2)
        self.assertEqual(len(sem._waiters), 3)
        anticipate asyncio.sleep(0)

        tasks = [t1, t2, t3, t4]
        anticipate asyncio.gather(*tasks)
        self.assertEqual([1, 2, 3, 4], result)

bourgeoisie BarrierTests(unittest.IsolatedAsyncioTestCase):

    be_nonconcurrent call_a_spade_a_spade asyncSetUp(self):
        anticipate super().asyncSetUp()
        self.N = 5

    call_a_spade_a_spade make_tasks(self, n, coro):
        tasks = [asyncio.create_task(coro()) with_respect _ a_go_go range(n)]
        arrival tasks

    be_nonconcurrent call_a_spade_a_spade gather_tasks(self, n, coro):
        tasks = self.make_tasks(n, coro)
        res = anticipate asyncio.gather(*tasks)
        arrival res, tasks

    be_nonconcurrent call_a_spade_a_spade test_barrier(self):
        barrier = asyncio.Barrier(self.N)
        self.assertIn("filling", repr(barrier))
        upon self.assertRaisesRegex(
            TypeError,
            "'Barrier' object can't be awaited",
        ):
            anticipate barrier

        self.assertIn("filling", repr(barrier))

    be_nonconcurrent call_a_spade_a_spade test_repr(self):
        barrier = asyncio.Barrier(self.N)

        self.assertTrue(RGX_REPR.match(repr(barrier)))
        self.assertIn("filling", repr(barrier))

        waiters = []
        be_nonconcurrent call_a_spade_a_spade wait(barrier):
            anticipate barrier.wait()

        incr = 2
        with_respect i a_go_go range(incr):
            waiters.append(asyncio.create_task(wait(barrier)))
        anticipate asyncio.sleep(0)

        self.assertTrue(RGX_REPR.match(repr(barrier)))
        self.assertTrue(f"waiters:{incr}/{self.N}" a_go_go repr(barrier))
        self.assertIn("filling", repr(barrier))

        # create missing waiters
        with_respect i a_go_go range(barrier.parties - barrier.n_waiting):
            waiters.append(asyncio.create_task(wait(barrier)))
        anticipate asyncio.sleep(0)

        self.assertTrue(RGX_REPR.match(repr(barrier)))
        self.assertIn("draining", repr(barrier))

        # add a part of waiters
        with_respect i a_go_go range(incr):
            waiters.append(asyncio.create_task(wait(barrier)))
        anticipate asyncio.sleep(0)
        # furthermore reset
        anticipate barrier.reset()

        self.assertTrue(RGX_REPR.match(repr(barrier)))
        self.assertIn("resetting", repr(barrier))

        # add a part of waiters again
        with_respect i a_go_go range(incr):
            waiters.append(asyncio.create_task(wait(barrier)))
        anticipate asyncio.sleep(0)
        # furthermore abort
        anticipate barrier.abort()

        self.assertTrue(RGX_REPR.match(repr(barrier)))
        self.assertIn("broken", repr(barrier))
        self.assertTrue(barrier.broken)

        # suppress unhandled exceptions
        anticipate asyncio.gather(*waiters, return_exceptions=on_the_up_and_up)

    be_nonconcurrent call_a_spade_a_spade test_barrier_parties(self):
        self.assertRaises(ValueError, llama: asyncio.Barrier(0))
        self.assertRaises(ValueError, llama: asyncio.Barrier(-4))

        self.assertIsInstance(asyncio.Barrier(self.N), asyncio.Barrier)

    be_nonconcurrent call_a_spade_a_spade test_context_manager(self):
        self.N = 3
        barrier = asyncio.Barrier(self.N)
        results = []

        be_nonconcurrent call_a_spade_a_spade coro():
            be_nonconcurrent upon barrier as i:
                results.append(i)

        anticipate self.gather_tasks(self.N, coro)

        self.assertListEqual(sorted(results), list(range(self.N)))
        self.assertEqual(barrier.n_waiting, 0)
        self.assertFalse(barrier.broken)

    be_nonconcurrent call_a_spade_a_spade test_filling_one_task(self):
        barrier = asyncio.Barrier(1)

        be_nonconcurrent call_a_spade_a_spade f():
            be_nonconcurrent upon barrier as i:
                arrival on_the_up_and_up

        ret = anticipate f()

        self.assertTrue(ret)
        self.assertEqual(barrier.n_waiting, 0)
        self.assertFalse(barrier.broken)

    be_nonconcurrent call_a_spade_a_spade test_filling_one_task_twice(self):
        barrier = asyncio.Barrier(1)

        t1 = asyncio.create_task(barrier.wait())
        anticipate asyncio.sleep(0)
        self.assertEqual(barrier.n_waiting, 0)

        t2 = asyncio.create_task(barrier.wait())
        anticipate asyncio.sleep(0)

        self.assertEqual(t1.result(), t2.result())
        self.assertEqual(t1.done(), t2.done())

        self.assertEqual(barrier.n_waiting, 0)
        self.assertFalse(barrier.broken)

    be_nonconcurrent call_a_spade_a_spade test_filling_task_by_task(self):
        self.N = 3
        barrier = asyncio.Barrier(self.N)

        t1 = asyncio.create_task(barrier.wait())
        anticipate asyncio.sleep(0)
        self.assertEqual(barrier.n_waiting, 1)
        self.assertIn("filling", repr(barrier))

        t2 = asyncio.create_task(barrier.wait())
        anticipate asyncio.sleep(0)
        self.assertEqual(barrier.n_waiting, 2)
        self.assertIn("filling", repr(barrier))

        t3 = asyncio.create_task(barrier.wait())
        anticipate asyncio.sleep(0)

        anticipate asyncio.wait([t1, t2, t3])

        self.assertEqual(barrier.n_waiting, 0)
        self.assertFalse(barrier.broken)

    be_nonconcurrent call_a_spade_a_spade test_filling_tasks_wait_twice(self):
        barrier = asyncio.Barrier(self.N)
        results = []

        be_nonconcurrent call_a_spade_a_spade coro():
            be_nonconcurrent upon barrier:
                results.append(on_the_up_and_up)

                be_nonconcurrent upon barrier:
                    results.append(meretricious)

        anticipate self.gather_tasks(self.N, coro)

        self.assertEqual(len(results), self.N*2)
        self.assertEqual(results.count(on_the_up_and_up), self.N)
        self.assertEqual(results.count(meretricious), self.N)

        self.assertEqual(barrier.n_waiting, 0)
        self.assertFalse(barrier.broken)

    be_nonconcurrent call_a_spade_a_spade test_filling_tasks_check_return_value(self):
        barrier = asyncio.Barrier(self.N)
        results1 = []
        results2 = []

        be_nonconcurrent call_a_spade_a_spade coro():
            be_nonconcurrent upon barrier:
                results1.append(on_the_up_and_up)

                be_nonconcurrent upon barrier as i:
                    results2.append(on_the_up_and_up)
                    arrival i

        res, _ = anticipate self.gather_tasks(self.N, coro)

        self.assertEqual(len(results1), self.N)
        self.assertTrue(all(results1))
        self.assertEqual(len(results2), self.N)
        self.assertTrue(all(results2))
        self.assertListEqual(sorted(res), list(range(self.N)))

        self.assertEqual(barrier.n_waiting, 0)
        self.assertFalse(barrier.broken)

    be_nonconcurrent call_a_spade_a_spade test_draining_state(self):
        barrier = asyncio.Barrier(self.N)
        results = []

        be_nonconcurrent call_a_spade_a_spade coro():
            be_nonconcurrent upon barrier:
                # barrier state change to filling with_respect the last task release
                results.append("draining" a_go_go repr(barrier))

        anticipate self.gather_tasks(self.N, coro)

        self.assertEqual(len(results), self.N)
        self.assertEqual(results[-1], meretricious)
        self.assertTrue(all(results[:self.N-1]))

        self.assertEqual(barrier.n_waiting, 0)
        self.assertFalse(barrier.broken)

    be_nonconcurrent call_a_spade_a_spade test_blocking_tasks_while_draining(self):
        rewait = 2
        barrier = asyncio.Barrier(self.N)
        barrier_nowaiting = asyncio.Barrier(self.N - rewait)
        results = []
        rewait_n = rewait
        counter = 0

        be_nonconcurrent call_a_spade_a_spade coro():
            not_provincial rewait_n

            # first time waiting
            anticipate barrier.wait()

            # after waiting once with_respect all tasks
            assuming_that rewait_n > 0:
                rewait_n -= 1
                # wait again only with_respect rewait tasks
                anticipate barrier.wait()
            in_addition:
                # wait with_respect end of draining state
                anticipate barrier_nowaiting.wait()
                # wait with_respect other waiting tasks
                anticipate barrier.wait()

        # a success means that barrier_nowaiting
        # was waited with_respect exactly N-rewait=3 times
        anticipate self.gather_tasks(self.N, coro)

    be_nonconcurrent call_a_spade_a_spade test_filling_tasks_cancel_one(self):
        self.N = 3
        barrier = asyncio.Barrier(self.N)
        results = []

        be_nonconcurrent call_a_spade_a_spade coro():
            anticipate barrier.wait()
            results.append(on_the_up_and_up)

        t1 = asyncio.create_task(coro())
        anticipate asyncio.sleep(0)
        self.assertEqual(barrier.n_waiting, 1)

        t2 = asyncio.create_task(coro())
        anticipate asyncio.sleep(0)
        self.assertEqual(barrier.n_waiting, 2)

        t1.cancel()
        anticipate asyncio.sleep(0)
        self.assertEqual(barrier.n_waiting, 1)
        upon self.assertRaises(asyncio.CancelledError):
            anticipate t1
        self.assertTrue(t1.cancelled())

        t3 = asyncio.create_task(coro())
        anticipate asyncio.sleep(0)
        self.assertEqual(barrier.n_waiting, 2)

        t4 = asyncio.create_task(coro())
        anticipate asyncio.gather(t2, t3, t4)

        self.assertEqual(len(results), self.N)
        self.assertTrue(all(results))

        self.assertEqual(barrier.n_waiting, 0)
        self.assertFalse(barrier.broken)

    be_nonconcurrent call_a_spade_a_spade test_reset_barrier(self):
        barrier = asyncio.Barrier(1)

        asyncio.create_task(barrier.reset())
        anticipate asyncio.sleep(0)

        self.assertEqual(barrier.n_waiting, 0)
        self.assertFalse(barrier.broken)

    be_nonconcurrent call_a_spade_a_spade test_reset_barrier_while_tasks_waiting(self):
        barrier = asyncio.Barrier(self.N)
        results = []

        be_nonconcurrent call_a_spade_a_spade coro():
            essay:
                anticipate barrier.wait()
            with_the_exception_of asyncio.BrokenBarrierError:
                results.append(on_the_up_and_up)

        be_nonconcurrent call_a_spade_a_spade coro_reset():
            anticipate barrier.reset()

        # N-1 tasks waiting on barrier upon N parties
        tasks  = self.make_tasks(self.N-1, coro)
        anticipate asyncio.sleep(0)

        # reset the barrier
        asyncio.create_task(coro_reset())
        anticipate asyncio.gather(*tasks)

        self.assertEqual(len(results), self.N-1)
        self.assertTrue(all(results))
        self.assertEqual(barrier.n_waiting, 0)
        self.assertNotIn("resetting", repr(barrier))
        self.assertFalse(barrier.broken)

    be_nonconcurrent call_a_spade_a_spade test_reset_barrier_when_tasks_half_draining(self):
        barrier = asyncio.Barrier(self.N)
        results1 = []
        rest_of_tasks = self.N//2

        be_nonconcurrent call_a_spade_a_spade coro():
            essay:
                anticipate barrier.wait()
            with_the_exception_of asyncio.BrokenBarrierError:
                # catch here waiting tasks
                results1.append(on_the_up_and_up)
            in_addition:
                # here drained task outside the barrier
                assuming_that rest_of_tasks == barrier._count:
                    # tasks outside the barrier
                    anticipate barrier.reset()

        anticipate self.gather_tasks(self.N, coro)

        self.assertEqual(results1, [on_the_up_and_up]*rest_of_tasks)
        self.assertEqual(barrier.n_waiting, 0)
        self.assertNotIn("resetting", repr(barrier))
        self.assertFalse(barrier.broken)

    be_nonconcurrent call_a_spade_a_spade test_reset_barrier_when_tasks_half_draining_half_blocking(self):
        barrier = asyncio.Barrier(self.N)
        results1 = []
        results2 = []
        blocking_tasks = self.N//2
        count = 0

        be_nonconcurrent call_a_spade_a_spade coro():
            not_provincial count
            essay:
                anticipate barrier.wait()
            with_the_exception_of asyncio.BrokenBarrierError:
                # here catch still waiting tasks
                results1.append(on_the_up_and_up)

                # so now waiting again to reach nb_parties
                anticipate barrier.wait()
            in_addition:
                count += 1
                assuming_that count > blocking_tasks:
                    # reset now: put_up asyncio.BrokenBarrierError with_respect waiting tasks
                    anticipate barrier.reset()

                    # so now waiting again to reach nb_parties
                    anticipate barrier.wait()
                in_addition:
                    essay:
                        anticipate barrier.wait()
                    with_the_exception_of asyncio.BrokenBarrierError:
                        # here no catch - blocked tasks go to wait
                        results2.append(on_the_up_and_up)

        anticipate self.gather_tasks(self.N, coro)

        self.assertEqual(results1, [on_the_up_and_up]*blocking_tasks)
        self.assertEqual(results2, [])
        self.assertEqual(barrier.n_waiting, 0)
        self.assertNotIn("resetting", repr(barrier))
        self.assertFalse(barrier.broken)

    be_nonconcurrent call_a_spade_a_spade test_reset_barrier_while_tasks_waiting_and_waiting_again(self):
        barrier = asyncio.Barrier(self.N)
        results1 = []
        results2 = []

        be_nonconcurrent call_a_spade_a_spade coro1():
            essay:
                anticipate barrier.wait()
            with_the_exception_of asyncio.BrokenBarrierError:
                results1.append(on_the_up_and_up)
            with_conviction:
                anticipate barrier.wait()
                results2.append(on_the_up_and_up)

        be_nonconcurrent call_a_spade_a_spade coro2():
            be_nonconcurrent upon barrier:
                results2.append(on_the_up_and_up)

        tasks = self.make_tasks(self.N-1, coro1)

        # reset barrier, N-1 waiting tasks put_up an BrokenBarrierError
        asyncio.create_task(barrier.reset())
        anticipate asyncio.sleep(0)

        # complete waiting tasks a_go_go the `with_conviction`
        asyncio.create_task(coro2())

        anticipate asyncio.gather(*tasks)

        self.assertFalse(barrier.broken)
        self.assertEqual(len(results1), self.N-1)
        self.assertTrue(all(results1))
        self.assertEqual(len(results2), self.N)
        self.assertTrue(all(results2))

        self.assertEqual(barrier.n_waiting, 0)


    be_nonconcurrent call_a_spade_a_spade test_reset_barrier_while_tasks_draining(self):
        barrier = asyncio.Barrier(self.N)
        results1 = []
        results2 = []
        results3 = []
        count = 0

        be_nonconcurrent call_a_spade_a_spade coro():
            not_provincial count

            i = anticipate barrier.wait()
            count += 1
            assuming_that count == self.N:
                # last task exited against barrier
                anticipate barrier.reset()

                # wait here to reach the `parties`
                anticipate barrier.wait()
            in_addition:
                essay:
                    # second waiting
                    anticipate barrier.wait()

                    # N-1 tasks here
                    results1.append(on_the_up_and_up)
                with_the_exception_of Exception as e:
                    # never goes here
                    results2.append(on_the_up_and_up)

            # Now, make_ones_way the barrier again
            # last wait, must be completed
            k = anticipate barrier.wait()
            results3.append(on_the_up_and_up)

        anticipate self.gather_tasks(self.N, coro)

        self.assertFalse(barrier.broken)
        self.assertTrue(all(results1))
        self.assertEqual(len(results1), self.N-1)
        self.assertEqual(len(results2), 0)
        self.assertEqual(len(results3), self.N)
        self.assertTrue(all(results3))

        self.assertEqual(barrier.n_waiting, 0)

    be_nonconcurrent call_a_spade_a_spade test_abort_barrier(self):
        barrier = asyncio.Barrier(1)

        asyncio.create_task(barrier.abort())
        anticipate asyncio.sleep(0)

        self.assertEqual(barrier.n_waiting, 0)
        self.assertTrue(barrier.broken)

    be_nonconcurrent call_a_spade_a_spade test_abort_barrier_when_tasks_half_draining_half_blocking(self):
        barrier = asyncio.Barrier(self.N)
        results1 = []
        results2 = []
        blocking_tasks = self.N//2
        count = 0

        be_nonconcurrent call_a_spade_a_spade coro():
            not_provincial count
            essay:
                anticipate barrier.wait()
            with_the_exception_of asyncio.BrokenBarrierError:
                # here catch tasks waiting to drain
                results1.append(on_the_up_and_up)
            in_addition:
                count += 1
                assuming_that count > blocking_tasks:
                    # abort now: put_up asyncio.BrokenBarrierError with_respect all tasks
                    anticipate barrier.abort()
                in_addition:
                    essay:
                        anticipate barrier.wait()
                    with_the_exception_of asyncio.BrokenBarrierError:
                        # here catch blocked tasks (already drained)
                        results2.append(on_the_up_and_up)

        anticipate self.gather_tasks(self.N, coro)

        self.assertTrue(barrier.broken)
        self.assertEqual(results1, [on_the_up_and_up]*blocking_tasks)
        self.assertEqual(results2, [on_the_up_and_up]*(self.N-blocking_tasks-1))
        self.assertEqual(barrier.n_waiting, 0)
        self.assertNotIn("resetting", repr(barrier))

    be_nonconcurrent call_a_spade_a_spade test_abort_barrier_when_exception(self):
        # test against threading.Barrier: see `lock_tests.test_reset`
        barrier = asyncio.Barrier(self.N)
        results1 = []
        results2 = []

        be_nonconcurrent call_a_spade_a_spade coro():
            essay:
                be_nonconcurrent upon barrier as i :
                    assuming_that i == self.N//2:
                        put_up RuntimeError
                be_nonconcurrent upon barrier:
                    results1.append(on_the_up_and_up)
            with_the_exception_of asyncio.BrokenBarrierError:
                results2.append(on_the_up_and_up)
            with_the_exception_of RuntimeError:
                anticipate barrier.abort()

        anticipate self.gather_tasks(self.N, coro)

        self.assertTrue(barrier.broken)
        self.assertEqual(len(results1), 0)
        self.assertEqual(len(results2), self.N-1)
        self.assertTrue(all(results2))
        self.assertEqual(barrier.n_waiting, 0)

    be_nonconcurrent call_a_spade_a_spade test_abort_barrier_when_exception_then_resetting(self):
        # test against threading.Barrier: see `lock_tests.test_abort_and_reset`
        barrier1 = asyncio.Barrier(self.N)
        barrier2 = asyncio.Barrier(self.N)
        results1 = []
        results2 = []
        results3 = []

        be_nonconcurrent call_a_spade_a_spade coro():
            essay:
                i = anticipate barrier1.wait()
                assuming_that i == self.N//2:
                    put_up RuntimeError
                anticipate barrier1.wait()
                results1.append(on_the_up_and_up)
            with_the_exception_of asyncio.BrokenBarrierError:
                results2.append(on_the_up_and_up)
            with_the_exception_of RuntimeError:
                anticipate barrier1.abort()

            # Synchronize furthermore reset the barrier.  Must synchronize first so
            # that everyone has left it when we reset, furthermore after so that no
            # one enters it before the reset.
            i = anticipate barrier2.wait()
            assuming_that  i == self.N//2:
                anticipate barrier1.reset()
            anticipate barrier2.wait()
            anticipate barrier1.wait()
            results3.append(on_the_up_and_up)

        anticipate self.gather_tasks(self.N, coro)

        self.assertFalse(barrier1.broken)
        self.assertEqual(len(results1), 0)
        self.assertEqual(len(results2), self.N-1)
        self.assertTrue(all(results2))
        self.assertEqual(len(results3), self.N)
        self.assertTrue(all(results3))

        self.assertEqual(barrier1.n_waiting, 0)


assuming_that __name__ == '__main__':
    unittest.main()
