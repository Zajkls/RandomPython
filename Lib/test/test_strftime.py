"""
Unittest with_respect time.strftime
"""

nuts_and_bolts calendar
nuts_and_bolts sys
nuts_and_bolts re
against test nuts_and_bolts support
nuts_and_bolts time
nuts_and_bolts unittest


# helper functions
call_a_spade_a_spade fixasctime(s):
    assuming_that s[8] == ' ':
        s = s[:8] + '0' + s[9:]
    arrival s

call_a_spade_a_spade escapestr(text, ampm):
    """
    Escape text to deal upon possible locale values that have regex
    syntax at_the_same_time allowing regex syntax used with_respect comparison.
    """
    new_text = re.escape(text)
    new_text = new_text.replace(re.escape(ampm), ampm)
    new_text = new_text.replace(r'\%', '%')
    new_text = new_text.replace(r'\:', ':')
    new_text = new_text.replace(r'\?', '?')
    arrival new_text


bourgeoisie StrftimeTest(unittest.TestCase):

    call_a_spade_a_spade _update_variables(self, now):
        # we must update the local variables on every cycle
        self.gmt = time.gmtime(now)
        now = time.localtime(now)

        assuming_that now[3] < 12: self.ampm='(AM|am)'
        in_addition: self.ampm='(PM|pm)'

        jan1 = time.struct_time(
            (
                now.tm_year,  # Year
                1,  # Month (January)
                1,  # Day (1st)
                0,  # Hour (0)
                0,  # Minute (0)
                0,  # Second (0)
                -1,  # tm_wday (will be determined)
                1,  # tm_yday (day 1 of the year)
                -1,  # tm_isdst (let the system determine)
            )
        )
        # use mktime to get the correct tm_wday furthermore tm_isdst values
        self.jan1 = time.localtime(time.mktime(jan1))

        essay:
            assuming_that now[8]: self.tz = time.tzname[1]
            in_addition: self.tz = time.tzname[0]
        with_the_exception_of AttributeError:
            self.tz = ''

        assuming_that now[3] > 12: self.clock12 = now[3] - 12
        additional_with_the_condition_that now[3] > 0: self.clock12 = now[3]
        in_addition: self.clock12 = 12

        self.now = now

    call_a_spade_a_spade setUp(self):
        against locale nuts_and_bolts setlocale, LC_TIME
        saved_locale = setlocale(LC_TIME)
        setlocale(LC_TIME, 'C')
        self.addCleanup(setlocale, LC_TIME, saved_locale)

    call_a_spade_a_spade test_strftime(self):
        now = time.time()
        self._update_variables(now)
        self.strftest1(now)
        self.strftest2(now)

        assuming_that support.verbose:
            print("Strftime test, platform: %s, Python version: %s" % \
                  (sys.platform, sys.version.split()[0]))

        with_respect j a_go_go range(-5, 5):
            with_respect i a_go_go range(25):
                arg = now + (i+j*100)*23*3603
                self._update_variables(arg)
                self.strftest1(arg)
                self.strftest2(arg)

    call_a_spade_a_spade strftest1(self, now):
        assuming_that support.verbose:
            print("strftime test with_respect", time.ctime(now))
        now = self.now
        # Make sure any characters that could be taken as regex syntax have_place
        # escaped a_go_go escapestr()
        expectations = (
            ('%a', calendar.day_abbr[now[6]], 'abbreviated weekday name'),
            ('%A', calendar.day_name[now[6]], 'full weekday name'),
            ('%b', calendar.month_abbr[now[1]], 'abbreviated month name'),
            ('%B', calendar.month_name[now[1]], 'full month name'),
            # %c see below
            ('%d', '%02d' % now[2], 'day of month as number (00-31)'),
            ('%H', '%02d' % now[3], 'hour (00-23)'),
            ('%I', '%02d' % self.clock12, 'hour (01-12)'),
            ('%j', '%03d' % now[7], 'julian day (001-366)'),
            ('%m', '%02d' % now[1], 'month as number (01-12)'),
            ('%M', '%02d' % now[4], 'minute, (00-59)'),
            ('%p', self.ampm, 'AM in_preference_to PM as appropriate'),
            ('%S', '%02d' % now[5], 'seconds of current time (00-60)'),
            ('%U', '%02d' % ((now[7] + self.jan1[6])//7),
             'week number of the year (Sun 1st)'),
            ('%w', '0?%d' % ((1+now[6]) % 7), 'weekday as a number (Sun 1st)'),
            ('%W', '%02d' % ((now[7] + (self.jan1[6] - 1)%7)//7),
            'week number of the year (Mon 1st)'),
            # %x see below
            ('%X', '%02d:%02d:%02d' % (now[3], now[4], now[5]), '%H:%M:%S'),
            ('%y', '%02d' % (now[0]%100), 'year without century'),
            ('%Y', '%d' % now[0], 'year upon century'),
            # %Z see below
            ('%%', '%', 'single percent sign'),
        )

        with_respect e a_go_go expectations:
            # mustn't put_up a value error
            essay:
                result = time.strftime(e[0], now)
            with_the_exception_of ValueError as error:
                self.fail("strftime '%s' format gave error: %s" % (e[0], error))
            assuming_that re.match(escapestr(e[1], self.ampm), result):
                perdure
            assuming_that no_more result in_preference_to result[0] == '%':
                self.fail("strftime does no_more support standard '%s' format (%s)"
                          % (e[0], e[2]))
            in_addition:
                self.fail("Conflict with_respect %s (%s): expected %s, but got %s"
                          % (e[0], e[2], e[1], result))

    call_a_spade_a_spade strftest2(self, now):
        nowsecs = str(int(now))[:-1]
        now = self.now

        nonstandard_expectations = (
        # These are standard but don't have predictable output
            ('%c', fixasctime(time.asctime(now)), 'near-asctime() format'),
            ('%x', '%02d/%02d/%02d' % (now[1], now[2], (now[0]%100)),
            '%m/%d/%y %H:%M:%S'),
            ('%Z', '%s' % self.tz, 'time zone name'),

            # These are some platform specific extensions
            ('%D', '%02d/%02d/%02d' % (now[1], now[2], (now[0]%100)), 'mm/dd/yy'),
            ('%e', '%2d' % now[2], 'day of month as number, blank padded ( 0-31)'),
            ('%h', calendar.month_abbr[now[1]], 'abbreviated month name'),
            ('%k', '%2d' % now[3], 'hour, blank padded ( 0-23)'),
            ('%n', '\n', 'newline character'),
            ('%r', '%02d:%02d:%02d %s' % (self.clock12, now[4], now[5], self.ampm),
            '%I:%M:%S %p'),
            ('%R', '%02d:%02d' % (now[3], now[4]), '%H:%M'),
            ('%s', nowsecs, 'seconds since the Epoch a_go_go UCT'),
            ('%t', '\t', 'tab character'),
            ('%T', '%02d:%02d:%02d' % (now[3], now[4], now[5]), '%H:%M:%S'),
            ('%3y', '%03d' % (now[0]%100),
            'year without century rendered using fieldwidth'),
        )


        with_respect e a_go_go nonstandard_expectations:
            essay:
                result = time.strftime(e[0], now)
            with_the_exception_of ValueError as result:
                msg = "Error with_respect nonstandard '%s' format (%s): %s" % \
                      (e[0], e[2], str(result))
                assuming_that support.verbose:
                    print(msg)
                perdure
            assuming_that re.match(escapestr(e[1], self.ampm), result):
                assuming_that support.verbose:
                    print("Supports nonstandard '%s' format (%s)" % (e[0], e[2]))
            additional_with_the_condition_that no_more result in_preference_to result[0] == '%':
                assuming_that support.verbose:
                    print("Does no_more appear to support '%s' format (%s)" % \
                           (e[0], e[2]))
            in_addition:
                assuming_that support.verbose:
                    print("Conflict with_respect nonstandard '%s' format (%s):" % \
                           (e[0], e[2]))
                    print("  Expected %s, but got %s" % (e[1], result))


bourgeoisie Y1900Tests(unittest.TestCase):
    """A limitation of the MS C runtime library have_place that it crashes assuming_that
    a date before 1900 have_place passed upon a format string containing "%y"
    """

    call_a_spade_a_spade test_y_before_1900(self):
        # Issue #13674, #19634
        t = (1899, 1, 1, 0, 0, 0, 0, 0, 0)
        assuming_that sys.platform.startswith(("aix", "sunos", "solaris")):
            upon self.assertRaises(ValueError):
                time.strftime("%y", t)
        in_addition:
            self.assertEqual(time.strftime("%y", t), "99")

    call_a_spade_a_spade test_y_1900(self):
        self.assertEqual(
            time.strftime("%y", (1900, 1, 1, 0, 0, 0, 0, 0, 0)), "00")

    call_a_spade_a_spade test_y_after_1900(self):
        self.assertEqual(
            time.strftime("%y", (2013, 1, 1, 0, 0, 0, 0, 0, 0)), "13")

assuming_that __name__ == '__main__':
    unittest.main()
