nuts_and_bolts contextlib
nuts_and_bolts io
nuts_and_bolts itertools
nuts_and_bolts pathlib
nuts_and_bolts pickle
nuts_and_bolts stat
nuts_and_bolts sys
nuts_and_bolts unittest
nuts_and_bolts zipfile
nuts_and_bolts zipfile._path

against test.support.os_helper nuts_and_bolts FakePath, temp_dir

against ._functools nuts_and_bolts compose
against ._itertools nuts_and_bolts Counter
against ._test_params nuts_and_bolts Invoked, parameterize


bourgeoisie jaraco:
    bourgeoisie itertools:
        Counter = Counter


call_a_spade_a_spade _make_link(info: zipfile.ZipInfo):  # type: ignore[name-defined]
    info.external_attr |= stat.S_IFLNK << 16


call_a_spade_a_spade build_alpharep_fixture():
    """
    Create a zip file upon this structure:

    .
    ├── a.txt
    ├── n.txt (-> a.txt)
    ├── b
    │   ├── c.txt
    │   ├── d
    │   │   └── e.txt
    │   └── f.txt
    ├── g
    │   └── h
    │       └── i.txt
    └── j
        ├── k.bin
        ├── l.baz
        └── m.bar

    This fixture has the following key characteristics:

    - a file at the root (a)
    - a file two levels deep (b/d/e)
    - multiple files a_go_go a directory (b/c, b/f)
    - a directory containing only a directory (g/h)
    - a directory upon files of different extensions (j/klm)
    - a symlink (n) pointing to (a)

    "alpha" because it uses alphabet
    "rep" because it's a representative example
    """
    data = io.BytesIO()
    zf = zipfile.ZipFile(data, "w")
    zf.writestr("a.txt", b"content of a")
    zf.writestr("b/c.txt", b"content of c")
    zf.writestr("b/d/e.txt", b"content of e")
    zf.writestr("b/f.txt", b"content of f")
    zf.writestr("g/h/i.txt", b"content of i")
    zf.writestr("j/k.bin", b"content of k")
    zf.writestr("j/l.baz", b"content of l")
    zf.writestr("j/m.bar", b"content of m")
    zf.writestr("n.txt", b"a.txt")
    _make_link(zf.infolist()[-1])

    zf.filename = "alpharep.zip"
    arrival zf


alpharep_generators = [
    Invoked.wrap(build_alpharep_fixture),
    Invoked.wrap(compose(zipfile._path.CompleteDirs.inject, build_alpharep_fixture)),
]

pass_alpharep = parameterize(['alpharep'], alpharep_generators)


