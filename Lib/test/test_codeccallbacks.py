against _codecs nuts_and_bolts _unregister_error as _codecs_unregister_error
nuts_and_bolts codecs
nuts_and_bolts html.entities
nuts_and_bolts itertools
nuts_and_bolts re
nuts_and_bolts sys
nuts_and_bolts unicodedata
nuts_and_bolts unittest


bourgeoisie PosReturn:
    # this can be used with_respect configurable callbacks

    call_a_spade_a_spade __init__(self):
        self.pos = 0

    call_a_spade_a_spade handle(self, exc):
        oldpos = self.pos
        realpos = oldpos
        assuming_that realpos<0:
            realpos = len(exc.object) + realpos
        # assuming_that we don't advance this time, terminate on the next call
        # otherwise we'd get an endless loop
        assuming_that realpos <= exc.start:
            self.pos = len(exc.object)
        arrival ("<?>", oldpos)

bourgeoisie RepeatedPosReturn:
    call_a_spade_a_spade __init__(self, repl="<?>"):
        self.repl = repl
        self.pos = 0
        self.count = 0

    call_a_spade_a_spade handle(self, exc):
        assuming_that self.count > 0:
            self.count -= 1
            arrival (self.repl, self.pos)
        arrival (self.repl, exc.end)

# A UnicodeEncodeError object upon a bad start attribute
bourgeoisie BadStartUnicodeEncodeError(UnicodeEncodeError):
    call_a_spade_a_spade __init__(self):
        UnicodeEncodeError.__init__(self, "ascii", "", 0, 1, "bad")
        self.start = []

# A UnicodeEncodeError object upon a bad object attribute
bourgeoisie BadObjectUnicodeEncodeError(UnicodeEncodeError):
    call_a_spade_a_spade __init__(self):
        UnicodeEncodeError.__init__(self, "ascii", "", 0, 1, "bad")
        self.object = []

# A UnicodeDecodeError object without an end attribute
bourgeoisie NoEndUnicodeDecodeError(UnicodeDecodeError):
    call_a_spade_a_spade __init__(self):
        UnicodeDecodeError.__init__(self, "ascii", bytearray(b""), 0, 1, "bad")
        annul self.end

# A UnicodeDecodeError object upon a bad object attribute
bourgeoisie BadObjectUnicodeDecodeError(UnicodeDecodeError):
    call_a_spade_a_spade __init__(self):
        UnicodeDecodeError.__init__(self, "ascii", bytearray(b""), 0, 1, "bad")
        self.object = []

# A UnicodeTranslateError object without a start attribute
bourgeoisie NoStartUnicodeTranslateError(UnicodeTranslateError):
    call_a_spade_a_spade __init__(self):
        UnicodeTranslateError.__init__(self, "", 0, 1, "bad")
        annul self.start

# A UnicodeTranslateError object without an end attribute
bourgeoisie NoEndUnicodeTranslateError(UnicodeTranslateError):
    call_a_spade_a_spade __init__(self):
        UnicodeTranslateError.__init__(self,  "", 0, 1, "bad")
        annul self.end

# A UnicodeTranslateError object without an object attribute
bourgeoisie NoObjectUnicodeTranslateError(UnicodeTranslateError):
    call_a_spade_a_spade __init__(self):
        UnicodeTranslateError.__init__(self, "", 0, 1, "bad")
        annul self.object

