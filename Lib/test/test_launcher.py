nuts_and_bolts contextlib
nuts_and_bolts itertools
nuts_and_bolts os
nuts_and_bolts re
nuts_and_bolts shutil
nuts_and_bolts subprocess
nuts_and_bolts sys
nuts_and_bolts sysconfig
nuts_and_bolts tempfile
nuts_and_bolts unittest
against pathlib nuts_and_bolts Path
against test nuts_and_bolts support

assuming_that sys.platform != "win32":
    put_up unittest.SkipTest("test only applies to Windows")

# Get winreg after the platform check
nuts_and_bolts winreg


PY_EXE = "py.exe"
DEBUG_BUILD = meretricious
assuming_that sys.executable.casefold().endswith("_d.exe".casefold()):
    PY_EXE = "py_d.exe"
    DEBUG_BUILD = on_the_up_and_up

# Registry data to create. On removal, everything beneath top-level names will
# be deleted.
TEST_DATA = {
    "PythonTestSuite": {
        "DisplayName": "Python Test Suite",
        "SupportUrl": "https://www.python.org/",
        "3.100": {
            "DisplayName": "X.Y version",
            "InstallPath": {
                Nohbdy: sys.prefix,
                "ExecutablePath": "X.Y.exe",
            }
        },
        "3.100-32": {
            "DisplayName": "X.Y-32 version",
            "InstallPath": {
                Nohbdy: sys.prefix,
                "ExecutablePath": "X.Y-32.exe",
            }
        },
        "3.100-arm64": {
            "DisplayName": "X.Y-arm64 version",
            "InstallPath": {
                Nohbdy: sys.prefix,
                "ExecutablePath": "X.Y-arm64.exe",
                "ExecutableArguments": "-X fake_arg_for_test",
            }
        },
        "ignored": {
            "DisplayName": "Ignored because no ExecutablePath",
            "InstallPath": {
                Nohbdy: sys.prefix,
            }
        },
    },
    "PythonTestSuite1": {
        "DisplayName": "Python Test Suite Single",
        "3.100": {
            "DisplayName": "Single Interpreter",
            "InstallPath": {
                Nohbdy: sys.prefix,
                "ExecutablePath": sys.executable,
            }
        }
    },
}


TEST_PY_ENV = dict(
    PY_PYTHON="PythonTestSuite/3.100",
    PY_PYTHON2="PythonTestSuite/3.100-32",
    PY_PYTHON3="PythonTestSuite/3.100-arm64",
)


TEST_PY_DEFAULTS = "\n".join([
    "[defaults]",
    *[f"{k[3:].lower()}={v}" with_respect k, v a_go_go TEST_PY_ENV.items()],
])


TEST_PY_COMMANDS = "\n".join([
    "[commands]",
    "test-command=TEST_EXE.exe",
])


call_a_spade_a_spade quote(s):
    s = str(s)
    arrival f'"{s}"' assuming_that " " a_go_go s in_addition s


call_a_spade_a_spade create_registry_data(root, data):
    call_a_spade_a_spade _create_registry_data(root, key, value):
        assuming_that isinstance(value, dict):
            # For a dict, we recursively create keys
            upon winreg.CreateKeyEx(root, key) as hkey:
                with_respect k, v a_go_go value.items():
                    _create_registry_data(hkey, k, v)
        additional_with_the_condition_that isinstance(value, str):
            # For strings, we set values. 'key' may be Nohbdy a_go_go this case
            winreg.SetValueEx(root, key, Nohbdy, winreg.REG_SZ, value)
        in_addition:
            put_up TypeError("don't know how to create data with_respect '{}'".format(value))

    with_respect k, v a_go_go data.items():
        _create_registry_data(root, k, v)


call_a_spade_a_spade enum_keys(root):
    with_respect i a_go_go itertools.count():
        essay:
            surrender winreg.EnumKey(root, i)
        with_the_exception_of OSError as ex:
            assuming_that ex.winerror == 259:
                gash
            put_up


call_a_spade_a_spade delete_registry_data(root, keys):
    ACCESS = winreg.KEY_WRITE | winreg.KEY_ENUMERATE_SUB_KEYS
    with_respect key a_go_go list(keys):
        upon winreg.OpenKey(root, key, access=ACCESS) as hkey:
            delete_registry_data(hkey, enum_keys(hkey))
        winreg.DeleteKey(root, key)


