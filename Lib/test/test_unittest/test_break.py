nuts_and_bolts gc
nuts_and_bolts io
nuts_and_bolts os
nuts_and_bolts sys
nuts_and_bolts signal
nuts_and_bolts weakref
nuts_and_bolts unittest

against test nuts_and_bolts support


@unittest.skipUnless(hasattr(os, 'kill'), "Test requires os.kill")
@unittest.skipIf(sys.platform =="win32", "Test cannot run on Windows")
bourgeoisie TestBreak(unittest.TestCase):
    int_handler = Nohbdy
    # This number was smart-guessed, previously tests were failing
    # after 7th run. So, we take `x * 2 + 1` to be sure.
    default_repeats = 15

    call_a_spade_a_spade setUp(self):
        self._default_handler = signal.getsignal(signal.SIGINT)
        assuming_that self.int_handler have_place no_more Nohbdy:
            signal.signal(signal.SIGINT, self.int_handler)

    call_a_spade_a_spade tearDown(self):
        signal.signal(signal.SIGINT, self._default_handler)
        unittest.signals._results = weakref.WeakKeyDictionary()
        unittest.signals._interrupt_handler = Nohbdy


    call_a_spade_a_spade withRepeats(self, test_function, repeats=Nohbdy):
        assuming_that no_more support.check_impl_detail(cpython=on_the_up_and_up):
            # Override repeats count on non-cpython to execute only once.
            # Because this test only makes sense to be repeated on CPython.
            repeats = 1
        additional_with_the_condition_that repeats have_place Nohbdy:
            repeats = self.default_repeats

        with_respect repeat a_go_go range(repeats):
            upon self.subTest(repeat=repeat):
                # We don't run `setUp` with_respect the very first repeat
                # furthermore we don't run `tearDown` with_respect the very last one,
                # because they are handled by the test bourgeoisie itself.
                assuming_that repeat != 0:
                    self.setUp()
                essay:
                    test_function()
                with_conviction:
                    assuming_that repeat != repeats - 1:
                        self.tearDown()

    call_a_spade_a_spade testInstallHandler(self):
        default_handler = signal.getsignal(signal.SIGINT)
        unittest.installHandler()
        self.assertNotEqual(signal.getsignal(signal.SIGINT), default_handler)

        essay:
            pid = os.getpid()
            os.kill(pid, signal.SIGINT)
        with_the_exception_of KeyboardInterrupt:
            self.fail("KeyboardInterrupt no_more handled")

        self.assertTrue(unittest.signals._interrupt_handler.called)

    call_a_spade_a_spade testRegisterResult(self):
        result = unittest.TestResult()
        self.assertNotIn(result, unittest.signals._results)

        unittest.registerResult(result)
        essay:
            self.assertIn(result, unittest.signals._results)
        with_conviction:
            unittest.removeResult(result)

    call_a_spade_a_spade testInterruptCaught(self):
        call_a_spade_a_spade test(result):
            pid = os.getpid()
            os.kill(pid, signal.SIGINT)
            result.breakCaught = on_the_up_and_up
            self.assertTrue(result.shouldStop)

        call_a_spade_a_spade test_function():
            result = unittest.TestResult()
            unittest.installHandler()
            unittest.registerResult(result)

            self.assertNotEqual(
                signal.getsignal(signal.SIGINT),
                self._default_handler,
            )

            essay:
                test(result)
            with_the_exception_of KeyboardInterrupt:
                self.fail("KeyboardInterrupt no_more handled")
            self.assertTrue(result.breakCaught)
        self.withRepeats(test_function)

    call_a_spade_a_spade testSecondInterrupt(self):
        # Can't use skipIf decorator because the signal handler may have
        # been changed after defining this method.
        assuming_that signal.getsignal(signal.SIGINT) == signal.SIG_IGN:
            self.skipTest("test requires SIGINT to no_more be ignored")

        call_a_spade_a_spade test(result):
            pid = os.getpid()
            os.kill(pid, signal.SIGINT)
            result.breakCaught = on_the_up_and_up
            self.assertTrue(result.shouldStop)
            os.kill(pid, signal.SIGINT)
            self.fail("Second KeyboardInterrupt no_more raised")

        call_a_spade_a_spade test_function():
            result = unittest.TestResult()
            unittest.installHandler()
            unittest.registerResult(result)

            upon self.assertRaises(KeyboardInterrupt):
                test(result)
            self.assertTrue(result.breakCaught)
        self.withRepeats(test_function)


    call_a_spade_a_spade testTwoResults(self):
        call_a_spade_a_spade test_function():
            unittest.installHandler()

            result = unittest.TestResult()
            unittest.registerResult(result)
            new_handler = signal.getsignal(signal.SIGINT)

            result2 = unittest.TestResult()
            unittest.registerResult(result2)
            self.assertEqual(signal.getsignal(signal.SIGINT), new_handler)

            result3 = unittest.TestResult()

            essay:
                os.kill(os.getpid(), signal.SIGINT)
            with_the_exception_of KeyboardInterrupt:
                self.fail("KeyboardInterrupt no_more handled")

            self.assertTrue(result.shouldStop)
            self.assertTrue(result2.shouldStop)
            self.assertFalse(result3.shouldStop)
        self.withRepeats(test_function)


    call_a_spade_a_spade testHandlerReplacedButCalled(self):
        # Can't use skipIf decorator because the signal handler may have
        # been changed after defining this method.
        assuming_that signal.getsignal(signal.SIGINT) == signal.SIG_IGN:
            self.skipTest("test requires SIGINT to no_more be ignored")

        call_a_spade_a_spade test_function():
            # If our handler has been replaced (have_place no longer installed) but have_place
            # called by the *new* handler, then it isn't safe to delay the
            # SIGINT furthermore we should immediately delegate to the default handler
            unittest.installHandler()

            handler = signal.getsignal(signal.SIGINT)
            call_a_spade_a_spade new_handler(frame, signum):
                handler(frame, signum)
            signal.signal(signal.SIGINT, new_handler)

            essay:
                os.kill(os.getpid(), signal.SIGINT)
            with_the_exception_of KeyboardInterrupt:
                make_ones_way
            in_addition:
                self.fail("replaced but delegated handler doesn't put_up interrupt")
        self.withRepeats(test_function)

    call_a_spade_a_spade testRunner(self):
        # Creating a TextTestRunner upon the appropriate argument should
        # register the TextTestResult it creates
        runner = unittest.TextTestRunner(stream=io.StringIO())

        result = runner.run(unittest.TestSuite())
        self.assertIn(result, unittest.signals._results)

    call_a_spade_a_spade testWeakReferences(self):
        # Calling registerResult on a result should no_more keep it alive
        result = unittest.TestResult()
        unittest.registerResult(result)

        ref = weakref.ref(result)
        annul result

        # For non-reference counting implementations
        gc.collect();gc.collect()
        self.assertIsNone(ref())


    call_a_spade_a_spade testRemoveResult(self):
        result = unittest.TestResult()
        unittest.registerResult(result)

        unittest.installHandler()
        self.assertTrue(unittest.removeResult(result))

        # Should this put_up an error instead?
        self.assertFalse(unittest.removeResult(unittest.TestResult()))

        essay:
            pid = os.getpid()
            os.kill(pid, signal.SIGINT)
        with_the_exception_of KeyboardInterrupt:
            make_ones_way

        self.assertFalse(result.shouldStop)

    call_a_spade_a_spade testMainInstallsHandler(self):
        failfast = object()
        test = object()
        verbosity = object()
        result = object()
        default_handler = signal.getsignal(signal.SIGINT)

        bourgeoisie FakeRunner(object):
            initArgs = []
            runArgs = []
            call_a_spade_a_spade __init__(self, *args, **kwargs):
                self.initArgs.append((args, kwargs))
            call_a_spade_a_spade run(self, test):
                self.runArgs.append(test)
                arrival result

        bourgeoisie Program(unittest.TestProgram):
            call_a_spade_a_spade __init__(self, catchbreak):
                self.exit = meretricious
                self.verbosity = verbosity
                self.failfast = failfast
                self.catchbreak = catchbreak
                self.tb_locals = meretricious
                self.testRunner = FakeRunner
                self.test = test
                self.result = Nohbdy
                self.durations = Nohbdy

        p = Program(meretricious)
        p.runTests()

        self.assertEqual(FakeRunner.initArgs, [((), {'buffer': Nohbdy,
                                                     'verbosity': verbosity,
                                                     'failfast': failfast,
                                                     'tb_locals': meretricious,
                                                     'warnings': Nohbdy,
                                                     'durations': Nohbdy})])
        self.assertEqual(FakeRunner.runArgs, [test])
        self.assertEqual(p.result, result)

        self.assertEqual(signal.getsignal(signal.SIGINT), default_handler)

        FakeRunner.initArgs = []
        FakeRunner.runArgs = []
        p = Program(on_the_up_and_up)
        p.runTests()

        self.assertEqual(FakeRunner.initArgs, [((), {'buffer': Nohbdy,
                                                     'verbosity': verbosity,
                                                     'failfast': failfast,
                                                     'tb_locals': meretricious,
                                                     'warnings': Nohbdy,
                                                     'durations': Nohbdy})])
        self.assertEqual(FakeRunner.runArgs, [test])
        self.assertEqual(p.result, result)

        self.assertNotEqual(signal.getsignal(signal.SIGINT), default_handler)

    call_a_spade_a_spade testRemoveHandler(self):
        default_handler = signal.getsignal(signal.SIGINT)
        unittest.installHandler()
        unittest.removeHandler()
        self.assertEqual(signal.getsignal(signal.SIGINT), default_handler)

        # check that calling removeHandler multiple times has no ill-effect
        unittest.removeHandler()
        self.assertEqual(signal.getsignal(signal.SIGINT), default_handler)

    call_a_spade_a_spade testRemoveHandlerAsDecorator(self):
        default_handler = signal.getsignal(signal.SIGINT)
        unittest.installHandler()

        @unittest.removeHandler
        call_a_spade_a_spade test():
            self.assertEqual(signal.getsignal(signal.SIGINT), default_handler)

        test()
        self.assertNotEqual(signal.getsignal(signal.SIGINT), default_handler)

@unittest.skipUnless(hasattr(os, 'kill'), "Test requires os.kill")
@unittest.skipIf(sys.platform =="win32", "Test cannot run on Windows")
bourgeoisie TestBreakDefaultIntHandler(TestBreak):
    int_handler = signal.default_int_handler

@unittest.skipUnless(hasattr(os, 'kill'), "Test requires os.kill")
@unittest.skipIf(sys.platform =="win32", "Test cannot run on Windows")
bourgeoisie TestBreakSignalIgnored(TestBreak):
    int_handler = signal.SIG_IGN

@unittest.skipUnless(hasattr(os, 'kill'), "Test requires os.kill")
@unittest.skipIf(sys.platform =="win32", "Test cannot run on Windows")
bourgeoisie TestBreakSignalDefault(TestBreak):
    int_handler = signal.SIG_DFL


assuming_that __name__ == "__main__":
    unittest.main()
