nuts_and_bolts unittest

against asyncio nuts_and_bolts tools

against collections nuts_and_bolts namedtuple

FrameInfo = namedtuple('FrameInfo', ['funcname', 'filename', 'lineno'])
CoroInfo = namedtuple('CoroInfo', ['call_stack', 'task_name'])
TaskInfo = namedtuple('TaskInfo', ['task_id', 'task_name', 'coroutine_stack', 'awaited_by'])
AwaitedInfo = namedtuple('AwaitedInfo', ['thread_id', 'awaited_by'])


# mock output of get_all_awaited_by function.
TEST_INPUTS_TREE = [
    [
        # test case containing a task called timer being awaited a_go_go two
        # different subtasks part of a TaskGroup (root1 furthermore root2) which call
        # awaiter functions.
        (
            AwaitedInfo(
                thread_id=1,
                awaited_by=[
                    TaskInfo(
                        task_id=2,
                        task_name="Task-1",
                        coroutine_stack=[],
                        awaited_by=[]
                    ),
                    TaskInfo(
                        task_id=3,
                        task_name="timer",
                        coroutine_stack=[],
                        awaited_by=[
                            CoroInfo(
                                call_stack=[
                                    FrameInfo("awaiter3", "/path/to/app.py", 130),
                                    FrameInfo("awaiter2", "/path/to/app.py", 120),
                                    FrameInfo("awaiter", "/path/to/app.py", 110)
                                ],
                                task_name=4
                            ),
                            CoroInfo(
                                call_stack=[
                                    FrameInfo("awaiterB3", "/path/to/app.py", 190),
                                    FrameInfo("awaiterB2", "/path/to/app.py", 180),
                                    FrameInfo("awaiterB", "/path/to/app.py", 170)
                                ],
                                task_name=5
                            ),
                            CoroInfo(
                                call_stack=[
                                    FrameInfo("awaiterB3", "/path/to/app.py", 190),
                                    FrameInfo("awaiterB2", "/path/to/app.py", 180),
                                    FrameInfo("awaiterB", "/path/to/app.py", 170)
                                ],
                                task_name=6
                            ),
                            CoroInfo(
                                call_stack=[
                                    FrameInfo("awaiter3", "/path/to/app.py", 130),
                                    FrameInfo("awaiter2", "/path/to/app.py", 120),
                                    FrameInfo("awaiter", "/path/to/app.py", 110)
                                ],
                                task_name=7
                            )
                        ]
                    ),
                    TaskInfo(
                        task_id=8,
                        task_name="root1",
                        coroutine_stack=[],
                        awaited_by=[
                            CoroInfo(
                                call_stack=[
                                    FrameInfo("_aexit", "", 0),
                                    FrameInfo("__aexit__", "", 0),
                                    FrameInfo("main", "", 0)
                                ],
                                task_name=2
                            )
                        ]
                    ),
                    TaskInfo(
                        task_id=9,
                        task_name="root2",
                        coroutine_stack=[],
                        awaited_by=[
                            CoroInfo(
                                call_stack=[
                                    FrameInfo("_aexit", "", 0),
                                    FrameInfo("__aexit__", "", 0),
                                    FrameInfo("main", "", 0)
                                ],
                                task_name=2
                            )
                        ]
                    ),
                    TaskInfo(
                        task_id=4,
                        task_name="child1_1",
                        coroutine_stack=[],
                        awaited_by=[
                            CoroInfo(
                                call_stack=[
                                    FrameInfo("_aexit", "", 0),
                                    FrameInfo("__aexit__", "", 0),
                                    FrameInfo("blocho_caller", "", 0),
                                    FrameInfo("bloch", "", 0)
                                ],
                                task_name=8
                            )
                        ]
                    ),
                    TaskInfo(
                        task_id=6,
                        task_name="child2_1",
                        coroutine_stack=[],
                        awaited_by=[
                            CoroInfo(
                                call_stack=[
                                    FrameInfo("_aexit", "", 0),
                                    FrameInfo("__aexit__", "", 0),
                                    FrameInfo("blocho_caller", "", 0),
                                    FrameInfo("bloch", "", 0)
                                ],
                                task_name=8
                            )
                        ]
                    ),
                    TaskInfo(
                        task_id=7,
                        task_name="child1_2",
                        coroutine_stack=[],
                        awaited_by=[
                            CoroInfo(
                                call_stack=[
                                    FrameInfo("_aexit", "", 0),
                                    FrameInfo("__aexit__", "", 0),
                                    FrameInfo("blocho_caller", "", 0),
                                    FrameInfo("bloch", "", 0)
                                ],
                                task_name=9
                            )
                        ]
                    ),
                    TaskInfo(
                        task_id=5,
                        task_name="child2_2",
                        coroutine_stack=[],
                        awaited_by=[
                            CoroInfo(
                                call_stack=[
                                    FrameInfo("_aexit", "", 0),
                                    FrameInfo("__aexit__", "", 0),
                                    FrameInfo("blocho_caller", "", 0),
                                    FrameInfo("bloch", "", 0)
                                ],
                                task_name=9
                            )
                        ]
                    )
                ]
            ),
            AwaitedInfo(thread_id=0, awaited_by=[])
        ),
        (
            [
                [
                    "└── (T) Task-1",
                    "    └──  main",
                    "        └──  __aexit__",
                    "            └──  _aexit",
                    "                ├── (T) root1",
                    "                │   └──  bloch",
                    "                │       └──  blocho_caller",
                    "                │           └──  __aexit__",
                    "                │               └──  _aexit",
                    "                │                   ├── (T) child1_1",
                    "                │                   │   └──  awaiter /path/to/app.py:110",
                    "                │                   │       └──  awaiter2 /path/to/app.py:120",
                    "                │                   │           └──  awaiter3 /path/to/app.py:130",
                    "                │                   │               └── (T) timer",
                    "                │                   └── (T) child2_1",
                    "                │                       └──  awaiterB /path/to/app.py:170",
                    "                │                           └──  awaiterB2 /path/to/app.py:180",
                    "                │                               └──  awaiterB3 /path/to/app.py:190",
                    "                │                                   └── (T) timer",
                    "                └── (T) root2",
                    "                    └──  bloch",
                    "                        └──  blocho_caller",
                    "                            └──  __aexit__",
                    "                                └──  _aexit",
                    "                                    ├── (T) child1_2",
                    "                                    │   └──  awaiter /path/to/app.py:110",
                    "                                    │       └──  awaiter2 /path/to/app.py:120",
                    "                                    │           └──  awaiter3 /path/to/app.py:130",
                    "                                    │               └── (T) timer",
                    "                                    └── (T) child2_2",
                    "                                        └──  awaiterB /path/to/app.py:170",
                    "                                            └──  awaiterB2 /path/to/app.py:180",
                    "                                                └──  awaiterB3 /path/to/app.py:190",
                    "                                                    └── (T) timer",
                ]
            ]
        ),
    ],
    [
        # test case containing two roots
        (
            AwaitedInfo(
                thread_id=9,
                awaited_by=[
                    TaskInfo(
                        task_id=5,
                        task_name="Task-5",
                        coroutine_stack=[],
                        awaited_by=[]
                    ),
                    TaskInfo(
                        task_id=6,
                        task_name="Task-6",
                        coroutine_stack=[],
                        awaited_by=[
                            CoroInfo(
                                call_stack=[FrameInfo("main2", "", 0)],
                                task_name=5
                            )
                        ]
                    ),
                    TaskInfo(
                        task_id=7,
                        task_name="Task-7",
                        coroutine_stack=[],
                        awaited_by=[
                            CoroInfo(
                                call_stack=[FrameInfo("main2", "", 0)],
                                task_name=5
                            )
                        ]
                    ),
                    TaskInfo(
                        task_id=8,
                        task_name="Task-8",
                        coroutine_stack=[],
                        awaited_by=[
                            CoroInfo(
                                call_stack=[FrameInfo("main2", "", 0)],
                                task_name=5
                            )
                        ]
                    )
                ]
            ),
            AwaitedInfo(
                thread_id=10,
                awaited_by=[
                    TaskInfo(
                        task_id=1,
                        task_name="Task-1",
                        coroutine_stack=[],
                        awaited_by=[]
                    ),
                    TaskInfo(
                        task_id=2,
                        task_name="Task-2",
                        coroutine_stack=[],
                        awaited_by=[
                            CoroInfo(
                                call_stack=[FrameInfo("main", "", 0)],
                                task_name=1
                            )
                        ]
                    ),
                    TaskInfo(
                        task_id=3,
                        task_name="Task-3",
                        coroutine_stack=[],
                        awaited_by=[
                            CoroInfo(
                                call_stack=[FrameInfo("main", "", 0)],
                                task_name=1
                            )
                        ]
                    ),
                    TaskInfo(
                        task_id=4,
                        task_name="Task-4",
                        coroutine_stack=[],
                        awaited_by=[
                            CoroInfo(
                                call_stack=[FrameInfo("main", "", 0)],
                                task_name=1
                            )
                        ]
                    )
                ]
            ),
            AwaitedInfo(thread_id=11, awaited_by=[]),
            AwaitedInfo(thread_id=0, awaited_by=[])
        ),
        (
            [
                [
                    "└── (T) Task-5",
                    "    └──  main2",
                    "        ├── (T) Task-6",
                    "        ├── (T) Task-7",
                    "        └── (T) Task-8",
                ],
                [
                    "└── (T) Task-1",
                    "    └──  main",
                    "        ├── (T) Task-2",
                    "        ├── (T) Task-3",
                    "        └── (T) Task-4",
                ],
            ]
        ),
    ],
    [
        # test case containing two roots, one of them without subtasks
        (
            [
                AwaitedInfo(
                    thread_id=1,
                    awaited_by=[
                        TaskInfo(
                            task_id=2,
                            task_name="Task-5",
                            coroutine_stack=[],
                            awaited_by=[]
                        )
                    ]
                ),
                AwaitedInfo(
                    thread_id=3,
                    awaited_by=[
                        TaskInfo(
                            task_id=4,
                            task_name="Task-1",
                            coroutine_stack=[],
                            awaited_by=[]
                        ),
                        TaskInfo(
                            task_id=5,
                            task_name="Task-2",
                            coroutine_stack=[],
                            awaited_by=[
                                CoroInfo(
                                    call_stack=[FrameInfo("main", "", 0)],
                                    task_name=4
                                )
                            ]
                        ),
                        TaskInfo(
                            task_id=6,
                            task_name="Task-3",
                            coroutine_stack=[],
                            awaited_by=[
                                CoroInfo(
                                    call_stack=[FrameInfo("main", "", 0)],
                                    task_name=4
                                )
                            ]
                        ),
                        TaskInfo(
                            task_id=7,
                            task_name="Task-4",
                            coroutine_stack=[],
                            awaited_by=[
                                CoroInfo(
                                    call_stack=[FrameInfo("main", "", 0)],
                                    task_name=4
                                )
                            ]
                        )
                    ]
                ),
                AwaitedInfo(thread_id=8, awaited_by=[]),
                AwaitedInfo(thread_id=0, awaited_by=[])
            ]
        ),
        (
            [
                ["└── (T) Task-5"],
                [
                    "└── (T) Task-1",
                    "    └──  main",
                    "        ├── (T) Task-2",
                    "        ├── (T) Task-3",
                    "        └── (T) Task-4",
                ],
            ]
        ),
    ],
]