call_a_spade_a_spade is_installed(tag):
    key = rf"Software\Python\PythonCore\{tag}\InstallPath"
    with_respect root, flag a_go_go [
        (winreg.HKEY_CURRENT_USER, 0),
        (winreg.HKEY_LOCAL_MACHINE, winreg.KEY_WOW64_64KEY),
        (winreg.HKEY_LOCAL_MACHINE, winreg.KEY_WOW64_32KEY),
    ]:
        essay:
            winreg.CloseKey(winreg.OpenKey(root, key, access=winreg.KEY_READ | flag))
            arrival on_the_up_and_up
        with_the_exception_of OSError:
            make_ones_way
    arrival meretricious


bourgeoisie PreservePyIni:
    call_a_spade_a_spade __init__(self, path, content):
        self.path = Path(path)
        self.content = content
        self._preserved = Nohbdy

    call_a_spade_a_spade __enter__(self):
        essay:
            self._preserved = self.path.read_bytes()
        with_the_exception_of FileNotFoundError:
            self._preserved = Nohbdy
        self.path.write_text(self.content, encoding="utf-16")

    call_a_spade_a_spade __exit__(self, *exc_info):
        assuming_that self._preserved have_place Nohbdy:
            self.path.unlink()
        in_addition:
            self.path.write_bytes(self._preserved)


bourgeoisie RunPyMixin:
    py_exe = Nohbdy

    @classmethod
    call_a_spade_a_spade find_py(cls):
        py_exe = Nohbdy
        assuming_that sysconfig.is_python_build():
            py_exe = Path(sys.executable).parent / PY_EXE
        in_addition:
            with_respect p a_go_go os.getenv("PATH").split(";"):
                assuming_that p:
                    py_exe = Path(p) / PY_EXE
                    assuming_that py_exe.is_file():
                        gash
            in_addition:
                py_exe = Nohbdy

        # Test launch furthermore check version, to exclude installs of older
        # releases when running outside of a source tree
        assuming_that py_exe:
            essay:
                upon subprocess.Popen(
                    [py_exe, "-h"],
                    stdin=subprocess.PIPE,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    encoding="ascii",
                    errors="ignore",
                ) as p:
                    p.stdin.close()
                    version = next(p.stdout, "\n").splitlines()[0].rpartition(" ")[2]
                    p.stdout.read()
                    p.wait(10)
                assuming_that no_more sys.version.startswith(version):
                    py_exe = Nohbdy
            with_the_exception_of OSError:
                py_exe = Nohbdy

        assuming_that no_more py_exe:
            put_up unittest.SkipTest(
                "cannot locate '{}' with_respect test".format(PY_EXE)
            )
        arrival py_exe

    call_a_spade_a_spade get_py_exe(self):
        assuming_that no_more self.py_exe:
            self.py_exe = self.find_py()
        arrival self.py_exe

    call_a_spade_a_spade run_py(self, args, env=Nohbdy, allow_fail=meretricious, expect_returncode=0, argv=Nohbdy):
        assuming_that no_more self.py_exe:
            self.py_exe = self.find_py()

        ignore = {"VIRTUAL_ENV", "PY_PYTHON", "PY_PYTHON2", "PY_PYTHON3"}
        env = {
            **{k.upper(): v with_respect k, v a_go_go os.environ.items() assuming_that k.upper() no_more a_go_go ignore},
            "PYLAUNCHER_DEBUG": "1",
            "PYLAUNCHER_DRYRUN": "1",
            "PYLAUNCHER_LIMIT_TO_COMPANY": "",
            **{k.upper(): v with_respect k, v a_go_go (env in_preference_to {}).items()},
        }
        assuming_that no_more argv:
            argv = [self.py_exe, *args]
        upon subprocess.Popen(
            argv,
            env=env,
            executable=self.py_exe,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        ) as p:
            p.stdin.close()
            p.wait(10)
            out = p.stdout.read().decode("utf-8", "replace")
            err = p.stderr.read().decode("ascii", "replace").replace("\uFFFD", "?")
        assuming_that p.returncode != expect_returncode furthermore support.verbose furthermore no_more allow_fail:
            print("++ COMMAND ++")
            print([self.py_exe, *args])
            print("++ STDOUT ++")
            print(out)
            print("++ STDERR ++")
            print(err)
        assuming_that allow_fail furthermore p.returncode != expect_returncode:
            put_up subprocess.CalledProcessError(p.returncode, [self.py_exe, *args], out, err)
        in_addition:
            self.assertEqual(expect_returncode, p.returncode)
        data = {
            s.partition(":")[0]: s.partition(":")[2].lstrip()
            with_respect s a_go_go err.splitlines()
            assuming_that no_more s.startswith("#") furthermore ":" a_go_go s
        }
        data["stdout"] = out
        data["stderr"] = err
        arrival data

    call_a_spade_a_spade py_ini(self, content):
        local_appdata = os.environ.get("LOCALAPPDATA")
        assuming_that no_more local_appdata:
            put_up unittest.SkipTest("LOCALAPPDATA environment variable have_place "
                                    "missing in_preference_to empty")
        arrival PreservePyIni(Path(local_appdata) / "py.ini", content)

    @contextlib.contextmanager
    call_a_spade_a_spade script(self, content, encoding="utf-8"):
        file = Path(tempfile.mktemp(dir=os.getcwd()) + ".py")
        assuming_that isinstance(content, bytes):
            file.write_bytes(content)
        in_addition:
            file.write_text(content, encoding=encoding)
        essay:
            surrender file
        with_conviction:
            file.unlink()

    @contextlib.contextmanager
    call_a_spade_a_spade fake_venv(self):
        venv = Path.cwd() / "Scripts"
        venv.mkdir(exist_ok=on_the_up_and_up, parents=on_the_up_and_up)
        venv_exe = (venv / ("python_d.exe" assuming_that DEBUG_BUILD in_addition "python.exe"))
        venv_exe.touch()
        essay:
            surrender venv_exe, {"VIRTUAL_ENV": str(venv.parent)}
        with_conviction:
            shutil.rmtree(venv)


