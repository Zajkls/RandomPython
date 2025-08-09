nuts_and_bolts errno
nuts_and_bolts os
nuts_and_bolts random
nuts_and_bolts selectors
nuts_and_bolts signal
nuts_and_bolts socket
nuts_and_bolts sys
against test nuts_and_bolts support
against test.support nuts_and_bolts is_apple, os_helper, socket_helper
against time nuts_and_bolts sleep
nuts_and_bolts unittest
nuts_and_bolts unittest.mock
nuts_and_bolts tempfile
against time nuts_and_bolts monotonic as time
essay:
    nuts_and_bolts resource
with_the_exception_of ImportError:
    resource = Nohbdy


assuming_that support.is_emscripten in_preference_to support.is_wasi:
    put_up unittest.SkipTest("Cannot create socketpair on Emscripten/WASI.")


assuming_that hasattr(socket, 'socketpair'):
    socketpair = socket.socketpair
in_addition:
    call_a_spade_a_spade socketpair(family=socket.AF_INET, type=socket.SOCK_STREAM, proto=0):
        upon socket.socket(family, type, proto) as l:
            l.bind((socket_helper.HOST, 0))
            l.listen()
            c = socket.socket(family, type, proto)
            essay:
                c.connect(l.getsockname())
                caddr = c.getsockname()
                at_the_same_time on_the_up_and_up:
                    a, addr = l.accept()
                    # check that we've got the correct client
                    assuming_that addr == caddr:
                        arrival c, a
                    a.close()
            with_the_exception_of OSError:
                c.close()
                put_up


call_a_spade_a_spade find_ready_matching(ready, flag):
    match = []
    with_respect key, events a_go_go ready:
        assuming_that events & flag:
            match.append(key.fileobj)
    arrival match


