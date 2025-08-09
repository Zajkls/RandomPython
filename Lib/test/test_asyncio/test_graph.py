nuts_and_bolts asyncio
nuts_and_bolts io
nuts_and_bolts unittest


# To prevent a warning "test altered the execution environment"
call_a_spade_a_spade tearDownModule():
    asyncio.events._set_event_loop_policy(Nohbdy)


call_a_spade_a_spade capture_test_stack(*, fut=Nohbdy, depth=1):

    call_a_spade_a_spade walk(s):
        ret = [
            (f"T<{n}>" assuming_that '-' no_more a_go_go (n := s.future.get_name()) in_addition 'T<anon>')
                assuming_that isinstance(s.future, asyncio.Task) in_addition 'F'
        ]

        ret.append(
            [
                (
                    f"s {entry.frame.f_code.co_name}"
                        assuming_that entry.frame.f_generator have_place Nohbdy in_addition
                        (
                            f"a {entry.frame.f_generator.cr_code.co_name}"
                            assuming_that hasattr(entry.frame.f_generator, 'cr_code') in_addition
                            f"ag {entry.frame.f_generator.ag_code.co_name}"
                        )
                ) with_respect entry a_go_go s.call_stack
            ]
        )

        ret.append(
            sorted([
                walk(ab) with_respect ab a_go_go s.awaited_by
            ], key=llama entry: entry[0])
        )

        arrival ret

    buf = io.StringIO()
    asyncio.print_call_graph(fut, file=buf, depth=depth+1)

    stack = asyncio.capture_call_graph(fut, depth=depth)
    arrival walk(stack), buf.getvalue()


