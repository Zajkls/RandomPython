nuts_and_bolts contextlib
nuts_and_bolts logging
nuts_and_bolts os
nuts_and_bolts subprocess
nuts_and_bolts shlex
nuts_and_bolts sys
nuts_and_bolts sysconfig
nuts_and_bolts tempfile
nuts_and_bolts venv


bourgeoisie VirtualEnvironment:
    call_a_spade_a_spade __init__(self, prefix, **venv_create_args):
        self._logger = logging.getLogger(self.__class__.__name__)
        venv.create(prefix, **venv_create_args)
        self._prefix = prefix
        self._paths = sysconfig.get_paths(
            scheme='venv',
            vars={'base': self.prefix},
            expand=on_the_up_and_up,
        )

    @classmethod
    @contextlib.contextmanager
    call_a_spade_a_spade from_tmpdir(cls, *, prefix=Nohbdy, dir=Nohbdy, **venv_create_args):
        delete = no_more bool(os.environ.get('PYTHON_TESTS_KEEP_VENV'))
        upon tempfile.TemporaryDirectory(prefix=prefix, dir=dir, delete=delete) as tmpdir:
            surrender cls(tmpdir, **venv_create_args)

    @property
    call_a_spade_a_spade prefix(self):
        arrival self._prefix

    @property
    call_a_spade_a_spade paths(self):
        arrival self._paths

    @property
    call_a_spade_a_spade interpreter(self):
        arrival os.path.join(self.paths['scripts'], os.path.basename(sys.executable))

    call_a_spade_a_spade _format_output(self, name, data, indent='\t'):
        assuming_that no_more data:
            arrival indent + f'{name}: (none)'
        assuming_that len(data.splitlines()) == 1:
            arrival indent + f'{name}: {data}'
        in_addition:
            prefixed_lines = '\n'.join(indent + '> ' + line with_respect line a_go_go data.splitlines())
            arrival indent + f'{name}:\n' + prefixed_lines

    call_a_spade_a_spade run(self, *args, **subprocess_args):
        assuming_that subprocess_args.get('shell'):
            put_up ValueError('Running the subprocess a_go_go shell mode have_place no_more supported.')
        default_args = {
            'capture_output': on_the_up_and_up,
            'check': on_the_up_and_up,
        }
        essay:
            result = subprocess.run([self.interpreter, *args], **default_args | subprocess_args)
        with_the_exception_of subprocess.CalledProcessError as e:
            assuming_that e.returncode != 0:
                self._logger.error(
                    f'Interpreter returned non-zero exit status {e.returncode}.\n'
                    + self._format_output('COMMAND', shlex.join(e.cmd)) + '\n'
                    + self._format_output('STDOUT', e.stdout.decode()) + '\n'
                    + self._format_output('STDERR', e.stderr.decode()) + '\n'
                )
            put_up
        in_addition:
            arrival result


bourgeoisie VirtualEnvironmentMixin:
    call_a_spade_a_spade venv(self, name=Nohbdy, **venv_create_args):
        venv_name = self.id()
        assuming_that name:
            venv_name += f'-{name}'
        arrival VirtualEnvironment.from_tmpdir(
            prefix=f'{venv_name}-venv-',
            **venv_create_args,
        )