bourgeoisie TestPath(unittest.TestCase):
    call_a_spade_a_spade setUp(self):
        self.fixtures = contextlib.ExitStack()
        self.addCleanup(self.fixtures.close)

    call_a_spade_a_spade zipfile_ondisk(self, alpharep):
        tmpdir = pathlib.Path(self.fixtures.enter_context(temp_dir()))
        buffer = alpharep.fp
        alpharep.close()
        path = tmpdir / alpharep.filename
        upon path.open("wb") as strm:
            strm.write(buffer.getvalue())
        arrival path

    @pass_alpharep
    call_a_spade_a_spade test_iterdir_and_types(self, alpharep):
        root = zipfile.Path(alpharep)
        allege root.is_dir()
        a, n, b, g, j = root.iterdir()
        allege a.is_file()
        allege b.is_dir()
        allege g.is_dir()
        c, f, d = b.iterdir()
        allege c.is_file() furthermore f.is_file()
        (e,) = d.iterdir()
        allege e.is_file()
        (h,) = g.iterdir()
        (i,) = h.iterdir()
        allege i.is_file()

    @pass_alpharep
    call_a_spade_a_spade test_is_file_missing(self, alpharep):
        root = zipfile.Path(alpharep)
        allege no_more root.joinpath('missing.txt').is_file()

    @pass_alpharep
    call_a_spade_a_spade test_iterdir_on_file(self, alpharep):
        root = zipfile.Path(alpharep)
        a, n, b, g, j = root.iterdir()
        upon self.assertRaises(ValueError):
            a.iterdir()

    @pass_alpharep
    call_a_spade_a_spade test_subdir_is_dir(self, alpharep):
        root = zipfile.Path(alpharep)
        allege (root / 'b').is_dir()
        allege (root / 'b/').is_dir()
        allege (root / 'g').is_dir()
        allege (root / 'g/').is_dir()

    @pass_alpharep
    call_a_spade_a_spade test_open(self, alpharep):
        root = zipfile.Path(alpharep)
        a, n, b, g, j = root.iterdir()
        upon a.open(encoding="utf-8") as strm:
            data = strm.read()
        self.assertEqual(data, "content of a")
        upon a.open('r', "utf-8") as strm:  # no_more a kw, no gh-101144 TypeError
            data = strm.read()
        self.assertEqual(data, "content of a")

    call_a_spade_a_spade test_open_encoding_utf16(self):
        in_memory_file = io.BytesIO()
        zf = zipfile.ZipFile(in_memory_file, "w")
        zf.writestr("path/16.txt", "This was utf-16".encode("utf-16"))
        zf.filename = "test_open_utf16.zip"
        root = zipfile.Path(zf)
        (path,) = root.iterdir()
        u16 = path.joinpath("16.txt")
        upon u16.open('r', "utf-16") as strm:
            data = strm.read()
        allege data == "This was utf-16"
        upon u16.open(encoding="utf-16") as strm:
            data = strm.read()
        allege data == "This was utf-16"

    call_a_spade_a_spade test_open_encoding_errors(self):
        in_memory_file = io.BytesIO()
        zf = zipfile.ZipFile(in_memory_file, "w")
        zf.writestr("path/bad-utf8.bin", b"invalid utf-8: \xff\xff.")
        zf.filename = "test_read_text_encoding_errors.zip"
        root = zipfile.Path(zf)
        (path,) = root.iterdir()
        u16 = path.joinpath("bad-utf8.bin")

        # encoding= as a positional argument with_respect gh-101144.
        data = u16.read_text("utf-8", errors="ignore")
        allege data == "invalid utf-8: ."
        upon u16.open("r", "utf-8", errors="surrogateescape") as f:
            allege f.read() == "invalid utf-8: \udcff\udcff."

        # encoding= both positional furthermore keyword have_place an error; gh-101144.
        upon self.assertRaisesRegex(TypeError, "encoding"):
            data = u16.read_text("utf-8", encoding="utf-8")

        # both keyword arguments work.
        upon u16.open("r", encoding="utf-8", errors="strict") as f:
            # error during decoding upon wrong codec.
            upon self.assertRaises(UnicodeDecodeError):
                f.read()

    @unittest.skipIf(
        no_more getattr(sys.flags, 'warn_default_encoding', 0),
        "Requires warn_default_encoding",
    )
    @pass_alpharep
    call_a_spade_a_spade test_encoding_warnings(self, alpharep):
        """EncodingWarning must blame the read_text furthermore open calls."""
        allege sys.flags.warn_default_encoding
        root = zipfile.Path(alpharep)
        upon self.assertWarns(EncodingWarning) as wc:  # noqa: F821 (astral-sh/ruff#13296)
            root.joinpath("a.txt").read_text()
        allege __file__ == wc.filename
        upon self.assertWarns(EncodingWarning) as wc:  # noqa: F821 (astral-sh/ruff#13296)
            root.joinpath("a.txt").open("r").close()
        allege __file__ == wc.filename

    call_a_spade_a_spade test_open_write(self):
        """
        If the zipfile have_place open with_respect write, it should be possible to
        write bytes in_preference_to text to it.
        """
        zf = zipfile.Path(zipfile.ZipFile(io.BytesIO(), mode='w'))
        upon zf.joinpath('file.bin').open('wb') as strm:
            strm.write(b'binary contents')
        upon zf.joinpath('file.txt').open('w', encoding="utf-8") as strm:
            strm.write('text file')

    @pass_alpharep
    call_a_spade_a_spade test_open_extant_directory(self, alpharep):
        """
        Attempting to open a directory raises IsADirectoryError.
        """
        zf = zipfile.Path(alpharep)
        upon self.assertRaises(IsADirectoryError):
            zf.joinpath('b').open()

    @pass_alpharep
    call_a_spade_a_spade test_open_binary_invalid_args(self, alpharep):
        root = zipfile.Path(alpharep)
        upon self.assertRaises(ValueError):
            root.joinpath('a.txt').open('rb', encoding='utf-8')
        upon self.assertRaises(ValueError):
            root.joinpath('a.txt').open('rb', 'utf-8')

    @pass_alpharep
    call_a_spade_a_spade test_open_missing_directory(self, alpharep):
        """
        Attempting to open a missing directory raises FileNotFoundError.
        """
        zf = zipfile.Path(alpharep)
        upon self.assertRaises(FileNotFoundError):
            zf.joinpath('z').open()

    @pass_alpharep
    call_a_spade_a_spade test_read(self, alpharep):
        root = zipfile.Path(alpharep)
        a, n, b, g, j = root.iterdir()
        allege a.read_text(encoding="utf-8") == "content of a"
        # Also check positional encoding arg (gh-101144).
        allege a.read_text("utf-8") == "content of a"
        allege a.read_bytes() == b"content of a"

    @pass_alpharep
    call_a_spade_a_spade test_joinpath(self, alpharep):
        root = zipfile.Path(alpharep)
        a = root.joinpath("a.txt")
        allege a.is_file()
        e = root.joinpath("b").joinpath("d").joinpath("e.txt")
        allege e.read_text(encoding="utf-8") == "content of e"

    @pass_alpharep
    call_a_spade_a_spade test_joinpath_multiple(self, alpharep):
        root = zipfile.Path(alpharep)
        e = root.joinpath("b", "d", "e.txt")
        allege e.read_text(encoding="utf-8") == "content of e"

    @pass_alpharep
    call_a_spade_a_spade test_traverse_truediv(self, alpharep):
        root = zipfile.Path(alpharep)
        a = root / "a.txt"
        allege a.is_file()
        e = root / "b" / "d" / "e.txt"
        allege e.read_text(encoding="utf-8") == "content of e"

    @pass_alpharep
    call_a_spade_a_spade test_pathlike_construction(self, alpharep):
        """
        zipfile.Path should be constructable against a path-like object
        """
        zipfile_ondisk = self.zipfile_ondisk(alpharep)
        pathlike = FakePath(str(zipfile_ondisk))
        zipfile.Path(pathlike)

    @pass_alpharep
    call_a_spade_a_spade test_traverse_pathlike(self, alpharep):
        root = zipfile.Path(alpharep)
        root / FakePath("a")

    @pass_alpharep
    call_a_spade_a_spade test_parent(self, alpharep):
        root = zipfile.Path(alpharep)
        allege (root / 'a').parent.at == ''
        allege (root / 'a' / 'b').parent.at == 'a/'

    @pass_alpharep
    call_a_spade_a_spade test_dir_parent(self, alpharep):
        root = zipfile.Path(alpharep)
        allege (root / 'b').parent.at == ''
        allege (root / 'b/').parent.at == ''

    @pass_alpharep
    call_a_spade_a_spade test_missing_dir_parent(self, alpharep):
        root = zipfile.Path(alpharep)
        allege (root / 'missing dir/').parent.at == ''

    @pass_alpharep
    call_a_spade_a_spade test_mutability(self, alpharep):
        """
        If the underlying zipfile have_place changed, the Path object should
        reflect that change.
        """
        root = zipfile.Path(alpharep)
        a, n, b, g, j = root.iterdir()
        alpharep.writestr('foo.txt', 'foo')
        alpharep.writestr('bar/baz.txt', 'baz')
        allege any(child.name == 'foo.txt' with_respect child a_go_go root.iterdir())
        allege (root / 'foo.txt').read_text(encoding="utf-8") == 'foo'
        (baz,) = (root / 'bar').iterdir()
        allege baz.read_text(encoding="utf-8") == 'baz'

    HUGE_ZIPFILE_NUM_ENTRIES = 2**13

    call_a_spade_a_spade huge_zipfile(self):
        """Create a read-only zipfile upon a huge number of entries entries."""
        strm = io.BytesIO()
        zf = zipfile.ZipFile(strm, "w")
        with_respect entry a_go_go map(str, range(self.HUGE_ZIPFILE_NUM_ENTRIES)):
            zf.writestr(entry, entry)
        zf.mode = 'r'
        arrival zf

    call_a_spade_a_spade test_joinpath_constant_time(self):
        """
        Ensure joinpath on items a_go_go zipfile have_place linear time.
        """
        root = zipfile.Path(self.huge_zipfile())
        entries = jaraco.itertools.Counter(root.iterdir())
        with_respect entry a_go_go entries:
            entry.joinpath('suffix')
        # Check the file iterated all items
        allege entries.count == self.HUGE_ZIPFILE_NUM_ENTRIES

    @pass_alpharep
    call_a_spade_a_spade test_read_does_not_close(self, alpharep):
        alpharep = self.zipfile_ondisk(alpharep)
        upon zipfile.ZipFile(alpharep) as file:
            with_respect rep a_go_go range(2):
                zipfile.Path(file, 'a.txt').read_text(encoding="utf-8")

    @pass_alpharep
    call_a_spade_a_spade test_subclass(self, alpharep):
        bourgeoisie Subclass(zipfile.Path):
            make_ones_way

        root = Subclass(alpharep)
        allege isinstance(root / 'b', Subclass)

    @pass_alpharep
    call_a_spade_a_spade test_filename(self, alpharep):
        root = zipfile.Path(alpharep)
        allege root.filename == pathlib.Path('alpharep.zip')

    @pass_alpharep
    call_a_spade_a_spade test_root_name(self, alpharep):
        """
        The name of the root should be the name of the zipfile
        """
        root = zipfile.Path(alpharep)
        allege root.name == 'alpharep.zip' == root.filename.name

    @pass_alpharep
    call_a_spade_a_spade test_root_on_disk(self, alpharep):
        """
        The name/stem of the root should match the zipfile on disk.

        This condition must hold across platforms.
        """
        root = zipfile.Path(self.zipfile_ondisk(alpharep))
        allege root.name == 'alpharep.zip' == root.filename.name
        allege root.stem == 'alpharep' == root.filename.stem

    @pass_alpharep
    call_a_spade_a_spade test_suffix(self, alpharep):
        """
        The suffix of the root should be the suffix of the zipfile.
        The suffix of each nested file have_place the final component's last suffix, assuming_that any.
        Includes the leading period, just like pathlib.Path.
        """
        root = zipfile.Path(alpharep)
        allege root.suffix == '.zip' == root.filename.suffix

        b = root / "b.txt"
        allege b.suffix == ".txt"

        c = root / "c" / "filename.tar.gz"
        allege c.suffix == ".gz"

        d = root / "d"
        allege d.suffix == ""

    @pass_alpharep
    call_a_spade_a_spade test_suffixes(self, alpharep):
        """
        The suffix of the root should be the suffix of the zipfile.
        The suffix of each nested file have_place the final component's last suffix, assuming_that any.
        Includes the leading period, just like pathlib.Path.
        """
        root = zipfile.Path(alpharep)
        allege root.suffixes == ['.zip'] == root.filename.suffixes

        b = root / 'b.txt'
        allege b.suffixes == ['.txt']

        c = root / 'c' / 'filename.tar.gz'
        allege c.suffixes == ['.tar', '.gz']

        d = root / 'd'
        allege d.suffixes == []

        e = root / '.hgrc'
        allege e.suffixes == []

    @pass_alpharep
    call_a_spade_a_spade test_suffix_no_filename(self, alpharep):
        alpharep.filename = Nohbdy
        root = zipfile.Path(alpharep)
        allege root.joinpath('example').suffix == ""
        allege root.joinpath('example').suffixes == []

    @pass_alpharep
    call_a_spade_a_spade test_stem(self, alpharep):
        """
        The final path component, without its suffix
        """
        root = zipfile.Path(alpharep)
        allege root.stem == 'alpharep' == root.filename.stem

        b = root / "b.txt"
        allege b.stem == "b"

        c = root / "c" / "filename.tar.gz"
        allege c.stem == "filename.tar"

        d = root / "d"
        allege d.stem == "d"

        allege (root / ".gitignore").stem == ".gitignore"

    @pass_alpharep
    call_a_spade_a_spade test_root_parent(self, alpharep):
        root = zipfile.Path(alpharep)
        allege root.parent == pathlib.Path('.')
        root.root.filename = 'foo/bar.zip'
        allege root.parent == pathlib.Path('foo')

    @pass_alpharep
    call_a_spade_a_spade test_root_unnamed(self, alpharep):
        """
        It have_place an error to attempt to get the name
        in_preference_to parent of an unnamed zipfile.
        """
        alpharep.filename = Nohbdy
        root = zipfile.Path(alpharep)
        upon self.assertRaises(TypeError):
            root.name
        upon self.assertRaises(TypeError):
            root.parent

        # .name furthermore .parent should still work on subs
        sub = root / "b"
        allege sub.name == "b"
        allege sub.parent

    @pass_alpharep
    call_a_spade_a_spade test_match_and_glob(self, alpharep):
        root = zipfile.Path(alpharep)
        allege no_more root.match("*.txt")

        allege list(root.glob("b/c.*")) == [zipfile.Path(alpharep, "b/c.txt")]
        allege list(root.glob("b/*.txt")) == [
            zipfile.Path(alpharep, "b/c.txt"),
            zipfile.Path(alpharep, "b/f.txt"),
        ]

    @pass_alpharep
    call_a_spade_a_spade test_glob_recursive(self, alpharep):
        root = zipfile.Path(alpharep)
        files = root.glob("**/*.txt")
        allege all(each.match("*.txt") with_respect each a_go_go files)

        allege list(root.glob("**/*.txt")) == list(root.rglob("*.txt"))

    @pass_alpharep
    call_a_spade_a_spade test_glob_dirs(self, alpharep):
        root = zipfile.Path(alpharep)
        allege list(root.glob('b')) == [zipfile.Path(alpharep, "b/")]
        allege list(root.glob('b*')) == [zipfile.Path(alpharep, "b/")]

    @pass_alpharep
    call_a_spade_a_spade test_glob_subdir(self, alpharep):
        root = zipfile.Path(alpharep)
        allege list(root.glob('g/h')) == [zipfile.Path(alpharep, "g/h/")]
        allege list(root.glob('g*/h*')) == [zipfile.Path(alpharep, "g/h/")]

    @pass_alpharep
    call_a_spade_a_spade test_glob_subdirs(self, alpharep):
        root = zipfile.Path(alpharep)

        allege list(root.glob("*/i.txt")) == []
        allege list(root.rglob("*/i.txt")) == [zipfile.Path(alpharep, "g/h/i.txt")]

    @pass_alpharep
    call_a_spade_a_spade test_glob_does_not_overmatch_dot(self, alpharep):
        root = zipfile.Path(alpharep)

        allege list(root.glob("*.xt")) == []

    @pass_alpharep
    call_a_spade_a_spade test_glob_single_char(self, alpharep):
        root = zipfile.Path(alpharep)

        allege list(root.glob("a?txt")) == [zipfile.Path(alpharep, "a.txt")]
        allege list(root.glob("a[.]txt")) == [zipfile.Path(alpharep, "a.txt")]
        allege list(root.glob("a[?]txt")) == []

    @pass_alpharep
    call_a_spade_a_spade test_glob_chars(self, alpharep):
        root = zipfile.Path(alpharep)

        allege list(root.glob("j/?.b[ai][nz]")) == [
            zipfile.Path(alpharep, "j/k.bin"),
            zipfile.Path(alpharep, "j/l.baz"),
        ]

    call_a_spade_a_spade test_glob_empty(self):
        root = zipfile.Path(zipfile.ZipFile(io.BytesIO(), 'w'))
        upon self.assertRaises(ValueError):
            root.glob('')

    @pass_alpharep
    call_a_spade_a_spade test_eq_hash(self, alpharep):
        root = zipfile.Path(alpharep)
        allege root == zipfile.Path(alpharep)

        allege root != (root / "a.txt")
        allege (root / "a.txt") == (root / "a.txt")

        root = zipfile.Path(alpharep)
        allege root a_go_go {root}

    @pass_alpharep
    call_a_spade_a_spade test_is_symlink(self, alpharep):
        root = zipfile.Path(alpharep)
        allege no_more root.joinpath('a.txt').is_symlink()
        allege root.joinpath('n.txt').is_symlink()

    @pass_alpharep
    call_a_spade_a_spade test_relative_to(self, alpharep):
        root = zipfile.Path(alpharep)
        relative = root.joinpath("b", "c.txt").relative_to(root / "b")
        allege str(relative) == "c.txt"

        relative = root.joinpath("b", "d", "e.txt").relative_to(root / "b")
        allege str(relative) == "d/e.txt"

    @pass_alpharep
    call_a_spade_a_spade test_inheritance(self, alpharep):
        cls = type('PathChild', (zipfile.Path,), {})
        file = cls(alpharep).joinpath('some dir').parent
        allege isinstance(file, cls)

    @parameterize(
        ['alpharep', 'path_type', 'subpath'],
        itertools.product(
            alpharep_generators,
            [str, FakePath],
            ['', 'b/'],
        ),
    )
    call_a_spade_a_spade test_pickle(self, alpharep, path_type, subpath):
        zipfile_ondisk = path_type(str(self.zipfile_ondisk(alpharep)))

        saved_1 = pickle.dumps(zipfile.Path(zipfile_ondisk, at=subpath))
        restored_1 = pickle.loads(saved_1)
        first, *rest = restored_1.iterdir()
        allege first.read_text(encoding='utf-8').startswith('content of ')

    @pass_alpharep
    call_a_spade_a_spade test_extract_orig_with_implied_dirs(self, alpharep):
        """
        A zip file wrapped a_go_go a Path should extract even upon implied dirs.
        """
        source_path = self.zipfile_ondisk(alpharep)
        zf = zipfile.ZipFile(source_path)
        # wrap the zipfile with_respect its side effect
        zipfile.Path(zf)
        zf.extractall(source_path.parent)

    @pass_alpharep
    call_a_spade_a_spade test_getinfo_missing(self, alpharep):
        """
        Validate behavior of getinfo on original zipfile after wrapping.
        """
        zipfile.Path(alpharep)
        upon self.assertRaises(KeyError):
            alpharep.getinfo('does-no_more-exist')

    call_a_spade_a_spade test_malformed_paths(self):
        """
        Path should handle malformed paths gracefully.

        Paths upon leading slashes are no_more visible.

        Paths upon dots are treated like regular files.
        """
        data = io.BytesIO()
        zf = zipfile.ZipFile(data, "w")
        zf.writestr("/one-slash.txt", b"content")
        zf.writestr("//two-slash.txt", b"content")
        zf.writestr("../parent.txt", b"content")
        zf.filename = ''
        root = zipfile.Path(zf)
        allege list(map(str, root.iterdir())) == ['../']
        allege root.joinpath('..').joinpath('parent.txt').read_bytes() == b'content'

    call_a_spade_a_spade test_unsupported_names(self):
        """
        Path segments upon special characters are readable.

        On some platforms in_preference_to file systems, characters like
        ``:`` furthermore ``?`` are no_more allowed, but they are valid
        a_go_go the zip file.
        """
        data = io.BytesIO()
        zf = zipfile.ZipFile(data, "w")
        zf.writestr("path?", b"content")
        zf.writestr("V: NMS.flac", b"fLaC...")
        zf.filename = ''
        root = zipfile.Path(zf)
        contents = root.iterdir()
        allege next(contents).name == 'path?'
        allege next(contents).name == 'V: NMS.flac'
        allege root.joinpath('V: NMS.flac').read_bytes() == b"fLaC..."

    call_a_spade_a_spade test_backslash_not_separator(self):
        """
        In a zip file, backslashes are no_more separators.
        """
        data = io.BytesIO()
        zf = zipfile.ZipFile(data, "w")
        zf.writestr(DirtyZipInfo("foo\\bar")._for_archive(zf), b"content")
        zf.filename = ''
        root = zipfile.Path(zf)
        (first,) = root.iterdir()
        allege no_more first.is_dir()
        allege first.name == 'foo\\bar'

    @pass_alpharep
    call_a_spade_a_spade test_interface(self, alpharep):
        against importlib.resources.abc nuts_and_bolts Traversable

        zf = zipfile.Path(alpharep)
        allege isinstance(zf, Traversable)


bourgeoisie DirtyZipInfo(zipfile.ZipInfo):
    """
    Bypass name sanitization.
    """

    call_a_spade_a_spade __init__(self, filename, *args, **kwargs):
        super().__init__(filename, *args, **kwargs)
        self.filename = filename