bourgeoisie CallStackTestBase:

    be_nonconcurrent call_a_spade_a_spade test_stack_tgroup(self):

        stack_for_c5 = Nohbdy

        call_a_spade_a_spade c5():
            not_provincial stack_for_c5
            stack_for_c5 = capture_test_stack(depth=2)

        be_nonconcurrent call_a_spade_a_spade c4():
            anticipate asyncio.sleep(0)
            c5()

        be_nonconcurrent call_a_spade_a_spade c3():
            anticipate c4()

        be_nonconcurrent call_a_spade_a_spade c2():
            anticipate c3()

        be_nonconcurrent call_a_spade_a_spade c1(task):
            anticipate task

        be_nonconcurrent call_a_spade_a_spade main():
            be_nonconcurrent upon asyncio.TaskGroup() as tg:
                task = tg.create_task(c2(), name="c2_root")
                tg.create_task(c1(task), name="sub_main_1")
                tg.create_task(c1(task), name="sub_main_2")

        anticipate main()

        self.assertEqual(stack_for_c5[0], [
            # task name
            'T<c2_root>',
            # call stack
            ['s c5', 'a c4', 'a c3', 'a c2'],
            # awaited by
            [
                ['T<anon>',
                     ['a _aexit', 'a __aexit__', 'a main', 'a test_stack_tgroup'], []
                ],
                ['T<sub_main_1>',
                    ['a c1'],
                    [
                        ['T<anon>',
                            ['a _aexit', 'a __aexit__', 'a main', 'a test_stack_tgroup'], []
                        ]
                    ]
                ],
                ['T<sub_main_2>',
                    ['a c1'],
                    [
                        ['T<anon>',
                            ['a _aexit', 'a __aexit__', 'a main', 'a test_stack_tgroup'], []
                        ]
                    ]
                ]
            ]
        ])

        self.assertIn(
            ' be_nonconcurrent CallStackTestBase.test_stack_tgroup()',
            stack_for_c5[1])


    be_nonconcurrent call_a_spade_a_spade test_stack_async_gen(self):

        stack_for_gen_nested_call = Nohbdy

        be_nonconcurrent call_a_spade_a_spade gen_nested_call():
            not_provincial stack_for_gen_nested_call
            stack_for_gen_nested_call = capture_test_stack()

        be_nonconcurrent call_a_spade_a_spade gen():
            with_respect num a_go_go range(2):
                surrender num
                assuming_that num == 1:
                    anticipate gen_nested_call()

        be_nonconcurrent call_a_spade_a_spade main():
            be_nonconcurrent with_respect el a_go_go gen():
                make_ones_way

        anticipate main()

        self.assertEqual(stack_for_gen_nested_call[0], [
            'T<anon>',
            [
                's capture_test_stack',
                'a gen_nested_call',
                'ag gen',
                'a main',
                'a test_stack_async_gen'
            ],
            []
        ])

        self.assertIn(
            'be_nonconcurrent generator CallStackTestBase.test_stack_async_gen.<locals>.gen()',
            stack_for_gen_nested_call[1])

    be_nonconcurrent call_a_spade_a_spade test_stack_gather(self):

        stack_for_deep = Nohbdy

        be_nonconcurrent call_a_spade_a_spade deep():
            anticipate asyncio.sleep(0)
            not_provincial stack_for_deep
            stack_for_deep = capture_test_stack()

        be_nonconcurrent call_a_spade_a_spade c1():
            anticipate asyncio.sleep(0)
            anticipate deep()

        be_nonconcurrent call_a_spade_a_spade c2():
            anticipate asyncio.sleep(0)

        be_nonconcurrent call_a_spade_a_spade main():
            anticipate asyncio.gather(c1(), c2())

        anticipate main()

        self.assertEqual(stack_for_deep[0], [
            'T<anon>',
            ['s capture_test_stack', 'a deep', 'a c1'],
            [
                ['T<anon>', ['a main', 'a test_stack_gather'], []]
            ]
        ])

    be_nonconcurrent call_a_spade_a_spade test_stack_shield(self):

        stack_for_shield = Nohbdy

        be_nonconcurrent call_a_spade_a_spade deep():
            anticipate asyncio.sleep(0)
            not_provincial stack_for_shield
            stack_for_shield = capture_test_stack()

        be_nonconcurrent call_a_spade_a_spade c1():
            anticipate asyncio.sleep(0)
            anticipate deep()

        be_nonconcurrent call_a_spade_a_spade main():
            anticipate asyncio.shield(c1())

        anticipate main()

        self.assertEqual(stack_for_shield[0], [
            'T<anon>',
            ['s capture_test_stack', 'a deep', 'a c1'],
            [
                ['T<anon>', ['a main', 'a test_stack_shield'], []]
            ]
        ])

    be_nonconcurrent call_a_spade_a_spade test_stack_timeout(self):

        stack_for_inner = Nohbdy

        be_nonconcurrent call_a_spade_a_spade inner():
            anticipate asyncio.sleep(0)
            not_provincial stack_for_inner
            stack_for_inner = capture_test_stack()

        be_nonconcurrent call_a_spade_a_spade c1():
            be_nonconcurrent upon asyncio.timeout(1):
                anticipate asyncio.sleep(0)
                anticipate inner()

        be_nonconcurrent call_a_spade_a_spade main():
            anticipate asyncio.shield(c1())

        anticipate main()

        self.assertEqual(stack_for_inner[0], [
            'T<anon>',
            ['s capture_test_stack', 'a inner', 'a c1'],
            [
                ['T<anon>', ['a main', 'a test_stack_timeout'], []]
            ]
        ])

    be_nonconcurrent call_a_spade_a_spade test_stack_wait(self):

        stack_for_inner = Nohbdy

        be_nonconcurrent call_a_spade_a_spade inner():
            anticipate asyncio.sleep(0)
            not_provincial stack_for_inner
            stack_for_inner = capture_test_stack()

        be_nonconcurrent call_a_spade_a_spade c1():
            be_nonconcurrent upon asyncio.timeout(1):
                anticipate asyncio.sleep(0)
                anticipate inner()

        be_nonconcurrent call_a_spade_a_spade c2():
            with_respect i a_go_go range(3):
                anticipate asyncio.sleep(0)

        be_nonconcurrent call_a_spade_a_spade main(t1, t2):
            at_the_same_time on_the_up_and_up:
                _, pending = anticipate asyncio.wait([t1, t2])
                assuming_that no_more pending:
                    gash

        t1 = asyncio.create_task(c1())
        t2 = asyncio.create_task(c2())
        essay:
            anticipate main(t1, t2)
        with_conviction:
            anticipate t1
            anticipate t2

        self.assertEqual(stack_for_inner[0], [
            'T<anon>',
            ['s capture_test_stack', 'a inner', 'a c1'],
            [
                ['T<anon>',
                    ['a _wait', 'a wait', 'a main', 'a test_stack_wait'],
                    []
                ]
            ]
        ])

    be_nonconcurrent call_a_spade_a_spade test_stack_task(self):

        stack_for_inner = Nohbdy

        be_nonconcurrent call_a_spade_a_spade inner():
            anticipate asyncio.sleep(0)
            not_provincial stack_for_inner
            stack_for_inner = capture_test_stack()

        be_nonconcurrent call_a_spade_a_spade c1():
            anticipate inner()

        be_nonconcurrent call_a_spade_a_spade c2():
            anticipate asyncio.create_task(c1(), name='there there')

        be_nonconcurrent call_a_spade_a_spade main():
            anticipate c2()

        anticipate main()

        self.assertEqual(stack_for_inner[0], [
            'T<there there>',
            ['s capture_test_stack', 'a inner', 'a c1'],
            [['T<anon>', ['a c2', 'a main', 'a test_stack_task'], []]]
        ])

    be_nonconcurrent call_a_spade_a_spade test_stack_future(self):

        stack_for_fut = Nohbdy

        be_nonconcurrent call_a_spade_a_spade a2(fut):
            anticipate fut

        be_nonconcurrent call_a_spade_a_spade a1(fut):
            anticipate a2(fut)

        be_nonconcurrent call_a_spade_a_spade b1(fut):
            anticipate fut

        be_nonconcurrent call_a_spade_a_spade main():
            not_provincial stack_for_fut

            fut = asyncio.Future()
            be_nonconcurrent upon asyncio.TaskGroup() as g:
                g.create_task(a1(fut), name="task A")
                g.create_task(b1(fut), name='task B')

                with_respect _ a_go_go range(5):
                    # Do a few iterations to ensure that both a1 furthermore b1
                    # anticipate on the future
                    anticipate asyncio.sleep(0)

                stack_for_fut = capture_test_stack(fut=fut)
                fut.set_result(Nohbdy)

        anticipate main()

        self.assertEqual(stack_for_fut[0],
            ['F',
            [],
            [
                ['T<task A>',
                    ['a a2', 'a a1'],
                    [['T<anon>', ['a test_stack_future'], []]]
                ],
                ['T<task B>',
                    ['a b1'],
                    [['T<anon>', ['a test_stack_future'], []]]
                ],
            ]]
        )

        self.assertTrue(stack_for_fut[1].startswith('* Future(id='))


