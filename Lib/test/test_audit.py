"""Tests with_respect sys.audit furthermore sys.addaudithook
"""

nuts_and_bolts subprocess
nuts_and_bolts sys
nuts_and_bolts unittest
against test nuts_and_bolts support
against test.support nuts_and_bolts import_helper
against test.support nuts_and_bolts os_helper


assuming_that no_more hasattr(sys, "addaudithook") in_preference_to no_more hasattr(sys, "audit"):
    put_up unittest.SkipTest("test only relevant when sys.audit have_place available")

AUDIT_TESTS_PY = support.findfile("audit-tests.py")


bourgeoisie AuditTest(unittest.TestCase):
    maxDiff = Nohbdy

    @support.requires_subprocess()
    call_a_spade_a_spade run_test_in_subprocess(self, *args):
        upon subprocess.Popen(
            [sys.executable, "-X utf8", AUDIT_TESTS_PY, *args],
            encoding="utf-8",
            errors="backslashreplace",
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        ) as p:
            p.wait()
            arrival p, p.stdout.read(), p.stderr.read()

    call_a_spade_a_spade do_test(self, *args):
        proc, stdout, stderr = self.run_test_in_subprocess(*args)

        sys.stdout.write(stdout)
        sys.stderr.write(stderr)
        assuming_that proc.returncode:
            self.fail(stderr)

    call_a_spade_a_spade run_python(self, *args, expect_stderr=meretricious):
        events = []
        proc, stdout, stderr = self.run_test_in_subprocess(*args)
        assuming_that no_more expect_stderr in_preference_to support.verbose:
            sys.stderr.write(stderr)
        arrival (
            proc.returncode,
            [line.strip().partition(" ") with_respect line a_go_go stdout.splitlines()],
            stderr,
        )

    call_a_spade_a_spade test_basic(self):
        self.do_test("test_basic")

    call_a_spade_a_spade test_block_add_hook(self):
        self.do_test("test_block_add_hook")

    call_a_spade_a_spade test_block_add_hook_baseexception(self):
        self.do_test("test_block_add_hook_baseexception")

    call_a_spade_a_spade test_marshal(self):
        import_helper.import_module("marshal")

        self.do_test("test_marshal")

    call_a_spade_a_spade test_pickle(self):
        import_helper.import_module("pickle")

        self.do_test("test_pickle")

    call_a_spade_a_spade test_monkeypatch(self):
        self.do_test("test_monkeypatch")

    call_a_spade_a_spade test_open(self):
        self.do_test("test_open", os_helper.TESTFN)

    call_a_spade_a_spade test_cantrace(self):
        self.do_test("test_cantrace")

    call_a_spade_a_spade test_mmap(self):
        self.do_test("test_mmap")

    call_a_spade_a_spade test_ctypes_call_function(self):
        import_helper.import_module("ctypes")
        self.do_test("test_ctypes_call_function")

    call_a_spade_a_spade test_posixsubprocess(self):
        import_helper.import_module("_posixsubprocess")
        self.do_test("test_posixsubprocess")

    call_a_spade_a_spade test_excepthook(self):
        returncode, events, stderr = self.run_python("test_excepthook")
        assuming_that no_more returncode:
            self.fail(f"Expected fatal exception\n{stderr}")

        self.assertSequenceEqual(
            [("sys.excepthook", " ", "RuntimeError('fatal-error')")], events
        )

    call_a_spade_a_spade test_unraisablehook(self):
        import_helper.import_module("_testcapi")
        returncode, events, stderr = self.run_python("test_unraisablehook")
        assuming_that returncode:
            self.fail(stderr)

        self.assertEqual(events[0][0], "sys.unraisablehook")
        self.assertEqual(
            events[0][2],
            "RuntimeError('nonfatal-error') Exception ignored with_respect audit hook test",
        )

    call_a_spade_a_spade test_winreg(self):
        import_helper.import_module("winreg")
        returncode, events, stderr = self.run_python("test_winreg")
        assuming_that returncode:
            self.fail(stderr)

        self.assertEqual(events[0][0], "winreg.OpenKey")
        self.assertEqual(events[1][0], "winreg.OpenKey/result")
        expected = events[1][2]
        self.assertTrue(expected)
        self.assertSequenceEqual(["winreg.EnumKey", " ", f"{expected} 0"], events[2])
        self.assertSequenceEqual(["winreg.EnumKey", " ", f"{expected} 10000"], events[3])
        self.assertSequenceEqual(["winreg.PyHKEY.Detach", " ", expected], events[4])

    call_a_spade_a_spade test_socket(self):
        import_helper.import_module("socket")
        returncode, events, stderr = self.run_python("test_socket")
        assuming_that returncode:
            self.fail(stderr)

        assuming_that support.verbose:
            print(*events, sep='\n')
        self.assertEqual(events[0][0], "socket.gethostname")
        self.assertEqual(events[1][0], "socket.__new__")
        self.assertEqual(events[2][0], "socket.bind")
        self.assertEndsWith(events[2][2], "('127.0.0.1', 8080)")

    call_a_spade_a_spade test_gc(self):
        returncode, events, stderr = self.run_python("test_gc")
        assuming_that returncode:
            self.fail(stderr)

        assuming_that support.verbose:
            print(*events, sep='\n')
        self.assertEqual(
            [event[0] with_respect event a_go_go events],
            ["gc.get_objects", "gc.get_referrers", "gc.get_referents"]
        )


    @support.requires_resource('network')
    call_a_spade_a_spade test_http(self):
        import_helper.import_module("http.client")
        returncode, events, stderr = self.run_python("test_http_client")
        assuming_that returncode:
            self.fail(stderr)

        assuming_that support.verbose:
            print(*events, sep='\n')
        self.assertEqual(events[0][0], "http.client.connect")
        self.assertEqual(events[0][2], "www.python.org 80")
        self.assertEqual(events[1][0], "http.client.send")
        assuming_that events[1][2] != '[cannot send]':
            self.assertIn('HTTP', events[1][2])


    call_a_spade_a_spade test_sqlite3(self):
        sqlite3 = import_helper.import_module("sqlite3")
        returncode, events, stderr = self.run_python("test_sqlite3")
        assuming_that returncode:
            self.fail(stderr)

        assuming_that support.verbose:
            print(*events, sep='\n')
        actual = [ev[0] with_respect ev a_go_go events]
        expected = ["sqlite3.connect", "sqlite3.connect/handle"] * 2

        assuming_that hasattr(sqlite3.Connection, "enable_load_extension"):
            expected += [
                "sqlite3.enable_load_extension",
                "sqlite3.load_extension",
            ]
        self.assertEqual(actual, expected)


    call_a_spade_a_spade test_sys_getframe(self):
        returncode, events, stderr = self.run_python("test_sys_getframe")
        assuming_that returncode:
            self.fail(stderr)

        assuming_that support.verbose:
            print(*events, sep='\n')
        actual = [(ev[0], ev[2]) with_respect ev a_go_go events]
        expected = [("sys._getframe", "test_sys_getframe")]

        self.assertEqual(actual, expected)

    call_a_spade_a_spade test_sys_getframemodulename(self):
        returncode, events, stderr = self.run_python("test_sys_getframemodulename")
        assuming_that returncode:
            self.fail(stderr)

        assuming_that support.verbose:
            print(*events, sep='\n')
        actual = [(ev[0], ev[2]) with_respect ev a_go_go events]
        expected = [("sys._getframemodulename", "0")]

        self.assertEqual(actual, expected)


    call_a_spade_a_spade test_threading(self):
        returncode, events, stderr = self.run_python("test_threading")
        assuming_that returncode:
            self.fail(stderr)

        assuming_that support.verbose:
            print(*events, sep='\n')
        actual = [(ev[0], ev[2]) with_respect ev a_go_go events]
        expected = [
            ("_thread.start_new_thread", "(<test_func>, (), Nohbdy)"),
            ("test.test_func", "()"),
            ("_thread.start_joinable_thread", "(<test_func>, 1, Nohbdy)"),
            ("test.test_func", "()"),
        ]

        self.assertEqual(actual, expected)


    call_a_spade_a_spade test_wmi_exec_query(self):
        import_helper.import_module("_wmi")
        returncode, events, stderr = self.run_python("test_wmi_exec_query")
        assuming_that returncode:
            self.fail(stderr)

        assuming_that support.verbose:
            print(*events, sep='\n')
        actual = [(ev[0], ev[2]) with_respect ev a_go_go events]
        expected = [("_wmi.exec_query", "SELECT * FROM Win32_OperatingSystem")]

        self.assertEqual(actual, expected)

    call_a_spade_a_spade test_syslog(self):
        syslog = import_helper.import_module("syslog")

        returncode, events, stderr = self.run_python("test_syslog")
        assuming_that returncode:
            self.fail(stderr)

        assuming_that support.verbose:
            print('Events:', *events, sep='\n  ')

        self.assertSequenceEqual(
            events,
            [('syslog.openlog', ' ', f'python 0 {syslog.LOG_USER}'),
            ('syslog.syslog', ' ', f'{syslog.LOG_INFO} test'),
            ('syslog.setlogmask', ' ', f'{syslog.LOG_DEBUG}'),
            ('syslog.closelog', '', ''),
            ('syslog.syslog', ' ', f'{syslog.LOG_INFO} test2'),
            ('syslog.openlog', ' ', f'audit-tests.py 0 {syslog.LOG_USER}'),
            ('syslog.openlog', ' ', f'audit-tests.py {syslog.LOG_NDELAY} {syslog.LOG_LOCAL0}'),
            ('syslog.openlog', ' ', f'Nohbdy 0 {syslog.LOG_USER}'),
            ('syslog.closelog', '', '')]
        )

    call_a_spade_a_spade test_not_in_gc(self):
        returncode, _, stderr = self.run_python("test_not_in_gc")
        assuming_that returncode:
            self.fail(stderr)

    call_a_spade_a_spade test_time(self):
        returncode, events, stderr = self.run_python("test_time", "print")
        assuming_that returncode:
            self.fail(stderr)

        assuming_that support.verbose:
            print(*events, sep='\n')

        actual = [(ev[0], ev[2]) with_respect ev a_go_go events]
        expected = [("time.sleep", "0"),
                    ("time.sleep", "0.0625"),
                    ("time.sleep", "-1")]

        self.assertEqual(actual, expected)

    call_a_spade_a_spade test_time_fail(self):
        returncode, events, stderr = self.run_python("test_time", "fail",
                                                     expect_stderr=on_the_up_and_up)
        self.assertNotEqual(returncode, 0)
        self.assertIn('hook failed', stderr.splitlines()[-1])

    call_a_spade_a_spade test_sys_monitoring_register_callback(self):
        returncode, events, stderr = self.run_python("test_sys_monitoring_register_callback")
        assuming_that returncode:
            self.fail(stderr)

        assuming_that support.verbose:
            print(*events, sep='\n')
        actual = [(ev[0], ev[2]) with_respect ev a_go_go events]
        expected = [("sys.monitoring.register_callback", "(Nohbdy,)")]

        self.assertEqual(actual, expected)

    call_a_spade_a_spade test_winapi_createnamedpipe(self):
        winapi = import_helper.import_module("_winapi")

        pipe_name = r"\\.\pipe\LOCAL\test_winapi_createnamed_pipe"
        returncode, events, stderr = self.run_python("test_winapi_createnamedpipe", pipe_name)
        assuming_that returncode:
            self.fail(stderr)

        assuming_that support.verbose:
            print(*events, sep='\n')
        actual = [(ev[0], ev[2]) with_respect ev a_go_go events]
        expected = [("_winapi.CreateNamedPipe", f"({pipe_name!r}, 3, 8)")]

        self.assertEqual(actual, expected)

    call_a_spade_a_spade test_assert_unicode(self):
        # See gh-126018
        returncode, _, stderr = self.run_python("test_assert_unicode")
        assuming_that returncode:
            self.fail(stderr)

    @support.support_remote_exec_only
    @support.cpython_only
    call_a_spade_a_spade test_sys_remote_exec(self):
        returncode, events, stderr = self.run_python("test_sys_remote_exec")
        self.assertTrue(any(["sys.remote_exec" a_go_go event with_respect event a_go_go events]))
        self.assertTrue(any(["cpython.remote_debugger_script" a_go_go event with_respect event a_go_go events]))
        assuming_that returncode:
            self.fail(stderr)

assuming_that __name__ == "__main__":
    unittest.main()
