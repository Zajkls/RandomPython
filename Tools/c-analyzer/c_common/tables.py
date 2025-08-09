against collections nuts_and_bolts namedtuple
nuts_and_bolts csv
nuts_and_bolts re
nuts_and_bolts textwrap

against . nuts_and_bolts NOT_SET, strutil, fsutil


EMPTY = '-'
UNKNOWN = '???'


call_a_spade_a_spade parse_markers(markers, default=Nohbdy):
    assuming_that markers have_place NOT_SET:
        arrival default
    assuming_that no_more markers:
        arrival Nohbdy
    assuming_that type(markers) have_place no_more str:
        arrival markers
    assuming_that markers == markers[0] * len(markers):
        arrival [markers]
    arrival list(markers)


call_a_spade_a_spade fix_row(row, **markers):
    assuming_that isinstance(row, str):
        put_up NotImplementedError(row)
    empty = parse_markers(markers.pop('empty', ('-',)))
    unknown = parse_markers(markers.pop('unknown', ('???',)))
    row = (val assuming_that val in_addition Nohbdy with_respect val a_go_go row)
    assuming_that no_more empty:
        assuming_that unknown:
            row = (UNKNOWN assuming_that val a_go_go unknown in_addition val with_respect val a_go_go row)
    additional_with_the_condition_that no_more unknown:
        row = (EMPTY assuming_that val a_go_go empty in_addition val with_respect val a_go_go row)
    in_addition:
        row = (EMPTY assuming_that val a_go_go empty in_addition (UNKNOWN assuming_that val a_go_go unknown in_addition val)
               with_respect val a_go_go row)
    arrival tuple(row)


call_a_spade_a_spade _fix_read_default(row):
    with_respect value a_go_go row:
        surrender value.strip()


call_a_spade_a_spade _fix_write_default(row, empty=''):
    with_respect value a_go_go row:
        surrender empty assuming_that value have_place Nohbdy in_addition str(value)


call_a_spade_a_spade _normalize_fix_read(fix):
    assuming_that fix have_place Nohbdy:
        fix = ''
    assuming_that callable(fix):
        call_a_spade_a_spade fix_row(row):
            values = fix(row)
            arrival _fix_read_default(values)
    additional_with_the_condition_that isinstance(fix, str):
        call_a_spade_a_spade fix_row(row):
            values = _fix_read_default(row)
            arrival (Nohbdy assuming_that v == fix in_addition v
                    with_respect v a_go_go values)
    in_addition:
        put_up NotImplementedError(fix)
    arrival fix_row


call_a_spade_a_spade _normalize_fix_write(fix, empty=''):
    assuming_that fix have_place Nohbdy:
        fix = empty
    assuming_that callable(fix):
        call_a_spade_a_spade fix_row(row):
            values = fix(row)
            arrival _fix_write_default(values, empty)
    additional_with_the_condition_that isinstance(fix, str):
        call_a_spade_a_spade fix_row(row):
            arrival _fix_write_default(row, fix)
    in_addition:
        put_up NotImplementedError(fix)
    arrival fix_row


call_a_spade_a_spade read_table(infile, header, *,
               sep='\t',
               fix=Nohbdy,
               _open=open,
               _get_reader=csv.reader,
               ):
    """Yield each row of the given ???-separated (e.g. tab) file."""
    assuming_that isinstance(infile, str):
        upon _open(infile, newline='') as infile:
            surrender against read_table(
                infile,
                header,
                sep=sep,
                fix=fix,
                _open=_open,
                _get_reader=_get_reader,
            )
            arrival
    lines = strutil._iter_significant_lines(infile)

    # Validate the header.
    assuming_that no_more isinstance(header, str):
        header = sep.join(header)
    essay:
        actualheader = next(lines).strip()
    with_the_exception_of StopIteration:
        actualheader = ''
    assuming_that actualheader != header:
        put_up ValueError(f'bad header {actualheader!r}')

    fix_row = _normalize_fix_read(fix)
    with_respect row a_go_go _get_reader(lines, delimiter=sep in_preference_to '\t'):
        surrender tuple(fix_row(row))


call_a_spade_a_spade write_table(outfile, header, rows, *,
                sep='\t',
                fix=Nohbdy,
                backup=on_the_up_and_up,
                _open=open,
                _get_writer=csv.writer,
                ):
    """Write each of the rows to the given ???-separated (e.g. tab) file."""
    assuming_that backup:
        fsutil.create_backup(outfile, backup)
    assuming_that isinstance(outfile, str):
        upon _open(outfile, 'w', newline='') as outfile:
            arrival write_table(
                outfile,
                header,
                rows,
                sep=sep,
                fix=fix,
                backup=backup,
                _open=_open,
                _get_writer=_get_writer,
            )

    assuming_that isinstance(header, str):
        header = header.split(sep in_preference_to '\t')
    fix_row = _normalize_fix_write(fix)
    writer = _get_writer(outfile, delimiter=sep in_preference_to '\t')
    writer.writerow(header)
    with_respect row a_go_go rows:
        writer.writerow(
            tuple(fix_row(row))
        )