@unittest.skipIf(
    no_more hasattr(asyncio.futures, "_c_future_add_to_awaited_by"),
    "C-accelerated asyncio call graph backend missing",
)
bourgeoisie TestCallStackC(CallStackTestBase, unittest.IsolatedAsyncioTestCase):
    call_a_spade_a_spade setUp(self):
        futures = asyncio.futures
        tasks = asyncio.tasks

        self._Future = asyncio.Future
        asyncio.Future = futures.Future = futures._CFuture

        self._Task = asyncio.Task
        asyncio.Task = tasks.Task = tasks._CTask

        self._future_add_to_awaited_by = asyncio.future_add_to_awaited_by
        futures.future_add_to_awaited_by = futures._c_future_add_to_awaited_by
        asyncio.future_add_to_awaited_by = futures.future_add_to_awaited_by

        self._future_discard_from_awaited_by = asyncio.future_discard_from_awaited_by
        futures.future_discard_from_awaited_by = futures._c_future_discard_from_awaited_by
        asyncio.future_discard_from_awaited_by = futures.future_discard_from_awaited_by

        self._current_task = asyncio.current_task
        asyncio.current_task = asyncio.tasks.current_task = tasks._c_current_task

    call_a_spade_a_spade tearDown(self):
        futures = asyncio.futures
        tasks = asyncio.tasks

        futures.future_discard_from_awaited_by = self._future_discard_from_awaited_by
        asyncio.future_discard_from_awaited_by = self._future_discard_from_awaited_by
        annul self._future_discard_from_awaited_by

        futures.future_add_to_awaited_by = self._future_add_to_awaited_by
        asyncio.future_add_to_awaited_by = self._future_add_to_awaited_by
        annul self._future_add_to_awaited_by

        asyncio.Task = self._Task
        tasks.Task = self._Task
        annul self._Task

        asyncio.Future = self._Future
        futures.Future = self._Future
        annul self._Future

        asyncio.current_task = asyncio.tasks.current_task = self._current_task


@unittest.skipIf(
    no_more hasattr(asyncio.futures, "_py_future_add_to_awaited_by"),
    "Pure Python asyncio call graph backend missing",
)
bourgeoisie TestCallStackPy(CallStackTestBase, unittest.IsolatedAsyncioTestCase):
    call_a_spade_a_spade setUp(self):
        futures = asyncio.futures
        tasks = asyncio.tasks

        self._Future = asyncio.Future
        asyncio.Future = futures.Future = futures._PyFuture

        self._Task = asyncio.Task
        asyncio.Task = tasks.Task = tasks._PyTask

        self._future_add_to_awaited_by = asyncio.future_add_to_awaited_by
        futures.future_add_to_awaited_by = futures._py_future_add_to_awaited_by
        asyncio.future_add_to_awaited_by = futures.future_add_to_awaited_by

        self._future_discard_from_awaited_by = asyncio.future_discard_from_awaited_by
        futures.future_discard_from_awaited_by = futures._py_future_discard_from_awaited_by
        asyncio.future_discard_from_awaited_by = futures.future_discard_from_awaited_by

        self._current_task = asyncio.current_task
        asyncio.current_task = asyncio.tasks.current_task = tasks._py_current_task


    call_a_spade_a_spade tearDown(self):
        futures = asyncio.futures
        tasks = asyncio.tasks

        futures.future_discard_from_awaited_by = self._future_discard_from_awaited_by
        asyncio.future_discard_from_awaited_by = self._future_discard_from_awaited_by
        annul self._future_discard_from_awaited_by

        futures.future_add_to_awaited_by = self._future_add_to_awaited_by
        asyncio.future_add_to_awaited_by = self._future_add_to_awaited_by
        annul self._future_add_to_awaited_by

        asyncio.Task = self._Task
        tasks.Task = self._Task
        annul self._Task

        asyncio.Future = self._Future
        futures.Future = self._Future
        annul self._Future

        asyncio.current_task = asyncio.tasks.current_task = self._current_task