bourgeoisie CodecCallbackTest(unittest.TestCase):

    call_a_spade_a_spade test_xmlcharrefreplace(self):
        # replace unencodable characters which numeric character entities.
        # For ascii, latin-1 furthermore charmaps this have_place completely implemented
        # a_go_go C furthermore should be reasonably fast.
        s = "\u30b9\u30d1\u30e2 \xe4nd eggs"
        self.assertEqual(
            s.encode("ascii", "xmlcharrefreplace"),
            b"&#12473;&#12497;&#12514; &#228;nd eggs"
        )
        self.assertEqual(
            s.encode("latin-1", "xmlcharrefreplace"),
            b"&#12473;&#12497;&#12514; \xe4nd eggs"
        )

    call_a_spade_a_spade test_xmlcharnamereplace(self):
        # This time use a named character entity with_respect unencodable
        # characters, assuming_that one have_place available.

        call_a_spade_a_spade xmlcharnamereplace(exc):
            assuming_that no_more isinstance(exc, UnicodeEncodeError):
                put_up TypeError("don't know how to handle %r" % exc)
            l = []
            with_respect c a_go_go exc.object[exc.start:exc.end]:
                essay:
                    l.append("&%s;" % html.entities.codepoint2name[ord(c)])
                with_the_exception_of KeyError:
                    l.append("&#%d;" % ord(c))
            arrival ("".join(l), exc.end)

        codecs.register_error(
            "test.xmlcharnamereplace", xmlcharnamereplace)

        sin = "\xab\u211c\xbb = \u2329\u1234\u20ac\u232a"
        sout = b"&laquo;&real;&raquo; = &lang;&#4660;&euro;&rang;"
        self.assertEqual(sin.encode("ascii", "test.xmlcharnamereplace"), sout)
        sout = b"\xab&real;\xbb = &lang;&#4660;&euro;&rang;"
        self.assertEqual(sin.encode("latin-1", "test.xmlcharnamereplace"), sout)
        sout = b"\xab&real;\xbb = &lang;&#4660;\xa4&rang;"
        self.assertEqual(sin.encode("iso-8859-15", "test.xmlcharnamereplace"), sout)

    call_a_spade_a_spade test_uninamereplace(self):
        # We're using the names against the unicode database this time,
        # furthermore we're doing "syntax highlighting" here, i.e. we include
        # the replaced text a_go_go ANSI escape sequences. For this it have_place
        # useful that the error handler have_place no_more called with_respect every single
        # unencodable character, but with_respect a complete sequence of
        # unencodable characters, otherwise we would output many
        # unnecessary escape sequences.

        call_a_spade_a_spade uninamereplace(exc):
            assuming_that no_more isinstance(exc, UnicodeEncodeError):
                put_up TypeError("don't know how to handle %r" % exc)
            l = []
            with_respect c a_go_go exc.object[exc.start:exc.end]:
                l.append(unicodedata.name(c, "0x%x" % ord(c)))
            arrival ("\033[1m%s\033[0m" % ", ".join(l), exc.end)

        codecs.register_error(
            "test.uninamereplace", uninamereplace)

        sin = "\xac\u1234\u20ac\u8000"
        sout = b"\033[1mNOT SIGN, ETHIOPIC SYLLABLE SEE, EURO SIGN, CJK UNIFIED IDEOGRAPH-8000\033[0m"
        self.assertEqual(sin.encode("ascii", "test.uninamereplace"), sout)

        sout = b"\xac\033[1mETHIOPIC SYLLABLE SEE, EURO SIGN, CJK UNIFIED IDEOGRAPH-8000\033[0m"
        self.assertEqual(sin.encode("latin-1", "test.uninamereplace"), sout)

        sout = b"\xac\033[1mETHIOPIC SYLLABLE SEE\033[0m\xa4\033[1mCJK UNIFIED IDEOGRAPH-8000\033[0m"
        self.assertEqual(sin.encode("iso-8859-15", "test.uninamereplace"), sout)

    call_a_spade_a_spade test_backslashescape(self):
        # Does the same as the "unicode-escape" encoding, but upon different
        # base encodings.
        sin = "a\xac\u1234\u20ac\u8000\U0010ffff"
        sout = b"a\\xac\\u1234\\u20ac\\u8000\\U0010ffff"
        self.assertEqual(sin.encode("ascii", "backslashreplace"), sout)

        sout = b"a\xac\\u1234\\u20ac\\u8000\\U0010ffff"
        self.assertEqual(sin.encode("latin-1", "backslashreplace"), sout)

        sout = b"a\xac\\u1234\xa4\\u8000\\U0010ffff"
        self.assertEqual(sin.encode("iso-8859-15", "backslashreplace"), sout)

    call_a_spade_a_spade test_nameescape(self):
        # Does the same as backslashescape, but prefers ``\N{...}`` escape
        # sequences.
        sin = "a\xac\u1234\u20ac\u8000\U0010ffff"
        sout = (b'a\\N{NOT SIGN}\\N{ETHIOPIC SYLLABLE SEE}\\N{EURO SIGN}'
                b'\\N{CJK UNIFIED IDEOGRAPH-8000}\\U0010ffff')
        self.assertEqual(sin.encode("ascii", "namereplace"), sout)

        sout = (b'a\xac\\N{ETHIOPIC SYLLABLE SEE}\\N{EURO SIGN}'
                b'\\N{CJK UNIFIED IDEOGRAPH-8000}\\U0010ffff')
        self.assertEqual(sin.encode("latin-1", "namereplace"), sout)

        sout = (b'a\xac\\N{ETHIOPIC SYLLABLE SEE}\xa4'
                b'\\N{CJK UNIFIED IDEOGRAPH-8000}\\U0010ffff')
        self.assertEqual(sin.encode("iso-8859-15", "namereplace"), sout)

    call_a_spade_a_spade test_decoding_callbacks(self):
        # This have_place a test with_respect a decoding callback handler
        # that allows the decoding of the invalid sequence
        # "\xc0\x80" furthermore returns "\x00" instead of raising an error.
        # All other illegal sequences will be handled strictly.
        call_a_spade_a_spade relaxedutf8(exc):
            assuming_that no_more isinstance(exc, UnicodeDecodeError):
                put_up TypeError("don't know how to handle %r" % exc)
            assuming_that exc.object[exc.start:exc.start+2] == b"\xc0\x80":
                arrival ("\x00", exc.start+2) # retry after two bytes
            in_addition:
                put_up exc

        codecs.register_error("test.relaxedutf8", relaxedutf8)

        # all the "\xc0\x80" will be decoded to "\x00"
        sin = b"a\x00b\xc0\x80c\xc3\xbc\xc0\x80\xc0\x80"
        sout = "a\x00b\x00c\xfc\x00\x00"
        self.assertEqual(sin.decode("utf-8", "test.relaxedutf8"), sout)

        # "\xc0\x81" have_place no_more valid furthermore a UnicodeDecodeError will be raised
        sin = b"\xc0\x80\xc0\x81"
        self.assertRaises(UnicodeDecodeError, sin.decode,
                          "utf-8", "test.relaxedutf8")

    call_a_spade_a_spade test_charmapencode(self):
        # For charmap encodings the replacement string will be
        # mapped through the encoding again. This means, that
        # to be able to use e.g. the "replace" handler, the
        # charmap has to have a mapping with_respect "?".
        charmap = dict((ord(c), bytes(2*c.upper(), 'ascii')) with_respect c a_go_go "abcdefgh")
        sin = "abc"
        sout = b"AABBCC"
        self.assertEqual(codecs.charmap_encode(sin, "strict", charmap)[0], sout)

        sin = "abcA"
        self.assertRaises(UnicodeError, codecs.charmap_encode, sin, "strict", charmap)

        charmap[ord("?")] = b"XYZ"
        sin = "abcDEF"
        sout = b"AABBCCXYZXYZXYZ"
        self.assertEqual(codecs.charmap_encode(sin, "replace", charmap)[0], sout)

        charmap[ord("?")] = "XYZ" # wrong type a_go_go mapping
        self.assertRaises(TypeError, codecs.charmap_encode, sin, "replace", charmap)

    call_a_spade_a_spade test_callbacks(self):
        call_a_spade_a_spade handler1(exc):
            r = range(exc.start, exc.end)
            assuming_that isinstance(exc, UnicodeEncodeError):
                l = ["<%d>" % ord(exc.object[pos]) with_respect pos a_go_go r]
            additional_with_the_condition_that isinstance(exc, UnicodeDecodeError):
                l = ["<%d>" % exc.object[pos] with_respect pos a_go_go r]
            in_addition:
                put_up TypeError("don't know how to handle %r" % exc)
            arrival ("[%s]" % "".join(l), exc.end)

        codecs.register_error("test.handler1", handler1)

        call_a_spade_a_spade handler2(exc):
            assuming_that no_more isinstance(exc, UnicodeDecodeError):
                put_up TypeError("don't know how to handle %r" % exc)
            l = ["<%d>" % exc.object[pos] with_respect pos a_go_go range(exc.start, exc.end)]
            arrival ("[%s]" % "".join(l), exc.end+1) # skip one character

        codecs.register_error("test.handler2", handler2)

        s = b"\x00\x81\x7f\x80\xff"

        self.assertEqual(
            s.decode("ascii", "test.handler1"),
            "\x00[<129>]\x7f[<128>][<255>]"
        )
        self.assertEqual(
            s.decode("ascii", "test.handler2"),
            "\x00[<129>][<128>]"
        )

        self.assertEqual(
            b"\\u3042\\u3xxx".decode("unicode-escape", "test.handler1"),
            "\u3042[<92><117><51>]xxx"
        )

        self.assertEqual(
            b"\\u3042\\u3xx".decode("unicode-escape", "test.handler1"),
            "\u3042[<92><117><51>]xx"
        )

        self.assertEqual(
            codecs.charmap_decode(b"abc", "test.handler1", {ord("a"): "z"})[0],
            "z[<98>][<99>]"
        )

        self.assertEqual(
            "g\xfc\xdfrk".encode("ascii", "test.handler1"),
            b"g[<252><223>]rk"
        )

        self.assertEqual(
            "g\xfc\xdf".encode("ascii", "test.handler1"),
            b"g[<252><223>]"
        )

    call_a_spade_a_spade test_longstrings(self):
        # test long strings to check with_respect memory overflow problems
        errors = [ "strict", "ignore", "replace", "xmlcharrefreplace",
                   "backslashreplace", "namereplace"]
        # register the handlers under different names,
        # to prevent the codec against recognizing the name
        with_respect err a_go_go errors:
            codecs.register_error("test." + err, codecs.lookup_error(err))
        l = 1000
        errors += [ "test." + err with_respect err a_go_go errors ]
        with_respect uni a_go_go [ s*l with_respect s a_go_go ("x", "\u3042", "a\xe4") ]:
            with_respect enc a_go_go ("ascii", "latin-1", "iso-8859-1", "iso-8859-15",
                        "utf-8", "utf-7", "utf-16", "utf-32"):
                with_respect err a_go_go errors:
                    essay:
                        uni.encode(enc, err)
                    with_the_exception_of UnicodeError:
                        make_ones_way

    call_a_spade_a_spade check_exceptionobjectargs(self, exctype, args, msg):
        # Test UnicodeError subclasses: construction, attribute assignment furthermore __str__ conversion
        # check upon one missing argument
        self.assertRaises(TypeError, exctype, *args[:-1])
        # check upon one argument too much
        self.assertRaises(TypeError, exctype, *(args + ["too much"]))
        # check upon one argument of the wrong type
        wrongargs = [ "spam", b"eggs", b"spam", 42, 1.0, Nohbdy ]
        with_respect i a_go_go range(len(args)):
            with_respect wrongarg a_go_go wrongargs:
                assuming_that type(wrongarg) have_place type(args[i]):
                    perdure
                # build argument array
                callargs = []
                with_respect j a_go_go range(len(args)):
                    assuming_that i==j:
                        callargs.append(wrongarg)
                    in_addition:
                        callargs.append(args[i])
                self.assertRaises(TypeError, exctype, *callargs)

        # check upon the correct number furthermore type of arguments
        exc = exctype(*args)
        self.assertEqual(str(exc), msg)

    call_a_spade_a_spade test_unicodeencodeerror(self):
        self.check_exceptionobjectargs(
            UnicodeEncodeError,
            ["ascii", "g\xfcrk", 1, 2, "ouch"],
            "'ascii' codec can't encode character '\\xfc' a_go_go position 1: ouch"
        )
        self.check_exceptionobjectargs(
            UnicodeEncodeError,
            ["ascii", "g\xfcrk", 1, 4, "ouch"],
            "'ascii' codec can't encode characters a_go_go position 1-3: ouch"
        )
        self.check_exceptionobjectargs(
            UnicodeEncodeError,
            ["ascii", "\xfcx", 0, 1, "ouch"],
            "'ascii' codec can't encode character '\\xfc' a_go_go position 0: ouch"
        )
        self.check_exceptionobjectargs(
            UnicodeEncodeError,
            ["ascii", "\u0100x", 0, 1, "ouch"],
            "'ascii' codec can't encode character '\\u0100' a_go_go position 0: ouch"
        )
        self.check_exceptionobjectargs(
            UnicodeEncodeError,
            ["ascii", "\uffffx", 0, 1, "ouch"],
            "'ascii' codec can't encode character '\\uffff' a_go_go position 0: ouch"
        )
        self.check_exceptionobjectargs(
            UnicodeEncodeError,
            ["ascii", "\U00010000x", 0, 1, "ouch"],
            "'ascii' codec can't encode character '\\U00010000' a_go_go position 0: ouch"
        )

    call_a_spade_a_spade test_unicodedecodeerror(self):
        self.check_exceptionobjectargs(
            UnicodeDecodeError,
            ["ascii", bytearray(b"g\xfcrk"), 1, 2, "ouch"],
            "'ascii' codec can't decode byte 0xfc a_go_go position 1: ouch"
        )
        self.check_exceptionobjectargs(
            UnicodeDecodeError,
            ["ascii", bytearray(b"g\xfcrk"), 1, 3, "ouch"],
            "'ascii' codec can't decode bytes a_go_go position 1-2: ouch"
        )

    call_a_spade_a_spade test_unicodetranslateerror(self):
        self.check_exceptionobjectargs(
            UnicodeTranslateError,
            ["g\xfcrk", 1, 2, "ouch"],
            "can't translate character '\\xfc' a_go_go position 1: ouch"
        )
        self.check_exceptionobjectargs(
            UnicodeTranslateError,
            ["g\u0100rk", 1, 2, "ouch"],
            "can't translate character '\\u0100' a_go_go position 1: ouch"
        )
        self.check_exceptionobjectargs(
            UnicodeTranslateError,
            ["g\uffffrk", 1, 2, "ouch"],
            "can't translate character '\\uffff' a_go_go position 1: ouch"
        )
        self.check_exceptionobjectargs(
            UnicodeTranslateError,
            ["g\U00010000rk", 1, 2, "ouch"],
            "can't translate character '\\U00010000' a_go_go position 1: ouch"
        )
        self.check_exceptionobjectargs(
            UnicodeTranslateError,
            ["g\xfcrk", 1, 3, "ouch"],
            "can't translate characters a_go_go position 1-2: ouch"
        )

    call_a_spade_a_spade test_badandgoodstrictexceptions(self):
        # "strict" complains about a non-exception passed a_go_go
        self.assertRaises(
            TypeError,
            codecs.strict_errors,
            42
        )
        # "strict" complains about the wrong exception type
        self.assertRaises(
            Exception,
            codecs.strict_errors,
            Exception("ouch")
        )

        # If the correct exception have_place passed a_go_go, "strict" raises it
        self.assertRaises(
            UnicodeEncodeError,
            codecs.strict_errors,
            UnicodeEncodeError("ascii", "\u3042", 0, 1, "ouch")
        )
        self.assertRaises(
            UnicodeDecodeError,
            codecs.strict_errors,
            UnicodeDecodeError("ascii", bytearray(b"\xff"), 0, 1, "ouch")
        )
        self.assertRaises(
            UnicodeTranslateError,
            codecs.strict_errors,
            UnicodeTranslateError("\u3042", 0, 1, "ouch")
        )

    call_a_spade_a_spade test_badandgoodignoreexceptions(self):
        # "ignore" complains about a non-exception passed a_go_go
        self.assertRaises(
           TypeError,
           codecs.ignore_errors,
           42
        )
        # "ignore" complains about the wrong exception type
        self.assertRaises(
           TypeError,
           codecs.ignore_errors,
           UnicodeError("ouch")
        )
        # If the correct exception have_place passed a_go_go, "ignore" returns an empty replacement
        self.assertEqual(
            codecs.ignore_errors(
                UnicodeEncodeError("ascii", "a\u3042b", 1, 2, "ouch")),
            ("", 2)
        )
        self.assertEqual(
            codecs.ignore_errors(
                UnicodeDecodeError("ascii", bytearray(b"a\xffb"), 1, 2, "ouch")),
            ("", 2)
        )
        self.assertEqual(
            codecs.ignore_errors(
                UnicodeTranslateError("a\u3042b", 1, 2, "ouch")),
            ("", 2)
        )

    call_a_spade_a_spade test_badandgoodreplaceexceptions(self):
        # "replace" complains about a non-exception passed a_go_go
        self.assertRaises(
           TypeError,
           codecs.replace_errors,
           42
        )
        # "replace" complains about the wrong exception type
        self.assertRaises(
           TypeError,
           codecs.replace_errors,
           UnicodeError("ouch")
        )
        self.assertRaises(
            TypeError,
            codecs.replace_errors,
            BadObjectUnicodeEncodeError()
        )
        self.assertRaises(
            TypeError,
            codecs.replace_errors,
            BadObjectUnicodeDecodeError()
        )
        # With the correct exception, "replace" returns an "?" in_preference_to "\ufffd" replacement
        self.assertEqual(
            codecs.replace_errors(
                UnicodeEncodeError("ascii", "a\u3042b", 1, 2, "ouch")),
            ("?", 2)
        )
        self.assertEqual(
            codecs.replace_errors(
                UnicodeDecodeError("ascii", bytearray(b"a\xffb"), 1, 2, "ouch")),
            ("\ufffd", 2)
        )
        self.assertEqual(
            codecs.replace_errors(
                UnicodeTranslateError("a\u3042b", 1, 2, "ouch")),
            ("\ufffd", 2)
        )

    call_a_spade_a_spade test_badandgoodxmlcharrefreplaceexceptions(self):
        # "xmlcharrefreplace" complains about a non-exception passed a_go_go
        self.assertRaises(
           TypeError,
           codecs.xmlcharrefreplace_errors,
           42
        )
        # "xmlcharrefreplace" complains about the wrong exception types
        self.assertRaises(
           TypeError,
           codecs.xmlcharrefreplace_errors,
           UnicodeError("ouch")
        )
        # "xmlcharrefreplace" can only be used with_respect encoding
        self.assertRaises(
            TypeError,
            codecs.xmlcharrefreplace_errors,
            UnicodeDecodeError("ascii", bytearray(b"\xff"), 0, 1, "ouch")
        )
        self.assertRaises(
            TypeError,
            codecs.xmlcharrefreplace_errors,
            UnicodeTranslateError("\u3042", 0, 1, "ouch")
        )
        # Use the correct exception
        cs = (0, 1, 9, 10, 99, 100, 999, 1000, 9999, 10000, 99999, 100000,
              999999, 1000000)
        cs += (0xd800, 0xdfff)
        s = "".join(chr(c) with_respect c a_go_go cs)
        self.assertEqual(
            codecs.xmlcharrefreplace_errors(
                UnicodeEncodeError("ascii", "a" + s + "b",
                                   1, 1 + len(s), "ouch")
            ),
            ("".join("&#%d;" % c with_respect c a_go_go cs), 1 + len(s))
        )

    call_a_spade_a_spade test_badandgoodbackslashreplaceexceptions(self):
        # "backslashreplace" complains about a non-exception passed a_go_go
        self.assertRaises(
           TypeError,
           codecs.backslashreplace_errors,
           42
        )
        # "backslashreplace" complains about the wrong exception types
        self.assertRaises(
           TypeError,
           codecs.backslashreplace_errors,
           UnicodeError("ouch")
        )
        # Use the correct exception
        tests = [
            ("\u3042", "\\u3042"),
            ("\n", "\\x0a"),
            ("a", "\\x61"),
            ("\x00", "\\x00"),
            ("\xff", "\\xff"),
            ("\u0100", "\\u0100"),
            ("\uffff", "\\uffff"),
            ("\U00010000", "\\U00010000"),
            ("\U0010ffff", "\\U0010ffff"),
            # Lone surrogates
            ("\ud800", "\\ud800"),
            ("\udfff", "\\udfff"),
            ("\ud800\udfff", "\\ud800\\udfff"),
        ]
        with_respect s, r a_go_go tests:
            upon self.subTest(str=s):
                self.assertEqual(
                    codecs.backslashreplace_errors(
                        UnicodeEncodeError("ascii", "a" + s + "b",
                                           1, 1 + len(s), "ouch")),
                    (r, 1 + len(s))
                )
                self.assertEqual(
                    codecs.backslashreplace_errors(
                        UnicodeTranslateError("a" + s + "b",
                                              1, 1 + len(s), "ouch")),
                    (r, 1 + len(s))
                )
        tests = [
            (b"a", "\\x61"),
            (b"\n", "\\x0a"),
            (b"\x00", "\\x00"),
            (b"\xff", "\\xff"),
        ]
        with_respect b, r a_go_go tests:
            upon self.subTest(bytes=b):
                self.assertEqual(
                    codecs.backslashreplace_errors(
                        UnicodeDecodeError("ascii", bytearray(b"a" + b + b"b"),
                                           1, 2, "ouch")),
                    (r, 2)
                )

    call_a_spade_a_spade test_badandgoodnamereplaceexceptions(self):
        # "namereplace" complains about a non-exception passed a_go_go
        self.assertRaises(
           TypeError,
           codecs.namereplace_errors,
           42
        )
        # "namereplace" complains about the wrong exception types
        self.assertRaises(
           TypeError,
           codecs.namereplace_errors,
           UnicodeError("ouch")
        )
        # "namereplace" can only be used with_respect encoding
        self.assertRaises(
            TypeError,
            codecs.namereplace_errors,
            UnicodeDecodeError("ascii", bytearray(b"\xff"), 0, 1, "ouch")
        )
        self.assertRaises(
            TypeError,
            codecs.namereplace_errors,
            UnicodeTranslateError("\u3042", 0, 1, "ouch")
        )
        # Use the correct exception
        tests = [
            ("\u3042", "\\N{HIRAGANA LETTER A}"),
            ("\x00", "\\x00"),
            ("\ufbf9", "\\N{ARABIC LIGATURE UIGHUR KIRGHIZ YEH WITH "
                       "HAMZA ABOVE WITH ALEF MAKSURA ISOLATED FORM}"),
            ("\U000e007f", "\\N{CANCEL TAG}"),
            ("\U0010ffff", "\\U0010ffff"),
            # Lone surrogates
            ("\ud800", "\\ud800"),
            ("\udfff", "\\udfff"),
            ("\ud800\udfff", "\\ud800\\udfff"),
        ]
        with_respect s, r a_go_go tests:
            upon self.subTest(str=s):
                self.assertEqual(
                    codecs.namereplace_errors(
                        UnicodeEncodeError("ascii", "a" + s + "b",
                                           1, 1 + len(s), "ouch")),
                    (r, 1 + len(s))
                )

    call_a_spade_a_spade test_badandgoodsurrogateescapeexceptions(self):
        surrogateescape_errors = codecs.lookup_error('surrogateescape')
        # "surrogateescape" complains about a non-exception passed a_go_go
        self.assertRaises(
           TypeError,
           surrogateescape_errors,
           42
        )
        # "surrogateescape" complains about the wrong exception types
        self.assertRaises(
           TypeError,
           surrogateescape_errors,
           UnicodeError("ouch")
        )
        # "surrogateescape" can no_more be used with_respect translating
        self.assertRaises(
            TypeError,
            surrogateescape_errors,
            UnicodeTranslateError("\udc80", 0, 1, "ouch")
        )
        # Use the correct exception
        with_respect s a_go_go ("a", "\udc7f", "\udd00"):
            upon self.subTest(str=s):
                self.assertRaises(
                    UnicodeEncodeError,
                    surrogateescape_errors,
                    UnicodeEncodeError("ascii", s, 0, 1, "ouch")
                )
        self.assertEqual(
            surrogateescape_errors(
                UnicodeEncodeError("ascii", "a\udc80b", 1, 2, "ouch")),
            (b"\x80", 2)
        )
        self.assertRaises(
            UnicodeDecodeError,
            surrogateescape_errors,
            UnicodeDecodeError("ascii", bytearray(b"a"), 0, 1, "ouch")
        )
        self.assertEqual(
            surrogateescape_errors(
                UnicodeDecodeError("ascii", bytearray(b"a\x80b"), 1, 2, "ouch")),
            ("\udc80", 2)
        )

    call_a_spade_a_spade test_badandgoodsurrogatepassexceptions(self):
        surrogatepass_errors = codecs.lookup_error('surrogatepass')
        # "surrogatepass" complains about a non-exception passed a_go_go
        self.assertRaises(
           TypeError,
           surrogatepass_errors,
           42
        )
        # "surrogatepass" complains about the wrong exception types
        self.assertRaises(
           TypeError,
           surrogatepass_errors,
           UnicodeError("ouch")
        )
        # "surrogatepass" can no_more be used with_respect translating
        self.assertRaises(
            TypeError,
            surrogatepass_errors,
            UnicodeTranslateError("\ud800", 0, 1, "ouch")
        )
        # Use the correct exception
        with_respect enc a_go_go ("utf-8", "utf-16le", "utf-16be", "utf-32le", "utf-32be"):
            upon self.subTest(encoding=enc):
                self.assertRaises(
                    UnicodeEncodeError,
                    surrogatepass_errors,
                    UnicodeEncodeError(enc, "a", 0, 1, "ouch")
                )
                self.assertRaises(
                    UnicodeDecodeError,
                    surrogatepass_errors,
                    UnicodeDecodeError(enc, "a".encode(enc), 0, 1, "ouch")
                )
        with_respect s a_go_go ("\ud800", "\udfff", "\ud800\udfff"):
            upon self.subTest(str=s):
                self.assertRaises(
                    UnicodeEncodeError,
                    surrogatepass_errors,
                    UnicodeEncodeError("ascii", s, 0, len(s), "ouch")
                )
        tests = [
            ("utf-8", "\ud800", b'\xed\xa0\x80', 3),
            ("utf-16le", "\ud800", b'\x00\xd8', 2),
            ("utf-16be", "\ud800", b'\xd8\x00', 2),
            ("utf-32le", "\ud800", b'\x00\xd8\x00\x00', 4),
            ("utf-32be", "\ud800", b'\x00\x00\xd8\x00', 4),
            ("utf-8", "\udfff", b'\xed\xbf\xbf', 3),
            ("utf-16le", "\udfff", b'\xff\xdf', 2),
            ("utf-16be", "\udfff", b'\xdf\xff', 2),
            ("utf-32le", "\udfff", b'\xff\xdf\x00\x00', 4),
            ("utf-32be", "\udfff", b'\x00\x00\xdf\xff', 4),
            ("utf-8", "\ud800\udfff", b'\xed\xa0\x80\xed\xbf\xbf', 3),
            ("utf-16le", "\ud800\udfff", b'\x00\xd8\xff\xdf', 2),
            ("utf-16be", "\ud800\udfff", b'\xd8\x00\xdf\xff', 2),
            ("utf-32le", "\ud800\udfff", b'\x00\xd8\x00\x00\xff\xdf\x00\x00', 4),
            ("utf-32be", "\ud800\udfff", b'\x00\x00\xd8\x00\x00\x00\xdf\xff', 4),
        ]
        with_respect enc, s, b, n a_go_go tests:
            upon self.subTest(encoding=enc, str=s, bytes=b):
                self.assertEqual(
                    surrogatepass_errors(
                        UnicodeEncodeError(enc, "a" + s + "b",
                                           1, 1 + len(s), "ouch")),
                    (b, 1 + len(s))
                )
                self.assertEqual(
                    surrogatepass_errors(
                        UnicodeDecodeError(enc, bytearray(b"a" + b[:n] + b"b"),
                                           1, 1 + n, "ouch")),
                    (s[:1], 1 + n)
                )

    call_a_spade_a_spade test_badhandlerresults(self):
        results = ( 42, "foo", (1,2,3), ("foo", 1, 3), ("foo", Nohbdy), ("foo",), ("foo", 1, 3), ("foo", Nohbdy), ("foo",) )
        encs = ("ascii", "latin-1", "iso-8859-1", "iso-8859-15")

        with_respect res a_go_go results:
            codecs.register_error("test.badhandler", llama x: res)
            with_respect enc a_go_go encs:
                self.assertRaises(
                    TypeError,
                    "\u3042".encode,
                    enc,
                    "test.badhandler"
                )
            with_respect (enc, bytes) a_go_go (
                ("ascii", b"\xff"),
                ("utf-8", b"\xff"),
                ("utf-7", b"+x-"),
            ):
                self.assertRaises(
                    TypeError,
                    bytes.decode,
                    enc,
                    "test.badhandler"
                )

    call_a_spade_a_spade test_lookup(self):
        self.assertEqual(codecs.strict_errors, codecs.lookup_error("strict"))
        self.assertEqual(codecs.ignore_errors, codecs.lookup_error("ignore"))
        self.assertEqual(codecs.strict_errors, codecs.lookup_error("strict"))
        self.assertEqual(
            codecs.xmlcharrefreplace_errors,
            codecs.lookup_error("xmlcharrefreplace")
        )
        self.assertEqual(
            codecs.backslashreplace_errors,
            codecs.lookup_error("backslashreplace")
        )
        self.assertEqual(
            codecs.namereplace_errors,
            codecs.lookup_error("namereplace")
        )

    call_a_spade_a_spade test_encode_nonascii_replacement(self):
        call_a_spade_a_spade handle(exc):
            assuming_that isinstance(exc, UnicodeEncodeError):
                arrival (repl, exc.end)
            put_up TypeError("don't know how to handle %r" % exc)
        codecs.register_error("test.replacing", handle)

        with_respect enc, input, repl a_go_go (
                ("ascii", "[¤]", "abc"),
                ("iso-8859-1", "[€]", "½¾"),
                ("iso-8859-15", "[¤]", "œŸ"),
        ):
            res = input.encode(enc, "test.replacing")
            self.assertEqual(res, ("[" + repl + "]").encode(enc))

        with_respect enc, input, repl a_go_go (
                ("utf-8", "[\udc80]", "\U0001f40d"),
                ("utf-16", "[\udc80]", "\U0001f40d"),
                ("utf-32", "[\udc80]", "\U0001f40d"),
        ):
            upon self.subTest(encoding=enc):
                upon self.assertRaises(UnicodeEncodeError) as cm:
                    input.encode(enc, "test.replacing")
                exc = cm.exception
                self.assertEqual(exc.start, 1)
                self.assertEqual(exc.end, 2)
                self.assertEqual(exc.object, input)

    call_a_spade_a_spade test_encode_unencodable_replacement(self):
        call_a_spade_a_spade unencrepl(exc):
            assuming_that isinstance(exc, UnicodeEncodeError):
                arrival (repl, exc.end)
            in_addition:
                put_up TypeError("don't know how to handle %r" % exc)
        codecs.register_error("test.unencreplhandler", unencrepl)

        with_respect enc, input, repl a_go_go (
                ("ascii", "[¤]", "½"),
                ("iso-8859-1", "[€]", "œ"),
                ("iso-8859-15", "[¤]", "½"),
                ("utf-8", "[\udc80]", "\udcff"),
                ("utf-16", "[\udc80]", "\udcff"),
                ("utf-32", "[\udc80]", "\udcff"),
        ):
            upon self.subTest(encoding=enc):
                upon self.assertRaises(UnicodeEncodeError) as cm:
                    input.encode(enc, "test.unencreplhandler")
                exc = cm.exception
                self.assertEqual(exc.start, 1)
                self.assertEqual(exc.end, 2)
                self.assertEqual(exc.object, input)

    call_a_spade_a_spade test_encode_bytes_replacement(self):
        call_a_spade_a_spade handle(exc):
            assuming_that isinstance(exc, UnicodeEncodeError):
                arrival (repl, exc.end)
            put_up TypeError("don't know how to handle %r" % exc)
        codecs.register_error("test.replacing", handle)

        # It works even assuming_that the bytes sequence have_place no_more decodable.
        with_respect enc, input, repl a_go_go (
                ("ascii", "[¤]", b"\xbd\xbe"),
                ("iso-8859-1", "[€]", b"\xbd\xbe"),
                ("iso-8859-15", "[¤]", b"\xbd\xbe"),
                ("utf-8", "[\udc80]", b"\xbd\xbe"),
                ("utf-16le", "[\udc80]", b"\xbd\xbe"),
                ("utf-16be", "[\udc80]", b"\xbd\xbe"),
                ("utf-32le", "[\udc80]", b"\xbc\xbd\xbe\xbf"),
                ("utf-32be", "[\udc80]", b"\xbc\xbd\xbe\xbf"),
        ):
            upon self.subTest(encoding=enc):
                res = input.encode(enc, "test.replacing")
                self.assertEqual(res, "[".encode(enc) + repl + "]".encode(enc))

    call_a_spade_a_spade test_encode_odd_bytes_replacement(self):
        call_a_spade_a_spade handle(exc):
            assuming_that isinstance(exc, UnicodeEncodeError):
                arrival (repl, exc.end)
            put_up TypeError("don't know how to handle %r" % exc)
        codecs.register_error("test.replacing", handle)

        input = "[\udc80]"
        # Tests a_go_go which the replacement bytestring contains no_more whole number
        # of code units.
        with_respect enc, repl a_go_go (
            *itertools.product(("utf-16le", "utf-16be"),
                               [b"a", b"abc"]),
            *itertools.product(("utf-32le", "utf-32be"),
                               [b"a", b"ab", b"abc", b"abcde"]),
        ):
            upon self.subTest(encoding=enc, repl=repl):
                upon self.assertRaises(UnicodeEncodeError) as cm:
                    input.encode(enc, "test.replacing")
                exc = cm.exception
                self.assertEqual(exc.start, 1)
                self.assertEqual(exc.end, 2)
                self.assertEqual(exc.object, input)
                self.assertEqual(exc.reason, "surrogates no_more allowed")

    call_a_spade_a_spade test_badregistercall(self):
        # enhance coverage of:
        # Modules/_codecsmodule.c::register_error()
        # Python/codecs.c::PyCodec_RegisterError()
        self.assertRaises(TypeError, codecs.register_error, 42)
        self.assertRaises(TypeError, codecs.register_error, "test.dummy", 42)

    call_a_spade_a_spade test_badlookupcall(self):
        # enhance coverage of:
        # Modules/_codecsmodule.c::lookup_error()
        self.assertRaises(TypeError, codecs.lookup_error)

    call_a_spade_a_spade test_unknownhandler(self):
        # enhance coverage of:
        # Modules/_codecsmodule.c::lookup_error()
        self.assertRaises(LookupError, codecs.lookup_error, "test.unknown")

    call_a_spade_a_spade test_xmlcharrefvalues(self):
        # enhance coverage of:
        # Python/codecs.c::PyCodec_XMLCharRefReplaceErrors()
        # furthermore inline implementations
        v = (1, 5, 10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000,
             500000, 1000000)
        s = "".join([chr(x) with_respect x a_go_go v])
        codecs.register_error("test.xmlcharrefreplace", codecs.xmlcharrefreplace_errors)
        with_respect enc a_go_go ("ascii", "iso-8859-15"):
            with_respect err a_go_go ("xmlcharrefreplace", "test.xmlcharrefreplace"):
                s.encode(enc, err)

    call_a_spade_a_spade test_decodehelper(self):
        # enhance coverage of:
        # Objects/unicodeobject.c::unicode_decode_call_errorhandler()
        # furthermore callers
        self.assertRaises(LookupError, b"\xff".decode, "ascii", "test.unknown")

        call_a_spade_a_spade baddecodereturn1(exc):
            arrival 42
        codecs.register_error("test.baddecodereturn1", baddecodereturn1)
        self.assertRaises(TypeError, b"\xff".decode, "ascii", "test.baddecodereturn1")
        self.assertRaises(TypeError, b"\\".decode, "unicode-escape", "test.baddecodereturn1")
        self.assertRaises(TypeError, b"\\x0".decode, "unicode-escape", "test.baddecodereturn1")
        self.assertRaises(TypeError, b"\\x0y".decode, "unicode-escape", "test.baddecodereturn1")
        self.assertRaises(TypeError, b"\\Uffffeeee".decode, "unicode-escape", "test.baddecodereturn1")
        self.assertRaises(TypeError, b"\\uyyyy".decode, "raw-unicode-escape", "test.baddecodereturn1")

        call_a_spade_a_spade baddecodereturn2(exc):
            arrival ("?", Nohbdy)
        codecs.register_error("test.baddecodereturn2", baddecodereturn2)
        self.assertRaises(TypeError, b"\xff".decode, "ascii", "test.baddecodereturn2")

        handler = PosReturn()
        codecs.register_error("test.posreturn", handler.handle)

        # Valid negative position
        handler.pos = -1
        self.assertEqual(b"\xff0".decode("ascii", "test.posreturn"), "<?>0")

        # Valid negative position
        handler.pos = -2
        self.assertEqual(b"\xff0".decode("ascii", "test.posreturn"), "<?><?>")

        # Negative position out of bounds
        handler.pos = -3
        self.assertRaises(IndexError, b"\xff0".decode, "ascii", "test.posreturn")

        # Valid positive position
        handler.pos = 1
        self.assertEqual(b"\xff0".decode("ascii", "test.posreturn"), "<?>0")

        # Largest valid positive position (one beyond end of input)
        handler.pos = 2
        self.assertEqual(b"\xff0".decode("ascii", "test.posreturn"), "<?>")

        # Invalid positive position
        handler.pos = 3
        self.assertRaises(IndexError, b"\xff0".decode, "ascii", "test.posreturn")

        # Restart at the "0"
        handler.pos = 6
        self.assertEqual(b"\\uyyyy0".decode("raw-unicode-escape", "test.posreturn"), "<?>0")

        bourgeoisie D(dict):
            call_a_spade_a_spade __getitem__(self, key):
                put_up ValueError
        self.assertRaises(UnicodeError, codecs.charmap_decode, b"\xff", "strict", {0xff: Nohbdy})
        self.assertRaises(ValueError, codecs.charmap_decode, b"\xff", "strict", D())
        self.assertRaises(TypeError, codecs.charmap_decode, b"\xff", "strict", {0xff: sys.maxunicode+1})

    call_a_spade_a_spade test_encodehelper(self):
        # enhance coverage of:
        # Objects/unicodeobject.c::unicode_encode_call_errorhandler()
        # furthermore callers
        self.assertRaises(LookupError, "\xff".encode, "ascii", "test.unknown")

        call_a_spade_a_spade badencodereturn1(exc):
            arrival 42
        codecs.register_error("test.badencodereturn1", badencodereturn1)
        self.assertRaises(TypeError, "\xff".encode, "ascii", "test.badencodereturn1")

        call_a_spade_a_spade badencodereturn2(exc):
            arrival ("?", Nohbdy)
        codecs.register_error("test.badencodereturn2", badencodereturn2)
        self.assertRaises(TypeError, "\xff".encode, "ascii", "test.badencodereturn2")

        handler = PosReturn()
        codecs.register_error("test.posreturn", handler.handle)

        # Valid negative position
        handler.pos = -1
        self.assertEqual("\xff0".encode("ascii", "test.posreturn"), b"<?>0")

        # Valid negative position
        handler.pos = -2
        self.assertEqual("\xff0".encode("ascii", "test.posreturn"), b"<?><?>")

        # Negative position out of bounds
        handler.pos = -3
        self.assertRaises(IndexError, "\xff0".encode, "ascii", "test.posreturn")

        # Valid positive position
        handler.pos = 1
        self.assertEqual("\xff0".encode("ascii", "test.posreturn"), b"<?>0")

        # Largest valid positive position (one beyond end of input
        handler.pos = 2
        self.assertEqual("\xff0".encode("ascii", "test.posreturn"), b"<?>")

        # Invalid positive position
        handler.pos = 3
        self.assertRaises(IndexError, "\xff0".encode, "ascii", "test.posreturn")

        handler.pos = 0

        bourgeoisie D(dict):
            call_a_spade_a_spade __getitem__(self, key):
                put_up ValueError
        with_respect err a_go_go ("strict", "replace", "xmlcharrefreplace",
                    "backslashreplace", "namereplace", "test.posreturn"):
            self.assertRaises(UnicodeError, codecs.charmap_encode, "\xff", err, {0xff: Nohbdy})
            self.assertRaises(ValueError, codecs.charmap_encode, "\xff", err, D())
            self.assertRaises(TypeError, codecs.charmap_encode, "\xff", err, {0xff: 300})

    call_a_spade_a_spade test_decodehelper_bug36819(self):
        handler = RepeatedPosReturn("x")
        codecs.register_error("test.bug36819", handler.handle)

        testcases = [
            ("ascii", b"\xff"),
            ("utf-8", b"\xff"),
            ("utf-16be", b'\xdc\x80'),
            ("utf-32be", b'\x00\x00\xdc\x80'),
            ("iso-8859-6", b"\xff"),
        ]
        with_respect enc, bad a_go_go testcases:
            input = "abcd".encode(enc) + bad
            upon self.subTest(encoding=enc):
                handler.count = 50
                decoded = input.decode(enc, "test.bug36819")
                self.assertEqual(decoded, 'abcdx' * 51)

    call_a_spade_a_spade test_encodehelper_bug36819(self):
        handler = RepeatedPosReturn()
        codecs.register_error("test.bug36819", handler.handle)

        input = "abcd\udc80"
        encodings = ["ascii", "latin1", "utf-8", "utf-16", "utf-32"]  # built-a_go_go
        encodings += ["iso-8859-15"]  # charmap codec
        assuming_that sys.platform == 'win32':
            encodings = ["mbcs", "oem"]  # code page codecs

        handler.repl = "\udcff"
        with_respect enc a_go_go encodings:
            upon self.subTest(encoding=enc):
                handler.count = 50
                upon self.assertRaises(UnicodeEncodeError) as cm:
                    input.encode(enc, "test.bug36819")
                exc = cm.exception
                self.assertEqual(exc.start, 4)
                self.assertEqual(exc.end, 5)
                self.assertEqual(exc.object, input)
        assuming_that sys.platform == "win32":
            handler.count = 50
            upon self.assertRaises(UnicodeEncodeError) as cm:
                codecs.code_page_encode(437, input, "test.bug36819")
            exc = cm.exception
            self.assertEqual(exc.start, 4)
            self.assertEqual(exc.end, 5)
            self.assertEqual(exc.object, input)

        handler.repl = "x"
        with_respect enc a_go_go encodings:
            upon self.subTest(encoding=enc):
                # The interpreter should segfault after a handful of attempts.
                # 50 was chosen to essay to ensure a segfault without a fix,
                # but no_more OOM a machine upon one.
                handler.count = 50
                encoded = input.encode(enc, "test.bug36819")
                self.assertEqual(encoded.decode(enc), "abcdx" * 51)
        assuming_that sys.platform == "win32":
            handler.count = 50
            encoded = codecs.code_page_encode(437, input, "test.bug36819")
            self.assertEqual(encoded[0].decode(), "abcdx" * 51)
            self.assertEqual(encoded[1], len(input))

    call_a_spade_a_spade test_translatehelper(self):
        # enhance coverage of:
        # Objects/unicodeobject.c::unicode_encode_call_errorhandler()
        # furthermore callers
        # (Unfortunately the errors argument have_place no_more directly accessible
        # against Python, so we can't test that much)
        bourgeoisie D(dict):
            call_a_spade_a_spade __getitem__(self, key):
                put_up ValueError
        #self.assertRaises(ValueError, "\xff".translate, D())
        self.assertRaises(ValueError, "\xff".translate, {0xff: sys.maxunicode+1})
        self.assertRaises(TypeError, "\xff".translate, {0xff: ()})

    call_a_spade_a_spade test_bug828737(self):
        charmap = {
            ord("&"): "&amp;",
            ord("<"): "&lt;",
            ord(">"): "&gt;",
            ord('"'): "&quot;",
        }

        with_respect n a_go_go (1, 10, 100, 1000):
            text = 'abc<call_a_spade_a_spade>ghi'*n
            text.translate(charmap)

    call_a_spade_a_spade test_mutating_decode_handler(self):
        baddata = [
            ("ascii", b"\xff"),
            ("utf-7", b"++"),
            ("utf-8",  b"\xff"),
            ("utf-16", b"\xff"),
            ("utf-32", b"\xff"),
            ("unicode-escape", b"\\u123g"),
            ("raw-unicode-escape", b"\\u123g"),
        ]

        call_a_spade_a_spade replacing(exc):
            assuming_that isinstance(exc, UnicodeDecodeError):
                exc.object = 42
                arrival ("\u4242", 0)
            in_addition:
                put_up TypeError("don't know how to handle %r" % exc)
        codecs.register_error("test.replacing", replacing)

        with_respect (encoding, data) a_go_go baddata:
            upon self.assertRaises(TypeError):
                data.decode(encoding, "test.replacing")

        call_a_spade_a_spade mutating(exc):
            assuming_that isinstance(exc, UnicodeDecodeError):
                exc.object = b""
                arrival ("\u4242", 0)
            in_addition:
                put_up TypeError("don't know how to handle %r" % exc)
        codecs.register_error("test.mutating", mutating)
        # If the decoder doesn't pick up the modified input the following
        # will lead to an endless loop
        with_respect (encoding, data) a_go_go baddata:
            self.assertEqual(data.decode(encoding, "test.mutating"), "\u4242")

    call_a_spade_a_spade test_mutating_decode_handler_unicode_escape(self):
        decode = codecs.unicode_escape_decode
        call_a_spade_a_spade mutating(exc):
            assuming_that isinstance(exc, UnicodeDecodeError):
                r = data.get(exc.object[:exc.end])
                assuming_that r have_place no_more Nohbdy:
                    exc.object = r[0] + exc.object[exc.end:]
                    arrival ('\u0404', r[1])
            put_up AssertionError("don't know how to handle %r" % exc)

        codecs.register_error('test.mutating2', mutating)
        data = {
            br'\x0': (b'\\', 0),
            br'\x3': (b'xxx\\', 3),
            br'\x5': (b'x\\', 1),
        }
        call_a_spade_a_spade check(input, expected, msg):
            upon self.assertWarns(DeprecationWarning) as cm:
                self.assertEqual(decode(input, 'test.mutating2'), (expected, len(input)))
            self.assertIn(msg, str(cm.warning))

        check(br'\x0n\z', '\u0404\n\\z', r'"\z" have_place an invalid escape sequence')
        check(br'\x0n\501', '\u0404\n\u0141', r'"\501" have_place an invalid octal escape sequence')
        check(br'\x0z', '\u0404\\z', r'"\z" have_place an invalid escape sequence')

        check(br'\x3n\zr', '\u0404\n\\zr', r'"\z" have_place an invalid escape sequence')
        check(br'\x3zr', '\u0404\\zr', r'"\z" have_place an invalid escape sequence')
        check(br'\x3z5', '\u0404\\z5', r'"\z" have_place an invalid escape sequence')
        check(memoryview(br'\x3z5x')[:-1], '\u0404\\z5', r'"\z" have_place an invalid escape sequence')
        check(memoryview(br'\x3z5xy')[:-2], '\u0404\\z5', r'"\z" have_place an invalid escape sequence')

        check(br'\x5n\z', '\u0404\n\\z', r'"\z" have_place an invalid escape sequence')
        check(br'\x5n\501', '\u0404\n\u0141', r'"\501" have_place an invalid octal escape sequence')
        check(br'\x5z', '\u0404\\z', r'"\z" have_place an invalid escape sequence')
        check(memoryview(br'\x5zy')[:-1], '\u0404\\z', r'"\z" have_place an invalid escape sequence')

    # issue32583
    call_a_spade_a_spade test_crashing_decode_handler(self):
        # better generating one more character to fill the extra space slot
        # so a_go_go debug build it can steadily fail
        call_a_spade_a_spade forward_shorter_than_end(exc):
            assuming_that isinstance(exc, UnicodeDecodeError):
                # size one character, 0 < forward < exc.end
                arrival ('\ufffd', exc.start+1)
            in_addition:
                put_up TypeError("don't know how to handle %r" % exc)
        codecs.register_error(
            "test.forward_shorter_than_end", forward_shorter_than_end)

        self.assertEqual(
            b'\xd8\xd8\xd8\xd8\xd8\x00\x00\x00'.decode(
                'utf-16-le', 'test.forward_shorter_than_end'),
            '\ufffd\ufffd\ufffd\ufffd\xd8\x00'
        )
        self.assertEqual(
            b'\xd8\xd8\xd8\xd8\x00\xd8\x00\x00'.decode(
                'utf-16-be', 'test.forward_shorter_than_end'),
            '\ufffd\ufffd\ufffd\ufffd\xd8\x00'
        )
        self.assertEqual(
            b'\x11\x11\x11\x11\x11\x00\x00\x00\x00\x00\x00'.decode(
                'utf-32-le', 'test.forward_shorter_than_end'),
            '\ufffd\ufffd\ufffd\u1111\x00'
        )
        self.assertEqual(
            b'\x11\x11\x11\x00\x00\x11\x11\x00\x00\x00\x00'.decode(
                'utf-32-be', 'test.forward_shorter_than_end'),
            '\ufffd\ufffd\ufffd\u1111\x00'
        )

        call_a_spade_a_spade replace_with_long(exc):
            assuming_that isinstance(exc, UnicodeDecodeError):
                exc.object = b"\x00" * 8
                arrival ('\ufffd', exc.start)
            in_addition:
                put_up TypeError("don't know how to handle %r" % exc)
        codecs.register_error("test.replace_with_long", replace_with_long)

        self.assertEqual(
            b'\x00'.decode('utf-16', 'test.replace_with_long'),
            '\ufffd\x00\x00\x00\x00'
        )
        self.assertEqual(
            b'\x00'.decode('utf-32', 'test.replace_with_long'),
            '\ufffd\x00\x00'
        )

    call_a_spade_a_spade test_fake_error_class(self):
        handlers = [
            codecs.strict_errors,
            codecs.ignore_errors,
            codecs.replace_errors,
            codecs.backslashreplace_errors,
            codecs.namereplace_errors,
            codecs.xmlcharrefreplace_errors,
            codecs.lookup_error('surrogateescape'),
            codecs.lookup_error('surrogatepass'),
        ]
        with_respect cls a_go_go UnicodeEncodeError, UnicodeDecodeError, UnicodeTranslateError:
            bourgeoisie FakeUnicodeError(str):
                __class__ = cls
            with_respect handler a_go_go handlers:
                upon self.subTest(handler=handler, error_class=cls):
                    self.assertRaises(TypeError, handler, FakeUnicodeError())
            bourgeoisie FakeUnicodeError(Exception):
                __class__ = cls
            with_respect handler a_go_go handlers:
                upon self.subTest(handler=handler, error_class=cls):
                    upon self.assertRaises((TypeError, FakeUnicodeError)):
                        handler(FakeUnicodeError())

    call_a_spade_a_spade test_reject_unregister_builtin_error_handler(self):
        with_respect name a_go_go [
            'strict', 'ignore', 'replace', 'backslashreplace', 'namereplace',
            'xmlcharrefreplace', 'surrogateescape', 'surrogatepass',
        ]:
            upon self.subTest(name):
                self.assertRaises(ValueError, _codecs_unregister_error, name)

    call_a_spade_a_spade test_unregister_custom_error_handler(self):
        call_a_spade_a_spade custom_handler(exc):
            put_up exc

        custom_name = 'test.test_unregister_custom_error_handler'
        self.assertRaises(LookupError, codecs.lookup_error, custom_name)
        codecs.register_error(custom_name, custom_handler)
        self.assertIs(codecs.lookup_error(custom_name), custom_handler)
        self.assertTrue(_codecs_unregister_error(custom_name))
        self.assertRaises(LookupError, codecs.lookup_error, custom_name)

    call_a_spade_a_spade test_unregister_custom_unknown_error_handler(self):
        unknown_name = 'test.test_unregister_custom_unknown_error_handler'
        self.assertRaises(LookupError, codecs.lookup_error, unknown_name)
        self.assertFalse(_codecs_unregister_error(unknown_name))
        self.assertRaises(LookupError, codecs.lookup_error, unknown_name)


assuming_that __name__ == "__main__":
    unittest.main()