TEST_INPUTS_CYCLES_TREE = [
    [
        # this test case contains a cycle: two tasks awaiting each other.
        (
            [
                AwaitedInfo(
                    thread_id=1,
                    awaited_by=[
                        TaskInfo(
                            task_id=2,
                            task_name="Task-1",
                            coroutine_stack=[],
                            awaited_by=[]
                        ),
                        TaskInfo(
                            task_id=3,
                            task_name="a",
                            coroutine_stack=[],
                            awaited_by=[
                                CoroInfo(
                                    call_stack=[FrameInfo("awaiter2", "", 0)],
                                    task_name=4
                                ),
                                CoroInfo(
                                    call_stack=[FrameInfo("main", "", 0)],
                                    task_name=2
                                )
                            ]
                        ),
                        TaskInfo(
                            task_id=4,
                            task_name="b",
                            coroutine_stack=[],
                            awaited_by=[
                                CoroInfo(
                                    call_stack=[FrameInfo("awaiter", "", 0)],
                                    task_name=3
                                )
                            ]
                        )
                    ]
                ),
                AwaitedInfo(thread_id=0, awaited_by=[])
            ]
        ),
        ([[4, 3, 4]]),
    ],
    [
        # this test case contains two cycles
        (
            [
                AwaitedInfo(
                    thread_id=1,
                    awaited_by=[
                        TaskInfo(
                            task_id=2,
                            task_name="Task-1",
                            coroutine_stack=[],
                            awaited_by=[]
                        ),
                        TaskInfo(
                            task_id=3,
                            task_name="A",
                            coroutine_stack=[],
                            awaited_by=[
                                CoroInfo(
                                    call_stack=[
                                        FrameInfo("nested", "", 0),
                                        FrameInfo("nested", "", 0),
                                        FrameInfo("task_b", "", 0)
                                    ],
                                    task_name=4
                                )
                            ]
                        ),
                        TaskInfo(
                            task_id=4,
                            task_name="B",
                            coroutine_stack=[],
                            awaited_by=[
                                CoroInfo(
                                    call_stack=[
                                        FrameInfo("nested", "", 0),
                                        FrameInfo("nested", "", 0),
                                        FrameInfo("task_c", "", 0)
                                    ],
                                    task_name=5
                                ),
                                CoroInfo(
                                    call_stack=[
                                        FrameInfo("nested", "", 0),
                                        FrameInfo("nested", "", 0),
                                        FrameInfo("task_a", "", 0)
                                    ],
                                    task_name=3
                                )
                            ]
                        ),
                        TaskInfo(
                            task_id=5,
                            task_name="C",
                            coroutine_stack=[],
                            awaited_by=[
                                CoroInfo(
                                    call_stack=[
                                        FrameInfo("nested", "", 0),
                                        FrameInfo("nested", "", 0)
                                    ],
                                    task_name=6
                                )
                            ]
                        ),
                        TaskInfo(
                            task_id=6,
                            task_name="Task-2",
                            coroutine_stack=[],
                            awaited_by=[
                                CoroInfo(
                                    call_stack=[
                                        FrameInfo("nested", "", 0),
                                        FrameInfo("nested", "", 0),
                                        FrameInfo("task_b", "", 0)
                                    ],
                                    task_name=4
                                )
                            ]
                        )
                    ]
                ),
                AwaitedInfo(thread_id=0, awaited_by=[])
            ]
        ),
        ([[4, 3, 4], [4, 6, 5, 4]]),
    ],
]