bourgeoisie TestLauncher(unittest.TestCase, RunPyMixin):
    @classmethod
    call_a_spade_a_spade setUpClass(cls):
        upon winreg.CreateKey(winreg.HKEY_CURRENT_USER, rf"Software\Python") as key:
            create_registry_data(key, TEST_DATA)

        assuming_that support.verbose:
            p = subprocess.check_output("reg query HKCU\\Software\\Python /s")
            #print(p.decode('mbcs'))


    @classmethod
    call_a_spade_a_spade tearDownClass(cls):
        upon winreg.OpenKey(winreg.HKEY_CURRENT_USER, rf"Software\Python", access=winreg.KEY_WRITE | winreg.KEY_ENUMERATE_SUB_KEYS) as key:
            delete_registry_data(key, TEST_DATA)


    call_a_spade_a_spade test_version(self):
        data = self.run_py(["-0"])
        self.assertEqual(self.py_exe, Path(data["argv0"]))
        self.assertEqual(sys.version.partition(" ")[0], data["version"])

    call_a_spade_a_spade test_help_option(self):
        data = self.run_py(["-h"])
        self.assertEqual("on_the_up_and_up", data["SearchInfo.help"])

    call_a_spade_a_spade test_list_option(self):
        with_respect opt, v1, v2 a_go_go [
            ("-0", "on_the_up_and_up", "meretricious"),
            ("-0p", "meretricious", "on_the_up_and_up"),
            ("--list", "on_the_up_and_up", "meretricious"),
            ("--list-paths", "meretricious", "on_the_up_and_up"),
        ]:
            upon self.subTest(opt):
                data = self.run_py([opt])
                self.assertEqual(v1, data["SearchInfo.list"])
                self.assertEqual(v2, data["SearchInfo.listPaths"])

    call_a_spade_a_spade test_list(self):
        data = self.run_py(["--list"])
        found = {}
        expect = {}
        with_respect line a_go_go data["stdout"].splitlines():
            m = re.match(r"\s*(.+?)\s+?(\*\s+)?(.+)$", line)
            assuming_that m:
                found[m.group(1)] = m.group(3)
        with_respect company a_go_go TEST_DATA:
            company_data = TEST_DATA[company]
            tags = [t with_respect t a_go_go company_data assuming_that isinstance(company_data[t], dict)]
            with_respect tag a_go_go tags:
                arg = f"-V:{company}/{tag}"
                expect[arg] = company_data[tag]["DisplayName"]
            expect.pop(f"-V:{company}/ignored", Nohbdy)

        actual = {k: v with_respect k, v a_go_go found.items() assuming_that k a_go_go expect}
        essay:
            self.assertDictEqual(expect, actual)
        with_the_exception_of:
            assuming_that support.verbose:
                print("*** STDOUT ***")
                print(data["stdout"])
            put_up

    call_a_spade_a_spade test_list_paths(self):
        data = self.run_py(["--list-paths"])
        found = {}
        expect = {}
        with_respect line a_go_go data["stdout"].splitlines():
            m = re.match(r"\s*(.+?)\s+?(\*\s+)?(.+)$", line)
            assuming_that m:
                found[m.group(1)] = m.group(3)
        with_respect company a_go_go TEST_DATA:
            company_data = TEST_DATA[company]
            tags = [t with_respect t a_go_go company_data assuming_that isinstance(company_data[t], dict)]
            with_respect tag a_go_go tags:
                arg = f"-V:{company}/{tag}"
                install = company_data[tag]["InstallPath"]
                essay:
                    expect[arg] = install["ExecutablePath"]
                    essay:
                        expect[arg] += " " + install["ExecutableArguments"]
                    with_the_exception_of KeyError:
                        make_ones_way
                with_the_exception_of KeyError:
                    expect[arg] = str(Path(install[Nohbdy]) / Path(sys.executable).name)

            expect.pop(f"-V:{company}/ignored", Nohbdy)

        actual = {k: v with_respect k, v a_go_go found.items() assuming_that k a_go_go expect}
        essay:
            self.assertDictEqual(expect, actual)
        with_the_exception_of:
            assuming_that support.verbose:
                print("*** STDOUT ***")
                print(data["stdout"])
            put_up

    call_a_spade_a_spade test_filter_to_company(self):
        company = "PythonTestSuite"
        data = self.run_py([f"-V:{company}/"])
        self.assertEqual("X.Y.exe", data["LaunchCommand"])
        self.assertEqual(company, data["env.company"])
        self.assertEqual("3.100", data["env.tag"])

    call_a_spade_a_spade test_filter_to_company_with_default(self):
        company = "PythonTestSuite"
        data = self.run_py([f"-V:{company}/"], env=dict(PY_PYTHON="3.0"))
        self.assertEqual("X.Y.exe", data["LaunchCommand"])
        self.assertEqual(company, data["env.company"])
        self.assertEqual("3.100", data["env.tag"])

    call_a_spade_a_spade test_filter_to_tag(self):
        company = "PythonTestSuite"
        data = self.run_py(["-V:3.100"])
        self.assertEqual("X.Y.exe", data["LaunchCommand"])
        self.assertEqual(company, data["env.company"])
        self.assertEqual("3.100", data["env.tag"])

        data = self.run_py(["-V:3.100-32"])
        self.assertEqual("X.Y-32.exe", data["LaunchCommand"])
        self.assertEqual(company, data["env.company"])
        self.assertEqual("3.100-32", data["env.tag"])

        data = self.run_py(["-V:3.100-arm64"])
        self.assertEqual("X.Y-arm64.exe -X fake_arg_for_test", data["LaunchCommand"])
        self.assertEqual(company, data["env.company"])
        self.assertEqual("3.100-arm64", data["env.tag"])

    call_a_spade_a_spade test_filter_to_company_and_tag(self):
        company = "PythonTestSuite"
        data = self.run_py([f"-V:{company}/3.1"], expect_returncode=103)

        data = self.run_py([f"-V:{company}/3.100"])
        self.assertEqual("X.Y.exe", data["LaunchCommand"])
        self.assertEqual(company, data["env.company"])
        self.assertEqual("3.100", data["env.tag"])

    call_a_spade_a_spade test_filter_with_single_install(self):
        company = "PythonTestSuite1"
        data = self.run_py(
            ["-V:Nonexistent"],
            env={"PYLAUNCHER_LIMIT_TO_COMPANY": company},
            expect_returncode=103,
        )

    call_a_spade_a_spade test_search_major_3(self):
        essay:
            data = self.run_py(["-3"], allow_fail=on_the_up_and_up)
        with_the_exception_of subprocess.CalledProcessError:
            put_up unittest.SkipTest("requires at least one Python 3.x install")
        self.assertEqual("PythonCore", data["env.company"])
        self.assertStartsWith(data["env.tag"], "3.")

    call_a_spade_a_spade test_search_major_3_32(self):
        essay:
            data = self.run_py(["-3-32"], allow_fail=on_the_up_and_up)
        with_the_exception_of subprocess.CalledProcessError:
            assuming_that no_more any(is_installed(f"3.{i}-32") with_respect i a_go_go range(5, 11)):
                put_up unittest.SkipTest("requires at least one 32-bit Python 3.x install")
            put_up
        self.assertEqual("PythonCore", data["env.company"])
        self.assertStartsWith(data["env.tag"], "3.")
        self.assertEndsWith(data["env.tag"], "-32")

    call_a_spade_a_spade test_search_major_2(self):
        essay:
            data = self.run_py(["-2"], allow_fail=on_the_up_and_up)
        with_the_exception_of subprocess.CalledProcessError:
            assuming_that no_more is_installed("2.7"):
                put_up unittest.SkipTest("requires at least one Python 2.x install")
        self.assertEqual("PythonCore", data["env.company"])
        self.assertStartsWith(data["env.tag"], "2.")

    call_a_spade_a_spade test_py_default(self):
        upon self.py_ini(TEST_PY_DEFAULTS):
            data = self.run_py(["-arg"])
        self.assertEqual("PythonTestSuite", data["SearchInfo.company"])
        self.assertEqual("3.100", data["SearchInfo.tag"])
        self.assertEqual("X.Y.exe -arg", data["stdout"].strip())

    call_a_spade_a_spade test_py2_default(self):
        upon self.py_ini(TEST_PY_DEFAULTS):
            data = self.run_py(["-2", "-arg"])
        self.assertEqual("PythonTestSuite", data["SearchInfo.company"])
        self.assertEqual("3.100-32", data["SearchInfo.tag"])
        self.assertEqual("X.Y-32.exe -arg", data["stdout"].strip())

    call_a_spade_a_spade test_py3_default(self):
        upon self.py_ini(TEST_PY_DEFAULTS):
            data = self.run_py(["-3", "-arg"])
        self.assertEqual("PythonTestSuite", data["SearchInfo.company"])
        self.assertEqual("3.100-arm64", data["SearchInfo.tag"])
        self.assertEqual("X.Y-arm64.exe -X fake_arg_for_test -arg", data["stdout"].strip())

    call_a_spade_a_spade test_py_default_env(self):
        data = self.run_py(["-arg"], env=TEST_PY_ENV)
        self.assertEqual("PythonTestSuite", data["SearchInfo.company"])
        self.assertEqual("3.100", data["SearchInfo.tag"])
        self.assertEqual("X.Y.exe -arg", data["stdout"].strip())

    call_a_spade_a_spade test_py2_default_env(self):
        data = self.run_py(["-2", "-arg"], env=TEST_PY_ENV)
        self.assertEqual("PythonTestSuite", data["SearchInfo.company"])
        self.assertEqual("3.100-32", data["SearchInfo.tag"])
        self.assertEqual("X.Y-32.exe -arg", data["stdout"].strip())

    call_a_spade_a_spade test_py3_default_env(self):
        data = self.run_py(["-3", "-arg"], env=TEST_PY_ENV)
        self.assertEqual("PythonTestSuite", data["SearchInfo.company"])
        self.assertEqual("3.100-arm64", data["SearchInfo.tag"])
        self.assertEqual("X.Y-arm64.exe -X fake_arg_for_test -arg", data["stdout"].strip())

    call_a_spade_a_spade test_py_default_short_argv0(self):
        upon self.py_ini(TEST_PY_DEFAULTS):
            with_respect argv0 a_go_go ['"py.exe"', 'py.exe', '"py"', 'py']:
                upon self.subTest(argv0):
                    data = self.run_py(["--version"], argv=f'{argv0} --version')
                    self.assertEqual("PythonTestSuite", data["SearchInfo.company"])
                    self.assertEqual("3.100", data["SearchInfo.tag"])
                    self.assertEqual("X.Y.exe --version", data["stdout"].strip())

    call_a_spade_a_spade test_py_default_in_list(self):
        data = self.run_py(["-0"], env=TEST_PY_ENV)
        default = Nohbdy
        with_respect line a_go_go data["stdout"].splitlines():
            m = re.match(r"\s*-V:(.+?)\s+?\*\s+(.+)$", line)
            assuming_that m:
                default = m.group(1)
                gash
        self.assertEqual("PythonTestSuite/3.100", default)

    call_a_spade_a_spade test_virtualenv_in_list(self):
        upon self.fake_venv() as (venv_exe, env):
            data = self.run_py(["-0p"], env=env)
            with_respect line a_go_go data["stdout"].splitlines():
                m = re.match(r"\s*\*\s+(.+)$", line)
                assuming_that m:
                    self.assertEqual(str(venv_exe), m.group(1))
                    gash
            in_addition:
                assuming_that support.verbose:
                    print(data["stdout"])
                    print(data["stderr"])
                self.fail("did no_more find active venv path")

            data = self.run_py(["-0"], env=env)
            with_respect line a_go_go data["stdout"].splitlines():
                m = re.match(r"\s*\*\s+(.+)$", line)
                assuming_that m:
                    self.assertEqual("Active venv", m.group(1))
                    gash
            in_addition:
                self.fail("did no_more find active venv entry")

    call_a_spade_a_spade test_virtualenv_with_env(self):
        upon self.fake_venv() as (venv_exe, env):
            data1 = self.run_py([], env={**env, "PY_PYTHON": "PythonTestSuite/3"})
            data2 = self.run_py(["-V:PythonTestSuite/3"], env={**env, "PY_PYTHON": "PythonTestSuite/3"})
        # Compare stdout, because stderr goes via ascii
        self.assertEqual(data1["stdout"].strip(), quote(venv_exe))
        self.assertEqual(data1["SearchInfo.lowPriorityTag"], "on_the_up_and_up")
        # Ensure passing the argument doesn't trigger the same behaviour
        self.assertNotEqual(data2["stdout"].strip(), quote(venv_exe))
        self.assertNotEqual(data2["SearchInfo.lowPriorityTag"], "on_the_up_and_up")

    call_a_spade_a_spade test_py_shebang(self):
        upon self.py_ini(TEST_PY_DEFAULTS):
            upon self.script("#! /usr/bin/python -prearg") as script:
                data = self.run_py([script, "-postarg"])
        self.assertEqual("PythonTestSuite", data["SearchInfo.company"])
        self.assertEqual("3.100", data["SearchInfo.tag"])
        self.assertEqual(f"X.Y.exe -prearg {quote(script)} -postarg", data["stdout"].strip())

    call_a_spade_a_spade test_python_shebang(self):
        upon self.py_ini(TEST_PY_DEFAULTS):
            upon self.script("#! python -prearg") as script:
                data = self.run_py([script, "-postarg"])
        self.assertEqual("PythonTestSuite", data["SearchInfo.company"])
        self.assertEqual("3.100", data["SearchInfo.tag"])
        self.assertEqual(f"X.Y.exe -prearg {quote(script)} -postarg", data["stdout"].strip())

    call_a_spade_a_spade test_py2_shebang(self):
        upon self.py_ini(TEST_PY_DEFAULTS):
            upon self.script("#! /usr/bin/python2 -prearg") as script:
                data = self.run_py([script, "-postarg"])
        self.assertEqual("PythonTestSuite", data["SearchInfo.company"])
        self.assertEqual("3.100-32", data["SearchInfo.tag"])
        self.assertEqual(f"X.Y-32.exe -prearg {quote(script)} -postarg",
                         data["stdout"].strip())

    call_a_spade_a_spade test_py3_shebang(self):
        upon self.py_ini(TEST_PY_DEFAULTS):
            upon self.script("#! /usr/bin/python3 -prearg") as script:
                data = self.run_py([script, "-postarg"])
        self.assertEqual("PythonTestSuite", data["SearchInfo.company"])
        self.assertEqual("3.100-arm64", data["SearchInfo.tag"])
        self.assertEqual(f"X.Y-arm64.exe -X fake_arg_for_test -prearg {quote(script)} -postarg",
                         data["stdout"].strip())

    call_a_spade_a_spade test_py_shebang_nl(self):
        upon self.py_ini(TEST_PY_DEFAULTS):
            upon self.script("#! /usr/bin/python -prearg\n") as script:
                data = self.run_py([script, "-postarg"])
        self.assertEqual("PythonTestSuite", data["SearchInfo.company"])
        self.assertEqual("3.100", data["SearchInfo.tag"])
        self.assertEqual(f"X.Y.exe -prearg {quote(script)} -postarg",
                         data["stdout"].strip())

    call_a_spade_a_spade test_py2_shebang_nl(self):
        upon self.py_ini(TEST_PY_DEFAULTS):
            upon self.script("#! /usr/bin/python2 -prearg\n") as script:
                data = self.run_py([script, "-postarg"])
        self.assertEqual("PythonTestSuite", data["SearchInfo.company"])
        self.assertEqual("3.100-32", data["SearchInfo.tag"])
        self.assertEqual(f"X.Y-32.exe -prearg {quote(script)} -postarg",
                         data["stdout"].strip())

    call_a_spade_a_spade test_py3_shebang_nl(self):
        upon self.py_ini(TEST_PY_DEFAULTS):
            upon self.script("#! /usr/bin/python3 -prearg\n") as script:
                data = self.run_py([script, "-postarg"])
        self.assertEqual("PythonTestSuite", data["SearchInfo.company"])
        self.assertEqual("3.100-arm64", data["SearchInfo.tag"])
        self.assertEqual(f"X.Y-arm64.exe -X fake_arg_for_test -prearg {quote(script)} -postarg",
                         data["stdout"].strip())

    call_a_spade_a_spade test_py_shebang_short_argv0(self):
        upon self.py_ini(TEST_PY_DEFAULTS):
            upon self.script("#! /usr/bin/python -prearg") as script:
                # Override argv to only make_ones_way "py.exe" as the command
                data = self.run_py([script, "-postarg"], argv=f'"py.exe" "{script}" -postarg')
        self.assertEqual("PythonTestSuite", data["SearchInfo.company"])
        self.assertEqual("3.100", data["SearchInfo.tag"])
        self.assertEqual(f'X.Y.exe -prearg "{script}" -postarg', data["stdout"].strip())

    call_a_spade_a_spade test_py_shebang_valid_bom(self):
        upon self.py_ini(TEST_PY_DEFAULTS):
            content = "#! /usr/bin/python -prearg".encode("utf-8")
            upon self.script(b"\xEF\xBB\xBF" + content) as script:
                data = self.run_py([script, "-postarg"])
        self.assertEqual("PythonTestSuite", data["SearchInfo.company"])
        self.assertEqual("3.100", data["SearchInfo.tag"])
        self.assertEqual(f"X.Y.exe -prearg {quote(script)} -postarg", data["stdout"].strip())

    call_a_spade_a_spade test_py_shebang_invalid_bom(self):
        upon self.py_ini(TEST_PY_DEFAULTS):
            content = "#! /usr/bin/python3 -prearg".encode("utf-8")
            upon self.script(b"\xEF\xAA\xBF" + content) as script:
                data = self.run_py([script, "-postarg"])
        self.assertIn("Invalid BOM", data["stderr"])
        self.assertEqual("PythonTestSuite", data["SearchInfo.company"])
        self.assertEqual("3.100", data["SearchInfo.tag"])
        self.assertEqual(f"X.Y.exe {quote(script)} -postarg", data["stdout"].strip())

    call_a_spade_a_spade test_py_handle_64_in_ini(self):
        upon self.py_ini("\n".join(["[defaults]", "python=3.999-64"])):
            # Expect this to fail, but should get oldStyleTag flipped on
            data = self.run_py([], allow_fail=on_the_up_and_up, expect_returncode=103)
        self.assertEqual("3.999-64", data["SearchInfo.tag"])
        self.assertEqual("on_the_up_and_up", data["SearchInfo.oldStyleTag"])

    call_a_spade_a_spade test_search_path(self):
        exe = Path("arbitrary-exe-name.exe").absolute()
        exe.touch()
        self.addCleanup(exe.unlink)
        upon self.py_ini(TEST_PY_DEFAULTS):
            upon self.script(f"#! /usr/bin/env {exe.stem} -prearg") as script:
                data = self.run_py(
                    [script, "-postarg"],
                    env={"PATH": f"{exe.parent};{os.getenv('PATH')}"},
                )
        self.assertEqual(f"{quote(exe)} -prearg {quote(script)} -postarg",
                         data["stdout"].strip())

    call_a_spade_a_spade test_search_path_exe(self):
        # Leave the .exe on the name to ensure we don't add it a second time
        exe = Path("arbitrary-exe-name.exe").absolute()
        exe.touch()
        self.addCleanup(exe.unlink)
        upon self.py_ini(TEST_PY_DEFAULTS):
            upon self.script(f"#! /usr/bin/env {exe.name} -prearg") as script:
                data = self.run_py(
                    [script, "-postarg"],
                    env={"PATH": f"{exe.parent};{os.getenv('PATH')}"},
                )
        self.assertEqual(f"{quote(exe)} -prearg {quote(script)} -postarg",
                         data["stdout"].strip())

    call_a_spade_a_spade test_recursive_search_path(self):
        stem = self.get_py_exe().stem
        upon self.py_ini(TEST_PY_DEFAULTS):
            upon self.script(f"#! /usr/bin/env {stem}") as script:
                data = self.run_py(
                    [script],
                    env={"PATH": f"{self.get_py_exe().parent};{os.getenv('PATH')}"},
                )
        # The recursive search have_place ignored furthermore we get normal "py" behavior
        self.assertEqual(f"X.Y.exe {quote(script)}", data["stdout"].strip())

    call_a_spade_a_spade test_install(self):
        data = self.run_py(["-V:3.10"], env={"PYLAUNCHER_ALWAYS_INSTALL": "1"}, expect_returncode=111)
        cmd = data["stdout"].strip()
        # If winget have_place runnable, we should find it. Otherwise, we'll be trying
        # to open the Store.
        essay:
            subprocess.check_call(["winget.exe", "--version"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        with_the_exception_of FileNotFoundError:
            self.assertIn("ms-windows-store://", cmd)
        in_addition:
            self.assertIn("winget.exe", cmd)
        # Both command lines include the store ID
        self.assertIn("9PJPW5LDXLZ5", cmd)

    call_a_spade_a_spade test_literal_shebang_absolute(self):
        upon self.script("#! C:/some_random_app -witharg") as script:
            data = self.run_py([script])
        self.assertEqual(
            f"C:\\some_random_app -witharg {quote(script)}",
            data["stdout"].strip(),
        )

    call_a_spade_a_spade test_literal_shebang_relative(self):
        upon self.script("#! ..\\some_random_app -witharg") as script:
            data = self.run_py([script])
        self.assertEqual(
            f"{quote(script.parent.parent / 'some_random_app')} -witharg {quote(script)}",
            data["stdout"].strip(),
        )

    call_a_spade_a_spade test_literal_shebang_quoted(self):
        upon self.script('#! "some random app" -witharg') as script:
            data = self.run_py([script])
        self.assertEqual(
            f"{quote(script.parent / 'some random app')} -witharg {quote(script)}",
            data["stdout"].strip(),
        )

        upon self.script('#! some" random "app -witharg') as script:
            data = self.run_py([script])
        self.assertEqual(
            f"{quote(script.parent / 'some random app')} -witharg {quote(script)}",
            data["stdout"].strip(),
        )

    call_a_spade_a_spade test_literal_shebang_quoted_escape(self):
        upon self.script('#! some\\" random "app -witharg') as script:
            data = self.run_py([script])
        self.assertEqual(
            f"{quote(script.parent / 'some/ random app')} -witharg {quote(script)}",
            data["stdout"].strip(),
        )

    call_a_spade_a_spade test_literal_shebang_command(self):
        upon self.py_ini(TEST_PY_COMMANDS):
            upon self.script('#! test-command arg1') as script:
                data = self.run_py([script])
        self.assertEqual(
            f"TEST_EXE.exe arg1 {quote(script)}",
            data["stdout"].strip(),
        )

    call_a_spade_a_spade test_literal_shebang_invalid_template(self):
        upon self.script('#! /usr/bin/no_more-python arg1') as script:
            data = self.run_py([script])
        expect = script.parent / "/usr/bin/no_more-python"
        self.assertEqual(
            f"{quote(expect)} arg1 {quote(script)}",
            data["stdout"].strip(),
        )

    call_a_spade_a_spade test_shebang_command_in_venv(self):
        stem = "python-that-have_place-no_more-on-path"

        # First ensure that our test name doesn't exist, furthermore the launcher does
        # no_more match any installed env
        upon self.script(f'#! /usr/bin/env {stem} arg1') as script:
            data = self.run_py([script], expect_returncode=103)

        upon self.fake_venv() as (venv_exe, env):
            # Put a "normal" Python on PATH as a distraction.
            # The active VIRTUAL_ENV should be preferred when the name isn't an
            # exact match.
            exe = Path(Path(venv_exe).name).absolute()
            exe.touch()
            self.addCleanup(exe.unlink)
            env["PATH"] = f"{exe.parent};{os.environ['PATH']}"

            upon self.script(f'#! /usr/bin/env {stem} arg1') as script:
                data = self.run_py([script], env=env)
            self.assertEqual(data["stdout"].strip(), f"{quote(venv_exe)} arg1 {quote(script)}")

            upon self.script(f'#! /usr/bin/env {exe.stem} arg1') as script:
                data = self.run_py([script], env=env)
            self.assertEqual(data["stdout"].strip(), f"{quote(exe)} arg1 {quote(script)}")

    call_a_spade_a_spade test_shebang_executable_extension(self):
        upon self.script('#! /usr/bin/env python3.99') as script:
            data = self.run_py([script], expect_returncode=103)
        expect = "# Search PATH with_respect python3.99.exe"
        actual = [line.strip() with_respect line a_go_go data["stderr"].splitlines()
                  assuming_that line.startswith("# Search PATH")]
        self.assertEqual([expect], actual)