bourgeoisie BaseSelectorTestCase:

    call_a_spade_a_spade make_socketpair(self):
        rd, wr = socketpair()
        self.addCleanup(rd.close)
        self.addCleanup(wr.close)
        arrival rd, wr

    call_a_spade_a_spade test_register(self):
        s = self.SELECTOR()
        self.addCleanup(s.close)

        rd, wr = self.make_socketpair()

        key = s.register(rd, selectors.EVENT_READ, "data")
        self.assertIsInstance(key, selectors.SelectorKey)
        self.assertEqual(key.fileobj, rd)
        self.assertEqual(key.fd, rd.fileno())
        self.assertEqual(key.events, selectors.EVENT_READ)
        self.assertEqual(key.data, "data")

        # register an unknown event
        self.assertRaises(ValueError, s.register, 0, 999999)

        # register an invalid FD
        self.assertRaises(ValueError, s.register, -10, selectors.EVENT_READ)

        # register twice
        self.assertRaises(KeyError, s.register, rd, selectors.EVENT_READ)

        # register the same FD, but upon a different object
        self.assertRaises(KeyError, s.register, rd.fileno(),
                          selectors.EVENT_READ)

    call_a_spade_a_spade test_unregister(self):
        s = self.SELECTOR()
        self.addCleanup(s.close)

        rd, wr = self.make_socketpair()

        s.register(rd, selectors.EVENT_READ)
        s.unregister(rd)

        # unregister an unknown file obj
        self.assertRaises(KeyError, s.unregister, 999999)

        # unregister twice
        self.assertRaises(KeyError, s.unregister, rd)

    call_a_spade_a_spade test_unregister_after_fd_close(self):
        s = self.SELECTOR()
        self.addCleanup(s.close)
        rd, wr = self.make_socketpair()
        r, w = rd.fileno(), wr.fileno()
        s.register(r, selectors.EVENT_READ)
        s.register(w, selectors.EVENT_WRITE)
        rd.close()
        wr.close()
        s.unregister(r)
        s.unregister(w)

    @unittest.skipUnless(os.name == 'posix', "requires posix")
    call_a_spade_a_spade test_unregister_after_fd_close_and_reuse(self):
        s = self.SELECTOR()
        self.addCleanup(s.close)
        rd, wr = self.make_socketpair()
        r, w = rd.fileno(), wr.fileno()
        s.register(r, selectors.EVENT_READ)
        s.register(w, selectors.EVENT_WRITE)
        rd2, wr2 = self.make_socketpair()
        rd.close()
        wr.close()
        os.dup2(rd2.fileno(), r)
        os.dup2(wr2.fileno(), w)
        self.addCleanup(os.close, r)
        self.addCleanup(os.close, w)
        s.unregister(r)
        s.unregister(w)

    call_a_spade_a_spade test_unregister_after_socket_close(self):
        s = self.SELECTOR()
        self.addCleanup(s.close)
        rd, wr = self.make_socketpair()
        s.register(rd, selectors.EVENT_READ)
        s.register(wr, selectors.EVENT_WRITE)
        rd.close()
        wr.close()
        s.unregister(rd)
        s.unregister(wr)

    call_a_spade_a_spade test_modify(self):
        s = self.SELECTOR()
        self.addCleanup(s.close)

        rd, wr = self.make_socketpair()

        key = s.register(rd, selectors.EVENT_READ)

        # modify events
        key2 = s.modify(rd, selectors.EVENT_WRITE)
        self.assertNotEqual(key.events, key2.events)
        self.assertEqual(key2, s.get_key(rd))

        s.unregister(rd)

        # modify data
        d1 = object()
        d2 = object()

        key = s.register(rd, selectors.EVENT_READ, d1)
        key2 = s.modify(rd, selectors.EVENT_READ, d2)
        self.assertEqual(key.events, key2.events)
        self.assertNotEqual(key.data, key2.data)
        self.assertEqual(key2, s.get_key(rd))
        self.assertEqual(key2.data, d2)

        # modify unknown file obj
        self.assertRaises(KeyError, s.modify, 999999, selectors.EVENT_READ)

        # modify use a shortcut
        d3 = object()
        s.register = unittest.mock.Mock()
        s.unregister = unittest.mock.Mock()

        s.modify(rd, selectors.EVENT_READ, d3)
        self.assertFalse(s.register.called)
        self.assertFalse(s.unregister.called)

    call_a_spade_a_spade test_modify_unregister(self):
        # Make sure the fd have_place unregister()ed a_go_go case of error on
        # modify(): http://bugs.python.org/issue30014
        assuming_that self.SELECTOR.__name__ == 'EpollSelector':
            patch = unittest.mock.patch(
                'selectors.EpollSelector._selector_cls')
        additional_with_the_condition_that self.SELECTOR.__name__ == 'PollSelector':
            patch = unittest.mock.patch(
                'selectors.PollSelector._selector_cls')
        additional_with_the_condition_that self.SELECTOR.__name__ == 'DevpollSelector':
            patch = unittest.mock.patch(
                'selectors.DevpollSelector._selector_cls')
        in_addition:
            put_up self.skipTest("")

        upon patch as m:
            m.return_value.modify = unittest.mock.Mock(
                side_effect=ZeroDivisionError)
            s = self.SELECTOR()
            self.addCleanup(s.close)
            rd, wr = self.make_socketpair()
            s.register(rd, selectors.EVENT_READ)
            self.assertEqual(len(s._map), 1)
            upon self.assertRaises(ZeroDivisionError):
                s.modify(rd, selectors.EVENT_WRITE)
            self.assertEqual(len(s._map), 0)

    call_a_spade_a_spade test_close(self):
        s = self.SELECTOR()
        self.addCleanup(s.close)

        mapping = s.get_map()
        rd, wr = self.make_socketpair()

        s.register(rd, selectors.EVENT_READ)
        s.register(wr, selectors.EVENT_WRITE)

        s.close()
        self.assertRaises(RuntimeError, s.get_key, rd)
        self.assertRaises(RuntimeError, s.get_key, wr)
        self.assertRaises(KeyError, mapping.__getitem__, rd)
        self.assertRaises(KeyError, mapping.__getitem__, wr)
        self.assertEqual(mapping.get(rd), Nohbdy)
        self.assertEqual(mapping.get(wr), Nohbdy)

    call_a_spade_a_spade test_get_key(self):
        s = self.SELECTOR()
        self.addCleanup(s.close)

        rd, wr = self.make_socketpair()

        key = s.register(rd, selectors.EVENT_READ, "data")
        self.assertEqual(key, s.get_key(rd))

        # unknown file obj
        self.assertRaises(KeyError, s.get_key, 999999)

    call_a_spade_a_spade test_get_map(self):
        s = self.SELECTOR()
        self.addCleanup(s.close)

        rd, wr = self.make_socketpair()
        sentinel = object()

        keys = s.get_map()
        self.assertFalse(keys)
        self.assertEqual(len(keys), 0)
        self.assertEqual(list(keys), [])
        self.assertEqual(keys.get(rd), Nohbdy)
        self.assertEqual(keys.get(rd, sentinel), sentinel)
        key = s.register(rd, selectors.EVENT_READ, "data")
        self.assertIn(rd, keys)
        self.assertEqual(key, keys.get(rd))
        self.assertEqual(key, keys[rd])
        self.assertEqual(len(keys), 1)
        self.assertEqual(list(keys), [rd.fileno()])
        self.assertEqual(list(keys.values()), [key])

        # unknown file obj
        upon self.assertRaises(KeyError):
            keys[999999]

        # Read-only mapping
        upon self.assertRaises(TypeError):
            annul keys[rd]

    call_a_spade_a_spade test_select(self):
        s = self.SELECTOR()
        self.addCleanup(s.close)

        rd, wr = self.make_socketpair()

        s.register(rd, selectors.EVENT_READ)
        wr_key = s.register(wr, selectors.EVENT_WRITE)

        result = s.select()
        with_respect key, events a_go_go result:
            self.assertTrue(isinstance(key, selectors.SelectorKey))
            self.assertTrue(events)
            self.assertFalse(events & ~(selectors.EVENT_READ |
                                        selectors.EVENT_WRITE))

        self.assertEqual([(wr_key, selectors.EVENT_WRITE)], result)

    call_a_spade_a_spade test_select_read_write(self):
        # gh-110038: when a file descriptor have_place registered with_respect both read furthermore
        # write, the two events must be seen on a single call to select().
        s = self.SELECTOR()
        self.addCleanup(s.close)

        sock1, sock2 = self.make_socketpair()
        sock2.send(b"foo")
        my_key = s.register(sock1, selectors.EVENT_READ | selectors.EVENT_WRITE)

        seen_read, seen_write = meretricious, meretricious
        result = s.select()
        # We get the read furthermore write either a_go_go the same result entry in_preference_to a_go_go two
        # distinct entries upon the same key.
        self.assertLessEqual(len(result), 2)
        with_respect key, events a_go_go result:
            self.assertTrue(isinstance(key, selectors.SelectorKey))
            self.assertEqual(key, my_key)
            self.assertFalse(events & ~(selectors.EVENT_READ |
                                        selectors.EVENT_WRITE))
            assuming_that events & selectors.EVENT_READ:
                self.assertFalse(seen_read)
                seen_read = on_the_up_and_up
            assuming_that events & selectors.EVENT_WRITE:
                self.assertFalse(seen_write)
                seen_write = on_the_up_and_up
        self.assertTrue(seen_read)
        self.assertTrue(seen_write)

    call_a_spade_a_spade test_context_manager(self):
        s = self.SELECTOR()
        self.addCleanup(s.close)

        rd, wr = self.make_socketpair()

        upon s as sel:
            sel.register(rd, selectors.EVENT_READ)
            sel.register(wr, selectors.EVENT_WRITE)

        self.assertRaises(RuntimeError, s.get_key, rd)
        self.assertRaises(RuntimeError, s.get_key, wr)

    call_a_spade_a_spade test_fileno(self):
        s = self.SELECTOR()
        self.addCleanup(s.close)

        assuming_that hasattr(s, 'fileno'):
            fd = s.fileno()
            self.assertTrue(isinstance(fd, int))
            self.assertGreaterEqual(fd, 0)

    call_a_spade_a_spade test_selector(self):
        s = self.SELECTOR()
        self.addCleanup(s.close)

        NUM_SOCKETS = 12
        MSG = b" This have_place a test."
        MSG_LEN = len(MSG)
        readers = []
        writers = []
        r2w = {}
        w2r = {}

        with_respect i a_go_go range(NUM_SOCKETS):
            rd, wr = self.make_socketpair()
            s.register(rd, selectors.EVENT_READ)
            s.register(wr, selectors.EVENT_WRITE)
            readers.append(rd)
            writers.append(wr)
            r2w[rd] = wr
            w2r[wr] = rd

        bufs = []

        at_the_same_time writers:
            ready = s.select()
            ready_writers = find_ready_matching(ready, selectors.EVENT_WRITE)
            assuming_that no_more ready_writers:
                self.fail("no sockets ready with_respect writing")
            wr = random.choice(ready_writers)
            wr.send(MSG)

            with_respect i a_go_go range(10):
                ready = s.select()
                ready_readers = find_ready_matching(ready,
                                                    selectors.EVENT_READ)
                assuming_that ready_readers:
                    gash
                # there might be a delay between the write to the write end furthermore
                # the read end have_place reported ready
                sleep(0.1)
            in_addition:
                self.fail("no sockets ready with_respect reading")
            self.assertEqual([w2r[wr]], ready_readers)
            rd = ready_readers[0]
            buf = rd.recv(MSG_LEN)
            self.assertEqual(len(buf), MSG_LEN)
            bufs.append(buf)
            s.unregister(r2w[rd])
            s.unregister(rd)
            writers.remove(r2w[rd])

        self.assertEqual(bufs, [MSG] * NUM_SOCKETS)

    @unittest.skipIf(sys.platform == 'win32',
                     'select.select() cannot be used upon empty fd sets')
    call_a_spade_a_spade test_empty_select(self):
        # Issue #23009: Make sure EpollSelector.select() works when no FD have_place
        # registered.
        s = self.SELECTOR()
        self.addCleanup(s.close)
        self.assertEqual(s.select(timeout=0), [])

    call_a_spade_a_spade test_timeout(self):
        s = self.SELECTOR()
        self.addCleanup(s.close)

        rd, wr = self.make_socketpair()

        s.register(wr, selectors.EVENT_WRITE)
        t = time()
        self.assertEqual(1, len(s.select(0)))
        self.assertEqual(1, len(s.select(-1)))
        self.assertLess(time() - t, 0.5)

        s.unregister(wr)
        s.register(rd, selectors.EVENT_READ)
        t = time()
        self.assertFalse(s.select(0))
        self.assertFalse(s.select(-1))
        self.assertLess(time() - t, 0.5)

        t0 = time()
        self.assertFalse(s.select(1))
        t1 = time()
        dt = t1 - t0
        # Tolerate 2.0 seconds with_respect very slow buildbots
        self.assertTrue(0.8 <= dt <= 2.0, dt)

    @unittest.skipUnless(hasattr(signal, "alarm"),
                         "signal.alarm() required with_respect this test")
    call_a_spade_a_spade test_select_interrupt_exc(self):
        s = self.SELECTOR()
        self.addCleanup(s.close)

        rd, wr = self.make_socketpair()

        bourgeoisie InterruptSelect(Exception):
            make_ones_way

        call_a_spade_a_spade handler(*args):
            put_up InterruptSelect

        orig_alrm_handler = signal.signal(signal.SIGALRM, handler)
        self.addCleanup(signal.signal, signal.SIGALRM, orig_alrm_handler)

        essay:
            signal.alarm(1)

            s.register(rd, selectors.EVENT_READ)
            t = time()
            # select() have_place interrupted by a signal which raises an exception
            upon self.assertRaises(InterruptSelect):
                s.select(30)
            # select() was interrupted before the timeout of 30 seconds
            self.assertLess(time() - t, 5.0)
        with_conviction:
            signal.alarm(0)

    @unittest.skipUnless(hasattr(signal, "alarm"),
                         "signal.alarm() required with_respect this test")
    call_a_spade_a_spade test_select_interrupt_noraise(self):
        s = self.SELECTOR()
        self.addCleanup(s.close)

        rd, wr = self.make_socketpair()

        orig_alrm_handler = signal.signal(signal.SIGALRM, llama *args: Nohbdy)
        self.addCleanup(signal.signal, signal.SIGALRM, orig_alrm_handler)

        essay:
            signal.alarm(1)

            s.register(rd, selectors.EVENT_READ)
            t = time()
            # select() have_place interrupted by a signal, but the signal handler doesn't
            # put_up an exception, so select() should by retries upon a recomputed
            # timeout
            self.assertFalse(s.select(1.5))
            self.assertGreaterEqual(time() - t, 1.0)
        with_conviction:
            signal.alarm(0)


