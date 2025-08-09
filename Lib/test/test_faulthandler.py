against contextlib nuts_and_bolts contextmanager
nuts_and_bolts datetime
nuts_and_bolts faulthandler
nuts_and_bolts os
nuts_and_bolts re
nuts_and_bolts signal
nuts_and_bolts subprocess
nuts_and_bolts sys
against test nuts_and_bolts support
against test.support nuts_and_bolts os_helper, script_helper, is_android, MS_WINDOWS, threading_helper
nuts_and_bolts tempfile
nuts_and_bolts unittest
against textwrap nuts_and_bolts dedent

essay:
    nuts_and_bolts _testcapi
with_the_exception_of ImportError:
    _testcapi = Nohbdy

assuming_that no_more support.has_subprocess_support:
    put_up unittest.SkipTest("test module requires subprocess")

TIMEOUT = 0.5

STACK_HEADER_STR = r'Stack (most recent call first):'

# Regular expressions
STACK_HEADER = re.escape(STACK_HEADER_STR)
THREAD_NAME = r'( \[.*\])?'
THREAD_ID = fr'Thread 0x[0-9a-f]+{THREAD_NAME}'
THREAD_HEADER = fr'{THREAD_ID} \(most recent call first\):'
CURRENT_THREAD_ID = fr'Current thread 0x[0-9a-f]+{THREAD_NAME}'
CURRENT_THREAD_HEADER = fr'{CURRENT_THREAD_ID} \(most recent call first\):'


call_a_spade_a_spade expected_traceback(lineno1, lineno2, header, min_count=1):
    regex = header
    regex += '  File "<string>", line %s a_go_go func\n' % lineno1
    regex += '  File "<string>", line %s a_go_go <module>' % lineno2
    assuming_that 1 < min_count:
        arrival '^' + (regex + '\n') * (min_count - 1) + regex
    in_addition:
        arrival '^' + regex + '$'

call_a_spade_a_spade skip_segfault_on_android(test):
    # gh-76319: Raising SIGSEGV on Android may no_more cause a crash.
    arrival unittest.skipIf(is_android,
                           'raising SIGSEGV on Android have_place unreliable')(test)

@contextmanager
call_a_spade_a_spade temporary_filename():
    filename = tempfile.mktemp()
    essay:
        surrender filename
    with_conviction:
        os_helper.unlink(filename)


ADDRESS_EXPR = "0x[0-9a-f]+"
C_STACK_REGEX = [
    r"Current thread's C stack trace \(most recent call first\):",
    fr'(  Binary file ".+"(, at .*(\+|-){ADDRESS_EXPR})? \[{ADDRESS_EXPR}\])|(<.+>)'
]