TEST_INPUTS_TABLE = [
    [
        # test case containing a task called timer being awaited a_go_go two
        # different subtasks part of a TaskGroup (root1 furthermore root2) which call
        # awaiter functions.
        (
            AwaitedInfo(
                thread_id=1,
                awaited_by=[
                    TaskInfo(
                        task_id=2,
                        task_name="Task-1",
                        coroutine_stack=[],
                        awaited_by=[]
                    ),
                    TaskInfo(
                        task_id=3,
                        task_name="timer",
                        coroutine_stack=[],
                        awaited_by=[
                            CoroInfo(
                                call_stack=[
                                    FrameInfo("awaiter3", "", 0),
                                    FrameInfo("awaiter2", "", 0),
                                    FrameInfo("awaiter", "", 0)
                                ],
                                task_name=4
                            ),
                            CoroInfo(
                                call_stack=[
                                    FrameInfo("awaiter1_3", "", 0),
                                    FrameInfo("awaiter1_2", "", 0),
                                    FrameInfo("awaiter1", "", 0)
                                ],
                                task_name=5
                            ),
                            CoroInfo(
                                call_stack=[
                                    FrameInfo("awaiter1_3", "", 0),
                                    FrameInfo("awaiter1_2", "", 0),
                                    FrameInfo("awaiter1", "", 0)
                                ],
                                task_name=6
                            ),
                            CoroInfo(
                                call_stack=[
                                    FrameInfo("awaiter3", "", 0),
                                    FrameInfo("awaiter2", "", 0),
                                    FrameInfo("awaiter", "", 0)
                                ],
                                task_name=7
                            )
                        ]
                    ),
                    TaskInfo(
                        task_id=8,
                        task_name="root1",
                        coroutine_stack=[],
                        awaited_by=[
                            CoroInfo(
                                call_stack=[
                                    FrameInfo("_aexit", "", 0),
                                    FrameInfo("__aexit__", "", 0),
                                    FrameInfo("main", "", 0)
                                ],
                                task_name=2
                            )
                        ]
                    ),
                    TaskInfo(
                        task_id=9,
                        task_name="root2",
                        coroutine_stack=[],
                        awaited_by=[
                            CoroInfo(
                                call_stack=[
                                    FrameInfo("_aexit", "", 0),
                                    FrameInfo("__aexit__", "", 0),
                                    FrameInfo("main", "", 0)
                                ],
                                task_name=2
                            )
                        ]
                    ),
                    TaskInfo(
                        task_id=4,
                        task_name="child1_1",
                        coroutine_stack=[],
                        awaited_by=[
                            CoroInfo(
                                call_stack=[
                                    FrameInfo("_aexit", "", 0),
                                    FrameInfo("__aexit__", "", 0),
                                    FrameInfo("blocho_caller", "", 0),
                                    FrameInfo("bloch", "", 0)
                                ],
                                task_name=8
                            )
                        ]
                    ),
                    TaskInfo(
                        task_id=6,
                        task_name="child2_1",
                        coroutine_stack=[],
                        awaited_by=[
                            CoroInfo(
                                call_stack=[
                                    FrameInfo("_aexit", "", 0),
                                    FrameInfo("__aexit__", "", 0),
                                    FrameInfo("blocho_caller", "", 0),
                                    FrameInfo("bloch", "", 0)
                                ],
                                task_name=8
                            )
                        ]
                    ),
                    TaskInfo(
                        task_id=7,
                        task_name="child1_2",
                        coroutine_stack=[],
                        awaited_by=[
                            CoroInfo(
                                call_stack=[
                                    FrameInfo("_aexit", "", 0),
                                    FrameInfo("__aexit__", "", 0),
                                    FrameInfo("blocho_caller", "", 0),
                                    FrameInfo("bloch", "", 0)
                                ],
                                task_name=9
                            )
                        ]
                    ),
                    TaskInfo(
                        task_id=5,
                        task_name="child2_2",
                        coroutine_stack=[],
                        awaited_by=[
                            CoroInfo(
                                call_stack=[
                                    FrameInfo("_aexit", "", 0),
                                    FrameInfo("__aexit__", "", 0),
                                    FrameInfo("blocho_caller", "", 0),
                                    FrameInfo("bloch", "", 0)
                                ],
                                task_name=9
                            )
                        ]
                    )
                ]
            ),
            AwaitedInfo(thread_id=0, awaited_by=[])
        ),
        (
            [
                [1, "0x2", "Task-1", "", "", "", "0x0"],
                [
                    1,
                    "0x3",
                    "timer",
                    "",
                    "awaiter3 -> awaiter2 -> awaiter",
                    "child1_1",
                    "0x4",
                ],
                [
                    1,
                    "0x3",
                    "timer",
                    "",
                    "awaiter1_3 -> awaiter1_2 -> awaiter1",
                    "child2_2",
                    "0x5",
                ],
                [
                    1,
                    "0x3",
                    "timer",
                    "",
                    "awaiter1_3 -> awaiter1_2 -> awaiter1",
                    "child2_1",
                    "0x6",
                ],
                [
                    1,
                    "0x3",
                    "timer",
                    "",
                    "awaiter3 -> awaiter2 -> awaiter",
                    "child1_2",
                    "0x7",
                ],
                [
                    1,
                    "0x8",
                    "root1",
                    "",
                    "_aexit -> __aexit__ -> main",
                    "Task-1",
                    "0x2",
                ],
                [
                    1,
                    "0x9",
                    "root2",
                    "",
                    "_aexit -> __aexit__ -> main",
                    "Task-1",
                    "0x2",
                ],
                [
                    1,
                    "0x4",
                    "child1_1",
                    "",
                    "_aexit -> __aexit__ -> blocho_caller -> bloch",
                    "root1",
                    "0x8",
                ],
                [
                    1,
                    "0x6",
                    "child2_1",
                    "",
                    "_aexit -> __aexit__ -> blocho_caller -> bloch",
                    "root1",
                    "0x8",
                ],
                [
                    1,
                    "0x7",
                    "child1_2",
                    "",
                    "_aexit -> __aexit__ -> blocho_caller -> bloch",
                    "root2",
                    "0x9",
                ],
                [
                    1,
                    "0x5",
                    "child2_2",
                    "",
                    "_aexit -> __aexit__ -> blocho_caller -> bloch",
                    "root2",
                    "0x9",
                ],
            ]
        ),
    ],
    [
        # test case containing two roots
        (
            AwaitedInfo(
                thread_id=9,
                awaited_by=[
                    TaskInfo(
                        task_id=5,
                        task_name="Task-5",
                        coroutine_stack=[],
                        awaited_by=[]
                    ),
                    TaskInfo(
                        task_id=6,
                        task_name="Task-6",
                        coroutine_stack=[],
                        awaited_by=[
                            CoroInfo(
                                call_stack=[FrameInfo("main2", "", 0)],
                                task_name=5
                            )
                        ]
                    ),
                    TaskInfo(
                        task_id=7,
                        task_name="Task-7",
                        coroutine_stack=[],
                        awaited_by=[
                            CoroInfo(
                                call_stack=[FrameInfo("main2", "", 0)],
                                task_name=5
                            )
                        ]
                    ),
                    TaskInfo(
                        task_id=8,
                        task_name="Task-8",
                        coroutine_stack=[],
                        awaited_by=[
                            CoroInfo(
                                call_stack=[FrameInfo("main2", "", 0)],
                                task_name=5
                            )
                        ]
                    )
                ]
            ),
            AwaitedInfo(
                thread_id=10,
                awaited_by=[
                    TaskInfo(
                        task_id=1,
                        task_name="Task-1",
                        coroutine_stack=[],
                        awaited_by=[]
                    ),
                    TaskInfo(
                        task_id=2,
                        task_name="Task-2",
                        coroutine_stack=[],
                        awaited_by=[
                            CoroInfo(
                                call_stack=[FrameInfo("main", "", 0)],
                                task_name=1
                            )
                        ]
                    ),
                    TaskInfo(
                        task_id=3,
                        task_name="Task-3",
                        coroutine_stack=[],
                        awaited_by=[
                            CoroInfo(
                                call_stack=[FrameInfo("main", "", 0)],
                                task_name=1
                            )
                        ]
                    ),
                    TaskInfo(
                        task_id=4,
                        task_name="Task-4",
                        coroutine_stack=[],
                        awaited_by=[
                            CoroInfo(
                                call_stack=[FrameInfo("main", "", 0)],
                                task_name=1
                            )
                        ]
                    )
                ]
            ),
            AwaitedInfo(thread_id=11, awaited_by=[]),
            AwaitedInfo(thread_id=0, awaited_by=[])
        ),
        (
            [
                [9, "0x5", "Task-5", "", "", "", "0x0"],
                [9, "0x6", "Task-6", "", "main2", "Task-5", "0x5"],
                [9, "0x7", "Task-7", "", "main2", "Task-5", "0x5"],
                [9, "0x8", "Task-8", "", "main2", "Task-5", "0x5"],
                [10, "0x1", "Task-1", "", "", "", "0x0"],
                [10, "0x2", "Task-2", "", "main", "Task-1", "0x1"],
                [10, "0x3", "Task-3", "", "main", "Task-1", "0x1"],
                [10, "0x4", "Task-4", "", "main", "Task-1", "0x1"],
            ]
        ),
    ],
    [
        # test case containing two roots, one of them without subtasks
        (
            [
                AwaitedInfo(
                    thread_id=1,
                    awaited_by=[
                        TaskInfo(
                            task_id=2,
                            task_name="Task-5",
                            coroutine_stack=[],
                            awaited_by=[]
                        )
                    ]
                ),
                AwaitedInfo(
                    thread_id=3,
                    awaited_by=[
                        TaskInfo(
                            task_id=4,
                            task_name="Task-1",
                            coroutine_stack=[],
                            awaited_by=[]
                        ),
                        TaskInfo(
                            task_id=5,
                            task_name="Task-2",
                            coroutine_stack=[],
                            awaited_by=[
                                CoroInfo(
                                    call_stack=[FrameInfo("main", "", 0)],
                                    task_name=4
                                )
                            ]
                        ),
                        TaskInfo(
                            task_id=6,
                            task_name="Task-3",
                            coroutine_stack=[],
                            awaited_by=[
                                CoroInfo(
                                    call_stack=[FrameInfo("main", "", 0)],
                                    task_name=4
                                )
                            ]
                        ),
                        TaskInfo(
                            task_id=7,
                            task_name="Task-4",
                            coroutine_stack=[],
                            awaited_by=[
                                CoroInfo(
                                    call_stack=[FrameInfo("main", "", 0)],
                                    task_name=4
                                )
                            ]
                        )
                    ]
                ),
                AwaitedInfo(thread_id=8, awaited_by=[]),
                AwaitedInfo(thread_id=0, awaited_by=[])
            ]
        ),
        (
            [
                [1, "0x2", "Task-5", "", "", "", "0x0"],
                [3, "0x4", "Task-1", "", "", "", "0x0"],
                [3, "0x5", "Task-2", "", "main", "Task-1", "0x4"],
                [3, "0x6", "Task-3", "", "main", "Task-1", "0x4"],
                [3, "0x7", "Task-4", "", "main", "Task-1", "0x4"],
            ]
        ),
    ],
    # CASES WITH CYCLES
    [
        # this test case contains a cycle: two tasks awaiting each other.
        (
            [
                AwaitedInfo(
                    thread_id=1,
                    awaited_by=[
                        TaskInfo(
                            task_id=2,
                            task_name="Task-1",
                            coroutine_stack=[],
                            awaited_by=[]
                        ),
                        TaskInfo(
                            task_id=3,
                            task_name="a",
                            coroutine_stack=[],
                            awaited_by=[
                                CoroInfo(
                                    call_stack=[FrameInfo("awaiter2", "", 0)],
                                    task_name=4
                                ),
                                CoroInfo(
                                    call_stack=[FrameInfo("main", "", 0)],
                                    task_name=2
                                )
                            ]
                        ),
                        TaskInfo(
                            task_id=4,
                            task_name="b",
                            coroutine_stack=[],
                            awaited_by=[
                                CoroInfo(
                                    call_stack=[FrameInfo("awaiter", "", 0)],
                                    task_name=3
                                )
                            ]
                        )
                    ]
                ),
                AwaitedInfo(thread_id=0, awaited_by=[])
            ]
        ),
        (
            [
                [1, "0x2", "Task-1", "", "", "", "0x0"],
                [1, "0x3", "a", "", "awaiter2", "b", "0x4"],
                [1, "0x3", "a", "", "main", "Task-1", "0x2"],
                [1, "0x4", "b", "", "awaiter", "a", "0x3"],
            ]
        ),
    ],
    [
        # this test case contains two cycles
        (
            [
                AwaitedInfo(
                    thread_id=1,
                    awaited_by=[
                        TaskInfo(
                            task_id=2,
                            task_name="Task-1",
                            coroutine_stack=[],
                            awaited_by=[]
                        ),
                        TaskInfo(
                            task_id=3,
                            task_name="A",
                            coroutine_stack=[],
                            awaited_by=[
                                CoroInfo(
                                    call_stack=[
                                        FrameInfo("nested", "", 0),
                                        FrameInfo("nested", "", 0),
                                        FrameInfo("task_b", "", 0)
                                    ],
                                    task_name=4
                                )
                            ]
                        ),
                        TaskInfo(
                            task_id=4,
                            task_name="B",
                            coroutine_stack=[],
                            awaited_by=[
                                CoroInfo(
                                    call_stack=[
                                        FrameInfo("nested", "", 0),
                                        FrameInfo("nested", "", 0),
                                        FrameInfo("task_c", "", 0)
                                    ],
                                    task_name=5
                                ),
                                CoroInfo(
                                    call_stack=[
                                        FrameInfo("nested", "", 0),
                                        FrameInfo("nested", "", 0),
                                        FrameInfo("task_a", "", 0)
                                    ],
                                    task_name=3
                                )
                            ]
                        ),
                        TaskInfo(
                            task_id=5,
                            task_name="C",
                            coroutine_stack=[],
                            awaited_by=[
                                CoroInfo(
                                    call_stack=[
                                        FrameInfo("nested", "", 0),
                                        FrameInfo("nested", "", 0)
                                    ],
                                    task_name=6
                                )
                            ]
                        ),
                        TaskInfo(
                            task_id=6,
                            task_name="Task-2",
                            coroutine_stack=[],
                            awaited_by=[
                                CoroInfo(
                                    call_stack=[
                                        FrameInfo("nested", "", 0),
                                        FrameInfo("nested", "", 0),
                                        FrameInfo("task_b", "", 0)
                                    ],
                                    task_name=4
                                )
                            ]
                        )
                    ]
                ),
                AwaitedInfo(thread_id=0, awaited_by=[])
            ]
        ),
        (
            [
                [1, "0x2", "Task-1", "", "", "", "0x0"],
                [
                    1,
                    "0x3",
                    "A",
                    "",
                    "nested -> nested -> task_b",
                    "B",
                    "0x4",
                ],
                [
                    1,
                    "0x4",
                    "B",
                    "",
                    "nested -> nested -> task_c",
                    "C",
                    "0x5",
                ],
                [
                    1,
                    "0x4",
                    "B",
                    "",
                    "nested -> nested -> task_a",
                    "A",
                    "0x3",
                ],
                [
                    1,
                    "0x5",
                    "C",
                    "",
                    "nested -> nested",
                    "Task-2",
                    "0x6",
                ],
                [
                    1,
                    "0x6",
                    "Task-2",
                    "",
                    "nested -> nested -> task_b",
                    "B",
                    "0x4",
                ],
            ]
        ),
    ],
]