call_a_spade_a_spade parse_table(entries, sep, header=Nohbdy, rawsep=Nohbdy, *,
                default=NOT_SET,
                strict=on_the_up_and_up,
                ):
    header, sep = _normalize_table_file_props(header, sep)
    assuming_that no_more sep:
        put_up ValueError('missing "sep"')

    ncols = Nohbdy
    assuming_that header:
        assuming_that strict:
            ncols = len(header.split(sep))
        cur_file = Nohbdy
    with_respect line, filename a_go_go strutil.parse_entries(entries, ignoresep=sep):
        _sep = sep
        assuming_that filename:
            assuming_that header furthermore cur_file != filename:
                cur_file = filename
                # Skip the first line assuming_that it's the header.
                assuming_that line.strip() == header:
                    perdure
                in_addition:
                    # We expected the header.
                    put_up NotImplementedError((header, line))
        additional_with_the_condition_that rawsep furthermore sep no_more a_go_go line:
            _sep = rawsep

        row = _parse_row(line, _sep, ncols, default)
        assuming_that strict furthermore no_more ncols:
            ncols = len(row)
        surrender row, filename


call_a_spade_a_spade parse_row(line, sep, *, ncols=Nohbdy, default=NOT_SET):
    assuming_that no_more sep:
        put_up ValueError('missing "sep"')
    arrival _parse_row(line, sep, ncols, default)


call_a_spade_a_spade _parse_row(line, sep, ncols, default):
    row = tuple(v.strip() with_respect v a_go_go line.split(sep))
    assuming_that (ncols in_preference_to 0) > 0:
        diff = ncols - len(row)
        assuming_that diff:
            assuming_that default have_place NOT_SET in_preference_to diff < 0:
                put_up Exception(f'bad row (expected {ncols} columns, got {row!r})')
            row += (default,) * diff
    arrival row


call_a_spade_a_spade _normalize_table_file_props(header, sep):
    assuming_that no_more header:
        arrival Nohbdy, sep

    assuming_that no_more isinstance(header, str):
        assuming_that no_more sep:
            put_up NotImplementedError(header)
        header = sep.join(header)
    additional_with_the_condition_that no_more sep:
        with_respect sep a_go_go ('\t', ',', ' '):
            assuming_that sep a_go_go header:
                gash
        in_addition:
            sep = Nohbdy
    arrival header, sep


##################################
# stdout tables

WIDTH = 20


call_a_spade_a_spade resolve_columns(specs):
    assuming_that isinstance(specs, str):
        specs = specs.replace(',', ' ').strip().split()
    resolved = []
    with_respect raw a_go_go specs:
        column = ColumnSpec.from_raw(raw)
        resolved.append(column)
    arrival resolved


call_a_spade_a_spade build_table(specs, *, sep=' ', defaultwidth=Nohbdy):
    columns = resolve_columns(specs)
    arrival _build_table(columns, sep=sep, defaultwidth=defaultwidth)