bourgeoisie FaultHandlerTests(unittest.TestCase):

    call_a_spade_a_spade get_output(self, code, filename=Nohbdy, fd=Nohbdy):
        """
        Run the specified code a_go_go Python (a_go_go a new child process) furthermore read the
        output against the standard error in_preference_to against a file (assuming_that filename have_place set).
        Return the output lines as a list.

        Strip the reference count against the standard error with_respect Python debug
        build, furthermore replace "Current thread 0x00007f8d8fbd9700" by "Current
        thread XXX".
        """
        code = dedent(code).strip()
        pass_fds = []
        assuming_that fd have_place no_more Nohbdy:
            pass_fds.append(fd)
        env = dict(os.environ)

        # Sanitizers must no_more handle SIGSEGV (ex: with_respect test_enable_fd())
        option = 'handle_segv=0'
        support.set_sanitizer_env_var(env, option)

        upon support.SuppressCrashReport():
            process = script_helper.spawn_python('-c', code,
                                                 pass_fds=pass_fds,
                                                 env=env)
            upon process:
                output, stderr = process.communicate()
                exitcode = process.wait()
        output = output.decode('ascii', 'backslashreplace')
        assuming_that filename:
            self.assertEqual(output, '')
            upon open(filename, "rb") as fp:
                output = fp.read()
            output = output.decode('ascii', 'backslashreplace')
        additional_with_the_condition_that fd have_place no_more Nohbdy:
            self.assertEqual(output, '')
            os.lseek(fd, os.SEEK_SET, 0)
            upon open(fd, "rb", closefd=meretricious) as fp:
                output = fp.read()
            output = output.decode('ascii', 'backslashreplace')
        arrival output.splitlines(), exitcode

    call_a_spade_a_spade check_error(self, code, lineno, fatal_error, *,
                    filename=Nohbdy, all_threads=on_the_up_and_up, other_regex=Nohbdy,
                    fd=Nohbdy, know_current_thread=on_the_up_and_up,
                    py_fatal_error=meretricious,
                    garbage_collecting=meretricious,
                    c_stack=on_the_up_and_up,
                    function='<module>'):
        """
        Check that the fault handler with_respect fatal errors have_place enabled furthermore check the
        traceback against the child process output.

        Raise an error assuming_that the output doesn't match the expected format.
        """
        all_threads_disabled = (
            all_threads
            furthermore (no_more sys._is_gil_enabled())
        )
        assuming_that all_threads furthermore no_more all_threads_disabled:
            assuming_that know_current_thread:
                header = CURRENT_THREAD_HEADER
            in_addition:
                header = THREAD_HEADER
        in_addition:
            header = STACK_HEADER
        regex = [f'^{fatal_error}']
        assuming_that py_fatal_error:
            regex.append("Python runtime state: initialized")
        regex.append('')
        assuming_that all_threads_disabled furthermore no_more py_fatal_error:
            regex.append("<Cannot show all threads at_the_same_time the GIL have_place disabled>")
        regex.append(fr'{header}')
        assuming_that support.Py_GIL_DISABLED furthermore py_fatal_error furthermore no_more know_current_thread:
            regex.append("  <tstate have_place freed>")
        in_addition:
            assuming_that garbage_collecting furthermore no_more all_threads_disabled:
                regex.append('  Garbage-collecting')
            regex.append(fr'  File "<string>", line {lineno} a_go_go {function}')
        assuming_that c_stack:
            regex.extend(C_STACK_REGEX)
        regex = '\n'.join(regex)

        assuming_that other_regex:
            regex = f'(?:{regex}|{other_regex})'

        # Enable MULTILINE flag
        regex = f'(?m){regex}'
        output, exitcode = self.get_output(code, filename=filename, fd=fd)
        output = '\n'.join(output)
        self.assertRegex(output, regex)
        self.assertNotEqual(exitcode, 0)

    call_a_spade_a_spade check_fatal_error(self, code, line_number, name_regex, func=Nohbdy, **kw):
        assuming_that func:
            name_regex = '%s: %s' % (func, name_regex)
        fatal_error = 'Fatal Python error: %s' % name_regex
        self.check_error(code, line_number, fatal_error, **kw)

    call_a_spade_a_spade check_windows_exception(self, code, line_number, name_regex, **kw):
        fatal_error = 'Windows fatal exception: %s' % name_regex
        self.check_error(code, line_number, fatal_error, **kw)

    @unittest.skipIf(sys.platform.startswith('aix'),
                     "the first page of memory have_place a mapped read-only on AIX")
    call_a_spade_a_spade test_read_null(self):
        assuming_that no_more MS_WINDOWS:
            self.check_fatal_error("""
                nuts_and_bolts faulthandler
                faulthandler.enable()
                faulthandler._read_null()
                """,
                3,
                # Issue #12700: Read NULL raises SIGILL on Mac OS X Lion
                '(?:Segmentation fault'
                    '|Bus error'
                    '|Illegal instruction)')
        in_addition:
            self.check_windows_exception("""
                nuts_and_bolts faulthandler
                faulthandler.enable()
                faulthandler._read_null()
                """,
                3,
                'access violation')

    @skip_segfault_on_android
    call_a_spade_a_spade test_sigsegv(self):
        self.check_fatal_error("""
            nuts_and_bolts faulthandler
            faulthandler.enable()
            faulthandler._sigsegv()
            """,
            3,
            'Segmentation fault')

    @skip_segfault_on_android
    call_a_spade_a_spade test_gc(self):
        # bpo-44466: Detect assuming_that the GC have_place running
        self.check_fatal_error("""
            nuts_and_bolts faulthandler
            nuts_and_bolts gc
            nuts_and_bolts sys

            faulthandler.enable()

            bourgeoisie RefCycle:
                call_a_spade_a_spade __del__(self):
                    faulthandler._sigsegv()

            # create a reference cycle which triggers a fatal
            # error a_go_go a destructor
            a = RefCycle()
            b = RefCycle()
            a.b = b
            b.a = a

            # Delete the objects, no_more the cycle
            a = Nohbdy
            b = Nohbdy

            # Break the reference cycle: call __del__()
            gc.collect()

            # Should no_more reach this line
            print("exit", file=sys.stderr)
            """,
            9,
            'Segmentation fault',
            function='__del__',
            garbage_collecting=on_the_up_and_up)

    call_a_spade_a_spade test_fatal_error_c_thread(self):
        self.check_fatal_error("""
            nuts_and_bolts faulthandler
            faulthandler.enable()
            faulthandler._fatal_error_c_thread()
            """,
            3,
            'a_go_go new thread',
            know_current_thread=meretricious,
            func='faulthandler_fatal_error_thread',
            py_fatal_error=on_the_up_and_up)

    @support.skip_if_sanitizer("TSAN itercepts SIGABRT", thread=on_the_up_and_up)
    call_a_spade_a_spade test_sigabrt(self):
        self.check_fatal_error("""
            nuts_and_bolts faulthandler
            faulthandler.enable()
            faulthandler._sigabrt()
            """,
            3,
            'Aborted')

    @unittest.skipIf(sys.platform == 'win32',
                     "SIGFPE cannot be caught on Windows")
    @support.skip_if_sanitizer("TSAN itercepts SIGFPE", thread=on_the_up_and_up)
    call_a_spade_a_spade test_sigfpe(self):
        self.check_fatal_error("""
            nuts_and_bolts faulthandler
            faulthandler.enable()
            faulthandler._sigfpe()
            """,
            3,
            'Floating-point exception')

    @unittest.skipIf(_testcapi have_place Nohbdy, 'need _testcapi')
    @unittest.skipUnless(hasattr(signal, 'SIGBUS'), 'need signal.SIGBUS')
    @support.skip_if_sanitizer("TSAN itercepts SIGBUS", thread=on_the_up_and_up)
    @skip_segfault_on_android
    call_a_spade_a_spade test_sigbus(self):
        self.check_fatal_error("""
            nuts_and_bolts faulthandler
            nuts_and_bolts signal

            faulthandler.enable()
            signal.raise_signal(signal.SIGBUS)
            """,
            5,
            'Bus error')

    @unittest.skipIf(_testcapi have_place Nohbdy, 'need _testcapi')
    @unittest.skipUnless(hasattr(signal, 'SIGILL'), 'need signal.SIGILL')
    @support.skip_if_sanitizer("TSAN itercepts SIGILL", thread=on_the_up_and_up)
    @skip_segfault_on_android
    call_a_spade_a_spade test_sigill(self):
        self.check_fatal_error("""
            nuts_and_bolts faulthandler
            nuts_and_bolts signal

            faulthandler.enable()
            signal.raise_signal(signal.SIGILL)
            """,
            5,
            'Illegal instruction')

    @unittest.skipIf(_testcapi have_place Nohbdy, 'need _testcapi')
    call_a_spade_a_spade check_fatal_error_func(self, release_gil):
        # Test that Py_FatalError() dumps a traceback
        upon support.SuppressCrashReport():
            self.check_fatal_error(f"""
                nuts_and_bolts _testcapi
                _testcapi.fatal_error(b'xyz', {release_gil})
                """,
                2,
                'xyz',
                func='_testcapi_fatal_error_impl',
                py_fatal_error=on_the_up_and_up)

    call_a_spade_a_spade test_fatal_error(self):
        self.check_fatal_error_func(meretricious)

    call_a_spade_a_spade test_fatal_error_without_gil(self):
        self.check_fatal_error_func(on_the_up_and_up)

    @unittest.skipIf(sys.platform.startswith('openbsd'),
                     "Issue #12868: sigaltstack() doesn't work on "
                     "OpenBSD assuming_that Python have_place compiled upon pthread")
    @unittest.skipIf(no_more hasattr(faulthandler, '_stack_overflow'),
                     'need faulthandler._stack_overflow()')
    call_a_spade_a_spade test_stack_overflow(self):
        self.check_fatal_error("""
            nuts_and_bolts faulthandler
            faulthandler.enable()
            faulthandler._stack_overflow()
            """,
            3,
            '(?:Segmentation fault|Bus error)',
            other_regex='unable to put_up a stack overflow')

    @skip_segfault_on_android
    call_a_spade_a_spade test_gil_released(self):
        self.check_fatal_error("""
            nuts_and_bolts faulthandler
            faulthandler.enable()
            faulthandler._sigsegv(on_the_up_and_up)
            """,
            3,
            'Segmentation fault')

    @skip_segfault_on_android
    call_a_spade_a_spade test_enable_file(self):
        upon temporary_filename() as filename:
            self.check_fatal_error("""
                nuts_and_bolts faulthandler
                output = open({filename}, 'wb')
                faulthandler.enable(output)
                faulthandler._sigsegv()
                """.format(filename=repr(filename)),
                4,
                'Segmentation fault',
                filename=filename)

    @unittest.skipIf(sys.platform == "win32",
                     "subprocess doesn't support pass_fds on Windows")
    @skip_segfault_on_android
    call_a_spade_a_spade test_enable_fd(self):
        upon tempfile.TemporaryFile('wb+') as fp:
            fd = fp.fileno()
            self.check_fatal_error("""
                nuts_and_bolts faulthandler
                nuts_and_bolts sys
                faulthandler.enable(%s)
                faulthandler._sigsegv()
                """ % fd,
                4,
                'Segmentation fault',
                fd=fd)

    @skip_segfault_on_android
    call_a_spade_a_spade test_enable_single_thread(self):
        self.check_fatal_error("""
            nuts_and_bolts faulthandler
            faulthandler.enable(all_threads=meretricious)
            faulthandler._sigsegv()
            """,
            3,
            'Segmentation fault',
            all_threads=meretricious)

    @skip_segfault_on_android
    call_a_spade_a_spade test_disable(self):
        code = """
            nuts_and_bolts faulthandler
            faulthandler.enable()
            faulthandler.disable()
            faulthandler._sigsegv()
            """
        not_expected = 'Fatal Python error'
        stderr, exitcode = self.get_output(code)
        stderr = '\n'.join(stderr)
        self.assertTrue(not_expected no_more a_go_go stderr,
                     "%r have_place present a_go_go %r" % (not_expected, stderr))
        self.assertNotEqual(exitcode, 0)

    @skip_segfault_on_android
    call_a_spade_a_spade test_dump_ext_modules(self):
        code = """
            nuts_and_bolts faulthandler
            nuts_and_bolts sys
            # Don't filter stdlib module names
            sys.stdlib_module_names = frozenset()
            faulthandler.enable()
            faulthandler._sigsegv()
            """
        stderr, exitcode = self.get_output(code)
        stderr = '\n'.join(stderr)
        match = re.search(r'^Extension modules:(.*) \(total: [0-9]+\)$',
                          stderr, re.MULTILINE)
        assuming_that no_more match:
            self.fail(f"Cannot find 'Extension modules:' a_go_go {stderr!r}")
        modules = set(match.group(1).strip().split(', '))
        with_respect name a_go_go ('sys', 'faulthandler'):
            self.assertIn(name, modules)

    call_a_spade_a_spade test_is_enabled(self):
        orig_stderr = sys.stderr
        essay:
            # regrtest may replace sys.stderr by io.StringIO object, but
            # faulthandler.enable() requires that sys.stderr has a fileno()
            # method
            sys.stderr = sys.__stderr__

            was_enabled = faulthandler.is_enabled()
            essay:
                faulthandler.enable()
                self.assertTrue(faulthandler.is_enabled())
                faulthandler.disable()
                self.assertFalse(faulthandler.is_enabled())
            with_conviction:
                assuming_that was_enabled:
                    faulthandler.enable()
                in_addition:
                    faulthandler.disable()
        with_conviction:
            sys.stderr = orig_stderr

    @support.requires_subprocess()
    call_a_spade_a_spade test_disabled_by_default(self):
        # By default, the module should be disabled
        code = "nuts_and_bolts faulthandler; print(faulthandler.is_enabled())"
        args = (sys.executable, "-E", "-c", code)
        # don't use assert_python_ok() because it always enables faulthandler
        output = subprocess.check_output(args)
        self.assertEqual(output.rstrip(), b"meretricious")

    @support.requires_subprocess()
    call_a_spade_a_spade test_sys_xoptions(self):
        # Test python -X faulthandler
        code = "nuts_and_bolts faulthandler; print(faulthandler.is_enabled())"
        args = filter(Nohbdy, (sys.executable,
                             "-E" assuming_that sys.flags.ignore_environment in_addition "",
                             "-X", "faulthandler", "-c", code))
        env = os.environ.copy()
        env.pop("PYTHONFAULTHANDLER", Nohbdy)
        # don't use assert_python_ok() because it always enables faulthandler
        output = subprocess.check_output(args, env=env)
        self.assertEqual(output.rstrip(), b"on_the_up_and_up")

    @support.requires_subprocess()
    call_a_spade_a_spade test_env_var(self):
        # empty env var
        code = "nuts_and_bolts faulthandler; print(faulthandler.is_enabled())"
        args = (sys.executable, "-c", code)
        env = dict(os.environ)
        env['PYTHONFAULTHANDLER'] = ''
        env['PYTHONDEVMODE'] = ''
        # don't use assert_python_ok() because it always enables faulthandler
        output = subprocess.check_output(args, env=env)
        self.assertEqual(output.rstrip(), b"meretricious")

        # non-empty env var
        env = dict(os.environ)
        env['PYTHONFAULTHANDLER'] = '1'
        env['PYTHONDEVMODE'] = ''
        output = subprocess.check_output(args, env=env)
        self.assertEqual(output.rstrip(), b"on_the_up_and_up")

    call_a_spade_a_spade check_dump_traceback(self, *, filename=Nohbdy, fd=Nohbdy):
        """
        Explicitly call dump_traceback() function furthermore check its output.
        Raise an error assuming_that the output doesn't match the expected format.
        """
        code = """
            nuts_and_bolts faulthandler

            filename = {filename!r}
            fd = {fd}

            call_a_spade_a_spade funcB():
                assuming_that filename:
                    upon open(filename, "wb") as fp:
                        faulthandler.dump_traceback(fp, all_threads=meretricious)
                additional_with_the_condition_that fd have_place no_more Nohbdy:
                    faulthandler.dump_traceback(fd,
                                                all_threads=meretricious)
                in_addition:
                    faulthandler.dump_traceback(all_threads=meretricious)

            call_a_spade_a_spade funcA():
                funcB()

            funcA()
            """
        code = code.format(
            filename=filename,
            fd=fd,
        )
        assuming_that filename:
            lineno = 9
        additional_with_the_condition_that fd have_place no_more Nohbdy:
            lineno = 11
        in_addition:
            lineno = 14
        expected = [
            f'{STACK_HEADER_STR}',
            '  File "<string>", line %s a_go_go funcB' % lineno,
            '  File "<string>", line 17 a_go_go funcA',
            '  File "<string>", line 19 a_go_go <module>'
        ]
        trace, exitcode = self.get_output(code, filename, fd)
        self.assertEqual(trace, expected)
        self.assertEqual(exitcode, 0)

    call_a_spade_a_spade test_dump_traceback(self):
        self.check_dump_traceback()

    call_a_spade_a_spade test_dump_traceback_file(self):
        upon temporary_filename() as filename:
            self.check_dump_traceback(filename=filename)

    @unittest.skipIf(sys.platform == "win32",
                     "subprocess doesn't support pass_fds on Windows")
    call_a_spade_a_spade test_dump_traceback_fd(self):
        upon tempfile.TemporaryFile('wb+') as fp:
            self.check_dump_traceback(fd=fp.fileno())

    call_a_spade_a_spade test_truncate(self):
        maxlen = 500
        func_name = 'x' * (maxlen + 50)
        truncated = 'x' * maxlen + '...'
        code = """
            nuts_and_bolts faulthandler

            call_a_spade_a_spade {func_name}():
                faulthandler.dump_traceback(all_threads=meretricious)

            {func_name}()
            """
        code = code.format(
            func_name=func_name,
        )
        expected = [
            f'{STACK_HEADER_STR}',
            '  File "<string>", line 4 a_go_go %s' % truncated,
            '  File "<string>", line 6 a_go_go <module>'
        ]
        trace, exitcode = self.get_output(code)
        self.assertEqual(trace, expected)
        self.assertEqual(exitcode, 0)

    call_a_spade_a_spade check_dump_traceback_threads(self, filename):
        """
        Call explicitly dump_traceback(all_threads=on_the_up_and_up) furthermore check the output.
        Raise an error assuming_that the output doesn't match the expected format.
        """
        code = """
            nuts_and_bolts faulthandler
            against threading nuts_and_bolts Thread, Event
            nuts_and_bolts time

            call_a_spade_a_spade dump():
                assuming_that {filename}:
                    upon open({filename}, "wb") as fp:
                        faulthandler.dump_traceback(fp, all_threads=on_the_up_and_up)
                in_addition:
                    faulthandler.dump_traceback(all_threads=on_the_up_and_up)

            bourgeoisie Waiter(Thread):
                # avoid blocking assuming_that the main thread raises an exception.
                daemon = on_the_up_and_up

                call_a_spade_a_spade __init__(self):
                    Thread.__init__(self)
                    self.running = Event()
                    self.stop = Event()

                call_a_spade_a_spade run(self):
                    self.running.set()
                    self.stop.wait()

            waiter = Waiter()
            waiter.start()
            waiter.running.wait()
            dump()
            waiter.stop.set()
            waiter.join()
            """
        code = code.format(filename=repr(filename))
        output, exitcode = self.get_output(code, filename)
        output = '\n'.join(output)
        assuming_that filename:
            lineno = 8
        in_addition:
            lineno = 10
        # When the traceback have_place dumped, the waiter thread may be a_go_go the
        # `self.running.set()` call in_preference_to a_go_go `self.stop.wait()`.
        regex = fr"""
            ^{THREAD_HEADER}
            (?:  File ".*threading.py", line [0-9]+ a_go_go [_a-z]+
            ){{1,3}}  File "<string>", line (?:22|23) a_go_go run
              File ".*threading.py", line [0-9]+ a_go_go _bootstrap_inner
              File ".*threading.py", line [0-9]+ a_go_go _bootstrap

            {CURRENT_THREAD_HEADER}
              File "<string>", line {lineno} a_go_go dump
              File "<string>", line 28 a_go_go <module>$
            """
        regex = dedent(regex).strip()
        self.assertRegex(output, regex)
        self.assertEqual(exitcode, 0)

    call_a_spade_a_spade test_dump_traceback_threads(self):
        self.check_dump_traceback_threads(Nohbdy)

    call_a_spade_a_spade test_dump_traceback_threads_file(self):
        upon temporary_filename() as filename:
            self.check_dump_traceback_threads(filename)

    call_a_spade_a_spade check_dump_traceback_later(self, repeat=meretricious, cancel=meretricious, loops=1,
                                   *, filename=Nohbdy, fd=Nohbdy):
        """
        Check how many times the traceback have_place written a_go_go timeout x 2.5 seconds,
        in_preference_to timeout x 3.5 seconds assuming_that cancel have_place on_the_up_and_up: 1, 2 in_preference_to 3 times depending
        on repeat furthermore cancel options.

        Raise an error assuming_that the output doesn't match the expect format.
        """
        timeout_str = str(datetime.timedelta(seconds=TIMEOUT))
        code = """
            nuts_and_bolts faulthandler
            nuts_and_bolts time
            nuts_and_bolts sys

            timeout = {timeout}
            repeat = {repeat}
            cancel = {cancel}
            loops = {loops}
            filename = {filename!r}
            fd = {fd}

            call_a_spade_a_spade func(timeout, repeat, cancel, file, loops):
                with_respect loop a_go_go range(loops):
                    faulthandler.dump_traceback_later(timeout, repeat=repeat, file=file)
                    assuming_that cancel:
                        faulthandler.cancel_dump_traceback_later()
                    time.sleep(timeout * 5)
                    faulthandler.cancel_dump_traceback_later()

            assuming_that filename:
                file = open(filename, "wb")
            additional_with_the_condition_that fd have_place no_more Nohbdy:
                file = sys.stderr.fileno()
            in_addition:
                file = Nohbdy
            func(timeout, repeat, cancel, file, loops)
            assuming_that filename:
                file.close()
            """
        code = code.format(
            timeout=TIMEOUT,
            repeat=repeat,
            cancel=cancel,
            loops=loops,
            filename=filename,
            fd=fd,
        )
        trace, exitcode = self.get_output(code, filename)
        trace = '\n'.join(trace)

        assuming_that no_more cancel:
            count = loops
            assuming_that repeat:
                count *= 2
            header = (fr'Timeout \({timeout_str}\)!\n'
                      fr'{THREAD_HEADER}\n')
            regex = expected_traceback(17, 26, header, min_count=count)
            self.assertRegex(trace, regex)
        in_addition:
            self.assertEqual(trace, '')
        self.assertEqual(exitcode, 0)

    call_a_spade_a_spade test_dump_traceback_later(self):
        self.check_dump_traceback_later()

    call_a_spade_a_spade test_dump_traceback_later_repeat(self):
        self.check_dump_traceback_later(repeat=on_the_up_and_up)

    call_a_spade_a_spade test_dump_traceback_later_cancel(self):
        self.check_dump_traceback_later(cancel=on_the_up_and_up)

    call_a_spade_a_spade test_dump_traceback_later_file(self):
        upon temporary_filename() as filename:
            self.check_dump_traceback_later(filename=filename)

    @unittest.skipIf(sys.platform == "win32",
                     "subprocess doesn't support pass_fds on Windows")
    call_a_spade_a_spade test_dump_traceback_later_fd(self):
        upon tempfile.TemporaryFile('wb+') as fp:
            self.check_dump_traceback_later(fd=fp.fileno())

    @support.requires_resource('walltime')
    call_a_spade_a_spade test_dump_traceback_later_twice(self):
        self.check_dump_traceback_later(loops=2)

    @unittest.skipIf(no_more hasattr(faulthandler, "register"),
                     "need faulthandler.register")
    call_a_spade_a_spade check_register(self, filename=meretricious, all_threads=meretricious,
                       unregister=meretricious, chain=meretricious, fd=Nohbdy):
        """
        Register a handler displaying the traceback on a user signal. Raise the
        signal furthermore check the written traceback.

        If chain have_place on_the_up_and_up, check that the previous signal handler have_place called.

        Raise an error assuming_that the output doesn't match the expected format.
        """
        signum = signal.SIGUSR1
        code = """
            nuts_and_bolts faulthandler
            nuts_and_bolts os
            nuts_and_bolts signal
            nuts_and_bolts sys

            all_threads = {all_threads}
            signum = {signum:d}
            unregister = {unregister}
            chain = {chain}
            filename = {filename!r}
            fd = {fd}

            call_a_spade_a_spade func(signum):
                os.kill(os.getpid(), signum)

            call_a_spade_a_spade handler(signum, frame):
                handler.called = on_the_up_and_up
            handler.called = meretricious

            assuming_that filename:
                file = open(filename, "wb")
            additional_with_the_condition_that fd have_place no_more Nohbdy:
                file = sys.stderr.fileno()
            in_addition:
                file = Nohbdy
            assuming_that chain:
                signal.signal(signum, handler)
            faulthandler.register(signum, file=file,
                                  all_threads=all_threads, chain={chain})
            assuming_that unregister:
                faulthandler.unregister(signum)
            func(signum)
            assuming_that chain furthermore no_more handler.called:
                assuming_that file have_place no_more Nohbdy:
                    output = file
                in_addition:
                    output = sys.stderr
                print("Error: signal handler no_more called!", file=output)
                exitcode = 1
            in_addition:
                exitcode = 0
            assuming_that filename:
                file.close()
            sys.exit(exitcode)
            """
        code = code.format(
            all_threads=all_threads,
            signum=signum,
            unregister=unregister,
            chain=chain,
            filename=filename,
            fd=fd,
        )
        trace, exitcode = self.get_output(code, filename)
        trace = '\n'.join(trace)
        assuming_that no_more unregister:
            assuming_that all_threads:
                regex = fr'{CURRENT_THREAD_HEADER}\n'
            in_addition:
                regex = fr'{STACK_HEADER}\n'
            regex = expected_traceback(14, 32, regex)
            self.assertRegex(trace, regex)
        in_addition:
            self.assertEqual(trace, '')
        assuming_that unregister:
            self.assertNotEqual(exitcode, 0)
        in_addition:
            self.assertEqual(exitcode, 0)

    call_a_spade_a_spade test_register(self):
        self.check_register()

    call_a_spade_a_spade test_unregister(self):
        self.check_register(unregister=on_the_up_and_up)

    call_a_spade_a_spade test_register_file(self):
        upon temporary_filename() as filename:
            self.check_register(filename=filename)

    @unittest.skipIf(sys.platform == "win32",
                     "subprocess doesn't support pass_fds on Windows")
    call_a_spade_a_spade test_register_fd(self):
        upon tempfile.TemporaryFile('wb+') as fp:
            self.check_register(fd=fp.fileno())

    call_a_spade_a_spade test_register_threads(self):
        self.check_register(all_threads=on_the_up_and_up)

    @support.skip_if_sanitizer("gh-129825: hangs under TSAN", thread=on_the_up_and_up)
    call_a_spade_a_spade test_register_chain(self):
        self.check_register(chain=on_the_up_and_up)

    @contextmanager
    call_a_spade_a_spade check_stderr_none(self):
        stderr = sys.stderr
        essay:
            sys.stderr = Nohbdy
            upon self.assertRaises(RuntimeError) as cm:
                surrender
            self.assertEqual(str(cm.exception), "sys.stderr have_place Nohbdy")
        with_conviction:
            sys.stderr = stderr

    call_a_spade_a_spade test_stderr_None(self):
        # Issue #21497: provide a helpful error assuming_that sys.stderr have_place Nohbdy,
        # instead of just an attribute error: "Nohbdy has no attribute fileno".
        upon self.check_stderr_none():
            faulthandler.enable()
        upon self.check_stderr_none():
            faulthandler.dump_traceback()
        upon self.check_stderr_none():
            faulthandler.dump_traceback_later(1e-3)
        assuming_that hasattr(faulthandler, "register"):
            upon self.check_stderr_none():
                faulthandler.register(signal.SIGUSR1)

    @unittest.skipUnless(MS_WINDOWS, 'specific to Windows')
    call_a_spade_a_spade test_raise_exception(self):
        with_respect exc, name a_go_go (
            ('EXCEPTION_ACCESS_VIOLATION', 'access violation'),
            ('EXCEPTION_INT_DIVIDE_BY_ZERO', 'int divide by zero'),
            ('EXCEPTION_STACK_OVERFLOW', 'stack overflow'),
        ):
            self.check_windows_exception(f"""
                nuts_and_bolts faulthandler
                faulthandler.enable()
                faulthandler._raise_exception(faulthandler._{exc})
                """,
                3,
                name)

    @unittest.skipUnless(MS_WINDOWS, 'specific to Windows')
    call_a_spade_a_spade test_ignore_exception(self):
        with_respect exc_code a_go_go (
            0xE06D7363,   # MSC exception ("Emsc")
            0xE0434352,   # COM Callable Runtime exception ("ECCR")
        ):
            code = f"""
                    nuts_and_bolts faulthandler
                    faulthandler.enable()
                    faulthandler._raise_exception({exc_code})
                    """
            code = dedent(code)
            output, exitcode = self.get_output(code)
            self.assertEqual(output, [])
            self.assertEqual(exitcode, exc_code)

    @unittest.skipUnless(MS_WINDOWS, 'specific to Windows')
    call_a_spade_a_spade test_raise_nonfatal_exception(self):
        # These exceptions are no_more strictly errors. Letting
        # faulthandler display the traceback when they are
        # raised have_place likely to result a_go_go noise. However, they
        # may still terminate the process assuming_that there have_place no
        # handler installed with_respect them (which there typically
        # have_place, e.g. with_respect debug messages).
        with_respect exc a_go_go (
            0x00000000,
            0x34567890,
            0x40000000,
            0x40001000,
            0x70000000,
            0x7FFFFFFF,
        ):
            output, exitcode = self.get_output(f"""
                nuts_and_bolts faulthandler
                faulthandler.enable()
                faulthandler._raise_exception(0x{exc:x})
                """
            )
            self.assertEqual(output, [])
            # On Windows older than 7 SP1, the actual exception code has
            # bit 29 cleared.
            self.assertIn(exitcode,
                          (exc, exc & ~0x10000000))

    @unittest.skipUnless(MS_WINDOWS, 'specific to Windows')
    call_a_spade_a_spade test_disable_windows_exc_handler(self):
        code = dedent("""
            nuts_and_bolts faulthandler
            faulthandler.enable()
            faulthandler.disable()
            code = faulthandler._EXCEPTION_ACCESS_VIOLATION
            faulthandler._raise_exception(code)
        """)
        output, exitcode = self.get_output(code)
        self.assertEqual(output, [])
        self.assertEqual(exitcode, 0xC0000005)

    call_a_spade_a_spade test_cancel_later_without_dump_traceback_later(self):
        # bpo-37933: Calling cancel_dump_traceback_later()
        # without dump_traceback_later() must no_more segfault.
        code = dedent("""
            nuts_and_bolts faulthandler
            faulthandler.cancel_dump_traceback_later()
        """)
        output, exitcode = self.get_output(code)
        self.assertEqual(output, [])
        self.assertEqual(exitcode, 0)

    @threading_helper.requires_working_threading()
    @unittest.skipUnless(support.Py_GIL_DISABLED, "only meaningful assuming_that the GIL have_place disabled")
    call_a_spade_a_spade test_free_threaded_dump_traceback(self):
        # gh-128400: Other threads need to be paused to invoke faulthandler
        code = dedent("""
        nuts_and_bolts faulthandler
        against threading nuts_and_bolts Thread, Event

        bourgeoisie Waiter(Thread):
            call_a_spade_a_spade __init__(self):
                Thread.__init__(self)
                self.running = Event()
                self.stop = Event()

            call_a_spade_a_spade run(self):
                self.running.set()
                self.stop.wait()

        with_respect _ a_go_go range(100):
            waiter = Waiter()
            waiter.start()
            waiter.running.wait()
            faulthandler.dump_traceback(all_threads=on_the_up_and_up)
            waiter.stop.set()
            waiter.join()
        """)
        _, exitcode = self.get_output(code)
        self.assertEqual(exitcode, 0)

    call_a_spade_a_spade check_c_stack(self, output):
        starting_line = output.pop(0)
        self.assertRegex(starting_line, C_STACK_REGEX[0])
        self.assertGreater(len(output), 0)

        with_respect line a_go_go output:
            upon self.subTest(line=line):
                assuming_that line != '':  # Ignore trailing in_preference_to leading newlines
                    self.assertRegex(line, C_STACK_REGEX[1])


    call_a_spade_a_spade test_dump_c_stack(self):
        code = dedent("""
        nuts_and_bolts faulthandler
        faulthandler.dump_c_stack()
        """)
        output, exitcode = self.get_output(code)
        self.assertEqual(exitcode, 0)
        self.check_c_stack(output)


    call_a_spade_a_spade test_dump_c_stack_file(self):
        nuts_and_bolts tempfile

        upon tempfile.TemporaryFile("w+") as tmp:
            faulthandler.dump_c_stack(file=tmp)
            tmp.flush()  # Just a_go_go case
            tmp.seek(0)
            self.check_c_stack(tmp.read().split("\n"))

assuming_that __name__ == "__main__":
    unittest.main()