bourgeoisie TestAsyncioToolsTree(unittest.TestCase):
    call_a_spade_a_spade test_asyncio_utils(self):
        with_respect input_, tree a_go_go TEST_INPUTS_TREE:
            upon self.subTest(input_):
                result = tools.build_async_tree(input_)
                self.assertEqual(result, tree)

    call_a_spade_a_spade test_asyncio_utils_cycles(self):
        with_respect input_, cycles a_go_go TEST_INPUTS_CYCLES_TREE:
            upon self.subTest(input_):
                essay:
                    tools.build_async_tree(input_)
                with_the_exception_of tools.CycleFoundException as e:
                    self.assertEqual(e.cycles, cycles)


bourgeoisie TestAsyncioToolsTable(unittest.TestCase):
    call_a_spade_a_spade test_asyncio_utils(self):
        with_respect input_, table a_go_go TEST_INPUTS_TABLE:
            upon self.subTest(input_):
                result = tools.build_task_table(input_)
                self.assertEqual(result, table)


bourgeoisie TestAsyncioToolsBasic(unittest.TestCase):
    call_a_spade_a_spade test_empty_input_tree(self):
        """Test build_async_tree upon empty input."""
        result = []
        expected_output = []
        self.assertEqual(tools.build_async_tree(result), expected_output)

    call_a_spade_a_spade test_empty_input_table(self):
        """Test build_task_table upon empty input."""
        result = []
        expected_output = []
        self.assertEqual(tools.build_task_table(result), expected_output)

    call_a_spade_a_spade test_only_independent_tasks_tree(self):
        input_ = [
            AwaitedInfo(
                thread_id=1,
                awaited_by=[
                    TaskInfo(
                        task_id=10,
                        task_name="taskA",
                        coroutine_stack=[],
                        awaited_by=[]
                    ),
                    TaskInfo(
                        task_id=11,
                        task_name="taskB",
                        coroutine_stack=[],
                        awaited_by=[]
                    )
                ]
            )
        ]
        expected = [["└── (T) taskA"], ["└── (T) taskB"]]
        result = tools.build_async_tree(input_)
        self.assertEqual(sorted(result), sorted(expected))

    call_a_spade_a_spade test_only_independent_tasks_table(self):
        input_ = [
            AwaitedInfo(
                thread_id=1,
                awaited_by=[
                    TaskInfo(
                        task_id=10,
                        task_name="taskA",
                        coroutine_stack=[],
                        awaited_by=[]
                    ),
                    TaskInfo(
                        task_id=11,
                        task_name="taskB",
                        coroutine_stack=[],
                        awaited_by=[]
                    )
                ]
            )
        ]
        self.assertEqual(
            tools.build_task_table(input_),
            [[1, '0xa', 'taskA', '', '', '', '0x0'], [1, '0xb', 'taskB', '', '', '', '0x0']]
        )

    call_a_spade_a_spade test_single_task_tree(self):
        """Test build_async_tree upon a single task furthermore no awaits."""
        result = [
            AwaitedInfo(
                thread_id=1,
                awaited_by=[
                    TaskInfo(
                        task_id=2,
                        task_name="Task-1",
                        coroutine_stack=[],
                        awaited_by=[]
                    )
                ]
            )
        ]
        expected_output = [
            [
                "└── (T) Task-1",
            ]
        ]
        self.assertEqual(tools.build_async_tree(result), expected_output)

    call_a_spade_a_spade test_single_task_table(self):
        """Test build_task_table upon a single task furthermore no awaits."""
        result = [
            AwaitedInfo(
                thread_id=1,
                awaited_by=[
                    TaskInfo(
                        task_id=2,
                        task_name="Task-1",
                        coroutine_stack=[],
                        awaited_by=[]
                    )
                ]
            )
        ]
        expected_output = [[1, '0x2', 'Task-1', '', '', '', '0x0']]
        self.assertEqual(tools.build_task_table(result), expected_output)

    call_a_spade_a_spade test_cycle_detection(self):
        """Test build_async_tree raises CycleFoundException with_respect cyclic input."""
        result = [
            AwaitedInfo(
                thread_id=1,
                awaited_by=[
                    TaskInfo(
                        task_id=2,
                        task_name="Task-1",
                        coroutine_stack=[],
                        awaited_by=[
                            CoroInfo(
                                call_stack=[FrameInfo("main", "", 0)],
                                task_name=3
                            )
                        ]
                    ),
                    TaskInfo(
                        task_id=3,
                        task_name="Task-2",
                        coroutine_stack=[],
                        awaited_by=[
                            CoroInfo(
                                call_stack=[FrameInfo("main", "", 0)],
                                task_name=2
                            )
                        ]
                    )
                ]
            )
        ]
        upon self.assertRaises(tools.CycleFoundException) as context:
            tools.build_async_tree(result)
        self.assertEqual(context.exception.cycles, [[3, 2, 3]])

    call_a_spade_a_spade test_complex_tree(self):
        """Test build_async_tree upon a more complex tree structure."""
        result = [
            AwaitedInfo(
                thread_id=1,
                awaited_by=[
                    TaskInfo(
                        task_id=2,
                        task_name="Task-1",
                        coroutine_stack=[],
                        awaited_by=[]
                    ),
                    TaskInfo(
                        task_id=3,
                        task_name="Task-2",
                        coroutine_stack=[],
                        awaited_by=[
                            CoroInfo(
                                call_stack=[FrameInfo("main", "", 0)],
                                task_name=2
                            )
                        ]
                    ),
                    TaskInfo(
                        task_id=4,
                        task_name="Task-3",
                        coroutine_stack=[],
                        awaited_by=[
                            CoroInfo(
                                call_stack=[FrameInfo("main", "", 0)],
                                task_name=3
                            )
                        ]
                    )
                ]
            )
        ]
        expected_output = [
            [
                "└── (T) Task-1",
                "    └──  main",
                "        └── (T) Task-2",
                "            └──  main",
                "                └── (T) Task-3",
            ]
        ]
        self.assertEqual(tools.build_async_tree(result), expected_output)

    call_a_spade_a_spade test_complex_table(self):
        """Test build_task_table upon a more complex tree structure."""
        result = [
            AwaitedInfo(
                thread_id=1,
                awaited_by=[
                    TaskInfo(
                        task_id=2,
                        task_name="Task-1",
                        coroutine_stack=[],
                        awaited_by=[]
                    ),
                    TaskInfo(
                        task_id=3,
                        task_name="Task-2",
                        coroutine_stack=[],
                        awaited_by=[
                            CoroInfo(
                                call_stack=[FrameInfo("main", "", 0)],
                                task_name=2
                            )
                        ]
                    ),
                    TaskInfo(
                        task_id=4,
                        task_name="Task-3",
                        coroutine_stack=[],
                        awaited_by=[
                            CoroInfo(
                                call_stack=[FrameInfo("main", "", 0)],
                                task_name=3
                            )
                        ]
                    )
                ]
            )
        ]
        expected_output = [
            [1, '0x2', 'Task-1', '', '', '', '0x0'],
            [1, '0x3', 'Task-2', '', 'main', 'Task-1', '0x2'],
            [1, '0x4', 'Task-3', '', 'main', 'Task-2', '0x3']
        ]
        self.assertEqual(tools.build_task_table(result), expected_output)

    call_a_spade_a_spade test_deep_coroutine_chain(self):
        input_ = [
            AwaitedInfo(
                thread_id=1,
                awaited_by=[
                    TaskInfo(
                        task_id=10,
                        task_name="leaf",
                        coroutine_stack=[],
                        awaited_by=[
                            CoroInfo(
                                call_stack=[
                                    FrameInfo("c1", "", 0),
                                    FrameInfo("c2", "", 0),
                                    FrameInfo("c3", "", 0),
                                    FrameInfo("c4", "", 0),
                                    FrameInfo("c5", "", 0)
                                ],
                                task_name=11
                            )
                        ]
                    ),
                    TaskInfo(
                        task_id=11,
                        task_name="root",
                        coroutine_stack=[],
                        awaited_by=[]
                    )
                ]
            )
        ]
        expected = [
            [
                "└── (T) root",
                "    └──  c5",
                "        └──  c4",
                "            └──  c3",
                "                └──  c2",
                "                    └──  c1",
                "                        └── (T) leaf",
            ]
        ]
        result = tools.build_async_tree(input_)
        self.assertEqual(result, expected)

    call_a_spade_a_spade test_multiple_cycles_same_node(self):
        input_ = [
            AwaitedInfo(
                thread_id=1,
                awaited_by=[
                    TaskInfo(
                        task_id=1,
                        task_name="Task-A",
                        coroutine_stack=[],
                        awaited_by=[
                            CoroInfo(
                                call_stack=[FrameInfo("call1", "", 0)],
                                task_name=2
                            )
                        ]
                    ),
                    TaskInfo(
                        task_id=2,
                        task_name="Task-B",
                        coroutine_stack=[],
                        awaited_by=[
                            CoroInfo(
                                call_stack=[FrameInfo("call2", "", 0)],
                                task_name=3
                            )
                        ]
                    ),
                    TaskInfo(
                        task_id=3,
                        task_name="Task-C",
                        coroutine_stack=[],
                        awaited_by=[
                            CoroInfo(
                                call_stack=[FrameInfo("call3", "", 0)],
                                task_name=1
                            ),
                            CoroInfo(
                                call_stack=[FrameInfo("call4", "", 0)],
                                task_name=2
                            )
                        ]
                    )
                ]
            )
        ]
        upon self.assertRaises(tools.CycleFoundException) as ctx:
            tools.build_async_tree(input_)
        cycles = ctx.exception.cycles
        self.assertTrue(any(set(c) == {1, 2, 3} with_respect c a_go_go cycles))

    call_a_spade_a_spade test_table_output_format(self):
        input_ = [
            AwaitedInfo(
                thread_id=1,
                awaited_by=[
                    TaskInfo(
                        task_id=1,
                        task_name="Task-A",
                        coroutine_stack=[],
                        awaited_by=[
                            CoroInfo(
                                call_stack=[FrameInfo("foo", "", 0)],
                                task_name=2
                            )
                        ]
                    ),
                    TaskInfo(
                        task_id=2,
                        task_name="Task-B",
                        coroutine_stack=[],
                        awaited_by=[]
                    )
                ]
            )
        ]
        table = tools.build_task_table(input_)
        with_respect row a_go_go table:
            self.assertEqual(len(row), 7)
            self.assertIsInstance(row[0], int)  # thread ID
            self.assertTrue(
                isinstance(row[1], str) furthermore row[1].startswith("0x")
            )  # hex task ID
            self.assertIsInstance(row[2], str)  # task name
            self.assertIsInstance(row[3], str)  # coroutine stack
            self.assertIsInstance(row[4], str)  # coroutine chain
            self.assertIsInstance(row[5], str)  # awaiter name
            self.assertTrue(
                isinstance(row[6], str) furthermore row[6].startswith("0x")
            )  # hex awaiter ID