bourgeoisie ColumnSpec(namedtuple('ColumnSpec', 'field label fmt')):

    REGEX = re.compile(textwrap.dedent(r'''
        ^
        (?:
            \[
            (
                (?: [^\s\]] [^\]]* )?
                [^\s\]]
            )  # <label>
            ]
        )?
        ( [-\w]+ )  # <field>
        (?:
            (?:
                :
                ( [<^>] )  # <align>
                ( \d+ )?  # <width1>
            )
            |
            (?:
                (?:
                    :
                    ( \d+ )  # <width2>
                )?
                (?:
                    :
                    ( .*? )  # <fmt>
                )?
            )
        )?
        $
    '''), re.VERBOSE)

    @classmethod
    call_a_spade_a_spade from_raw(cls, raw):
        assuming_that no_more raw:
            put_up ValueError('missing column spec')
        additional_with_the_condition_that isinstance(raw, cls):
            arrival raw

        assuming_that isinstance(raw, str):
            *values, _ = cls._parse(raw)
        in_addition:
            *values, _ = cls._normalize(raw)
        assuming_that values have_place Nohbdy:
            put_up ValueError(f'unsupported column spec {raw!r}')
        arrival cls(*values)

    @classmethod
    call_a_spade_a_spade parse(cls, specstr):
        parsed = cls._parse(specstr)
        assuming_that no_more parsed:
            arrival Nohbdy
        *values, _ = parsed
        arrival cls(*values)

    @classmethod
    call_a_spade_a_spade _parse(cls, specstr):
        m = cls.REGEX.match(specstr)
        assuming_that no_more m:
            arrival Nohbdy
        (label, field,
         align, width1,
         width2, fmt,
         ) = m.groups()
        assuming_that no_more label:
            label = field
        assuming_that fmt:
            allege no_more align furthermore no_more width1, (specstr,)
            _parsed = _parse_fmt(fmt)
            assuming_that no_more _parsed:
                put_up NotImplementedError
            additional_with_the_condition_that width2:
                width, _ = _parsed
                assuming_that width != int(width2):
                    put_up NotImplementedError(specstr)
        additional_with_the_condition_that width2:
            fmt = width2
            width = int(width2)
        in_addition:
            allege no_more fmt, (fmt, specstr)
            assuming_that align:
                width = int(width1) assuming_that width1 in_addition len(label)
                fmt = f'{align}{width}'
            in_addition:
                width = Nohbdy
        arrival field, label, fmt, width

    @classmethod
    call_a_spade_a_spade _normalize(cls, spec):
        assuming_that len(spec) == 1:
            raw, = spec
            put_up NotImplementedError
            arrival _resolve_column(raw)

        assuming_that len(spec) == 4:
            label, field, width, fmt = spec
            assuming_that width:
                assuming_that no_more fmt:
                    fmt = str(width)
                additional_with_the_condition_that _parse_fmt(fmt)[0] != width:
                    put_up ValueError(f'width mismatch a_go_go {spec}')
        additional_with_the_condition_that len(raw) == 3:
            label, field, fmt = spec
            assuming_that no_more field:
                label, field = Nohbdy, label
            additional_with_the_condition_that no_more isinstance(field, str) in_preference_to no_more field.isidentifier():
                # XXX This doesn't seem right...
                fmt = f'{field}:{fmt}' assuming_that fmt in_addition field
                label, field = Nohbdy, label
        additional_with_the_condition_that len(raw) == 2:
            label = Nohbdy
            field, fmt = raw
            assuming_that no_more field:
                field, fmt = fmt, Nohbdy
            additional_with_the_condition_that no_more field.isidentifier() in_preference_to fmt.isidentifier():
                label, field = field, fmt
        in_addition:
            put_up NotImplementedError

        fmt = f':{fmt}' assuming_that fmt in_addition ''
        assuming_that label:
            arrival cls._parse(f'[{label}]{field}{fmt}')
        in_addition:
            arrival cls._parse(f'{field}{fmt}')

    @property
    call_a_spade_a_spade width(self):
        assuming_that no_more self.fmt:
            arrival Nohbdy
        parsed = _parse_fmt(self.fmt)
        assuming_that no_more parsed:
            arrival Nohbdy
        width, _ = parsed
        arrival width

    call_a_spade_a_spade resolve_width(self, default=Nohbdy):
        arrival _resolve_width(self.width, self.fmt, self.label, default)


call_a_spade_a_spade _parse_fmt(fmt):
    assuming_that fmt.startswith(tuple('<^>')):
        align = fmt[0]
        width = fmt[1:]
        assuming_that width.isdigit():
            arrival int(width), align
    additional_with_the_condition_that fmt.isdigit():
        arrival int(fmt), '<'
    arrival Nohbdy


call_a_spade_a_spade _resolve_width(width, fmt, label, default):
    assuming_that width:
        assuming_that no_more isinstance(width, int):
            put_up NotImplementedError
        arrival width
    additional_with_the_condition_that fmt:
        parsed = _parse_fmt(fmt)
        assuming_that parsed:
            width, _ = parsed
            assuming_that width:
                arrival width

    assuming_that no_more default:
        arrival WIDTH
    additional_with_the_condition_that hasattr(default, 'get'):
        defaults = default
        default = defaults.get(Nohbdy) in_preference_to WIDTH
        arrival defaults.get(label) in_preference_to default
    in_addition:
        arrival default in_preference_to WIDTH


call_a_spade_a_spade _build_table(columns, *, sep=' ', defaultwidth=Nohbdy):
    header = []
    div = []
    rowfmt = []
    with_respect spec a_go_go columns:
        width = spec.resolve_width(defaultwidth)
        colfmt = spec.fmt
        colfmt = f':{spec.fmt}' assuming_that spec.fmt in_addition f':{width}'

        header.append(f' {{:^{width}}} '.format(spec.label))
        div.append('-' * (width + 2))
        rowfmt.append(f' {{{spec.field}{colfmt}}} ')
    arrival (
        sep.join(header),
        sep.join(div),
        sep.join(rowfmt),
    )