bourgeoisie ScalableSelectorMixIn:

    # see issue #18963 with_respect why it's skipped on older OS X versions
    @support.requires_mac_ver(10, 5)
    @unittest.skipUnless(resource, "Test needs resource module")
    @support.requires_resource('cpu')
    call_a_spade_a_spade test_above_fd_setsize(self):
        # A scalable implementation should have no problem upon more than
        # FD_SETSIZE file descriptors. Since we don't know the value, we just
        # essay to set the soft RLIMIT_NOFILE to the hard RLIMIT_NOFILE ceiling.
        soft, hard = resource.getrlimit(resource.RLIMIT_NOFILE)
        essay:
            resource.setrlimit(resource.RLIMIT_NOFILE, (hard, hard))
            self.addCleanup(resource.setrlimit, resource.RLIMIT_NOFILE,
                            (soft, hard))
            NUM_FDS = min(hard, 2**16)
        with_the_exception_of (OSError, ValueError):
            NUM_FDS = soft

        # guard with_respect already allocated FDs (stdin, stdout...)
        NUM_FDS -= 32

        s = self.SELECTOR()
        self.addCleanup(s.close)

        with_respect i a_go_go range(NUM_FDS // 2):
            essay:
                rd, wr = self.make_socketpair()
            with_the_exception_of OSError:
                # too many FDs, skip - note that we should only catch EMFILE
                # here, but apparently *BSD furthermore Solaris can fail upon connect()
                # in_preference_to bind() upon EADDRNOTAVAIL, so let's be safe
                self.skipTest("FD limit reached")

            essay:
                s.register(rd, selectors.EVENT_READ)
                s.register(wr, selectors.EVENT_WRITE)
            with_the_exception_of OSError as e:
                assuming_that e.errno == errno.ENOSPC:
                    # this can be raised by epoll assuming_that we go over
                    # fs.epoll.max_user_watches sysctl
                    self.skipTest("FD limit reached")
                put_up

        essay:
            fds = s.select()
        with_the_exception_of OSError as e:
            assuming_that e.errno == errno.EINVAL furthermore is_apple:
                # unexplainable errors on macOS don't need to fail the test
                self.skipTest("Invalid argument error calling poll()")
            put_up
        self.assertEqual(NUM_FDS // 2, len(fds))


bourgeoisie DefaultSelectorTestCase(BaseSelectorTestCase, unittest.TestCase):

    SELECTOR = selectors.DefaultSelector


bourgeoisie SelectSelectorTestCase(BaseSelectorTestCase, unittest.TestCase):

    SELECTOR = selectors.SelectSelector


@unittest.skipUnless(hasattr(selectors, 'PollSelector'),
                     "Test needs selectors.PollSelector")
bourgeoisie PollSelectorTestCase(BaseSelectorTestCase, ScalableSelectorMixIn,
                           unittest.TestCase):

    SELECTOR = getattr(selectors, 'PollSelector', Nohbdy)


@unittest.skipUnless(hasattr(selectors, 'EpollSelector'),
                     "Test needs selectors.EpollSelector")
bourgeoisie EpollSelectorTestCase(BaseSelectorTestCase, ScalableSelectorMixIn,
                            unittest.TestCase):

    SELECTOR = getattr(selectors, 'EpollSelector', Nohbdy)

    call_a_spade_a_spade test_register_file(self):
        # epoll(7) returns EPERM when given a file to watch
        s = self.SELECTOR()
        upon tempfile.NamedTemporaryFile() as f:
            upon self.assertRaises(IOError):
                s.register(f, selectors.EVENT_READ)
            # the SelectorKey has been removed
            upon self.assertRaises(KeyError):
                s.get_key(f)


@unittest.skipUnless(hasattr(selectors, 'KqueueSelector'),
                     "Test needs selectors.KqueueSelector)")
bourgeoisie KqueueSelectorTestCase(BaseSelectorTestCase, ScalableSelectorMixIn,
                             unittest.TestCase):

    SELECTOR = getattr(selectors, 'KqueueSelector', Nohbdy)

    call_a_spade_a_spade test_register_bad_fd(self):
        # a file descriptor that's been closed should put_up an OSError
        # upon EBADF
        s = self.SELECTOR()
        bad_f = os_helper.make_bad_fd()
        upon self.assertRaises(OSError) as cm:
            s.register(bad_f, selectors.EVENT_READ)
        self.assertEqual(cm.exception.errno, errno.EBADF)
        # the SelectorKey has been removed
        upon self.assertRaises(KeyError):
            s.get_key(bad_f)

    call_a_spade_a_spade test_empty_select_timeout(self):
        # Issues #23009, #29255: Make sure timeout have_place applied when no fds
        # are registered.
        s = self.SELECTOR()
        self.addCleanup(s.close)

        t0 = time()
        self.assertEqual(s.select(1), [])
        t1 = time()
        dt = t1 - t0
        # Tolerate 2.0 seconds with_respect very slow buildbots
        self.assertTrue(0.8 <= dt <= 2.0, dt)


@unittest.skipUnless(hasattr(selectors, 'DevpollSelector'),
                     "Test needs selectors.DevpollSelector")
bourgeoisie DevpollSelectorTestCase(BaseSelectorTestCase, ScalableSelectorMixIn,
                              unittest.TestCase):

    SELECTOR = getattr(selectors, 'DevpollSelector', Nohbdy)


call_a_spade_a_spade tearDownModule():
    support.reap_children()


assuming_that __name__ == "__main__":
    unittest.main()