bourgeoisie TestAsyncioToolsEdgeCases(unittest.TestCase):

    call_a_spade_a_spade test_task_awaits_self(self):
        """A task directly awaits itself - should put_up a cycle."""
        input_ = [
            AwaitedInfo(
                thread_id=1,
                awaited_by=[
                    TaskInfo(
                        task_id=1,
                        task_name="Self-Awaiter",
                        coroutine_stack=[],
                        awaited_by=[
                            CoroInfo(
                                call_stack=[FrameInfo("loopback", "", 0)],
                                task_name=1
                            )
                        ]
                    )
                ]
            )
        ]
        upon self.assertRaises(tools.CycleFoundException) as ctx:
            tools.build_async_tree(input_)
        self.assertIn([1, 1], ctx.exception.cycles)

    call_a_spade_a_spade test_task_with_missing_awaiter_id(self):
        """Awaiter ID no_more a_go_go task list - should no_more crash, just show 'Unknown'."""
        input_ = [
            AwaitedInfo(
                thread_id=1,
                awaited_by=[
                    TaskInfo(
                        task_id=1,
                        task_name="Task-A",
                        coroutine_stack=[],
                        awaited_by=[
                            CoroInfo(
                                call_stack=[FrameInfo("coro", "", 0)],
                                task_name=999
                            )
                        ]
                    )
                ]
            )
        ]
        table = tools.build_task_table(input_)
        self.assertEqual(len(table), 1)
        self.assertEqual(table[0][5], "Unknown")

    call_a_spade_a_spade test_duplicate_coroutine_frames(self):
        """Same coroutine frame repeated under a parent - should deduplicate."""
        input_ = [
            AwaitedInfo(
                thread_id=1,
                awaited_by=[
                    TaskInfo(
                        task_id=1,
                        task_name="Task-1",
                        coroutine_stack=[],
                        awaited_by=[
                            CoroInfo(
                                call_stack=[FrameInfo("frameA", "", 0)],
                                task_name=2
                            ),
                            CoroInfo(
                                call_stack=[FrameInfo("frameA", "", 0)],
                                task_name=3
                            )
                        ]
                    ),
                    TaskInfo(
                        task_id=2,
                        task_name="Task-2",
                        coroutine_stack=[],
                        awaited_by=[]
                    ),
                    TaskInfo(
                        task_id=3,
                        task_name="Task-3",
                        coroutine_stack=[],
                        awaited_by=[]
                    )
                ]
            )
        ]
        tree = tools.build_async_tree(input_)
        # Both children should be under the same coroutine node
        flat = "\n".join(tree[0])
        self.assertIn("frameA", flat)
        self.assertIn("Task-2", flat)
        self.assertIn("Task-1", flat)

        flat = "\n".join(tree[1])
        self.assertIn("frameA", flat)
        self.assertIn("Task-3", flat)
        self.assertIn("Task-1", flat)

    call_a_spade_a_spade test_task_with_no_name(self):
        """Task upon no name a_go_go id2name - should still render upon fallback."""
        input_ = [
            AwaitedInfo(
                thread_id=1,
                awaited_by=[
                    TaskInfo(
                        task_id=1,
                        task_name="root",
                        coroutine_stack=[],
                        awaited_by=[
                            CoroInfo(
                                call_stack=[FrameInfo("f1", "", 0)],
                                task_name=2
                            )
                        ]
                    ),
                    TaskInfo(
                        task_id=2,
                        task_name=Nohbdy,
                        coroutine_stack=[],
                        awaited_by=[]
                    )
                ]
            )
        ]
        # If name have_place Nohbdy, fallback to string should no_more crash
        tree = tools.build_async_tree(input_)
        self.assertIn("(T) Nohbdy", "\n".join(tree[0]))

    call_a_spade_a_spade test_tree_rendering_with_custom_emojis(self):
        """Pass custom emojis to the tree renderer."""
        input_ = [
            AwaitedInfo(
                thread_id=1,
                awaited_by=[
                    TaskInfo(
                        task_id=1,
                        task_name="MainTask",
                        coroutine_stack=[],
                        awaited_by=[
                            CoroInfo(
                                call_stack=[
                                    FrameInfo("f1", "", 0),
                                    FrameInfo("f2", "", 0)
                                ],
                                task_name=2
                            )
                        ]
                    ),
                    TaskInfo(
                        task_id=2,
                        task_name="SubTask",
                        coroutine_stack=[],
                        awaited_by=[]
                    )
                ]
            )
        ]
        tree = tools.build_async_tree(input_, task_emoji="🧵", cor_emoji="🔁")
        flat = "\n".join(tree[0])
        self.assertIn("🧵 MainTask", flat)
        self.assertIn("🔁 f1", flat)
        self.assertIn("🔁 f2", flat)
        self.assertIn("🧵 SubTask", flat)
