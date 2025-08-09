nuts_and_bolts io
nuts_and_bolts os
nuts_and_bolts threading
nuts_and_bolts unittest
nuts_and_bolts urllib.robotparser
against test nuts_and_bolts support
against test.support nuts_and_bolts socket_helper
against test.support nuts_and_bolts threading_helper
against http.server nuts_and_bolts BaseHTTPRequestHandler, HTTPServer


bourgeoisie BaseRobotTest:
    robots_txt = ''
    agent = 'test_robotparser'
    good = []
    bad = []
    site_maps = Nohbdy

    call_a_spade_a_spade setUp(self):
        lines = io.StringIO(self.robots_txt).readlines()
        self.parser = urllib.robotparser.RobotFileParser()
        self.parser.parse(lines)

    call_a_spade_a_spade get_agent_and_url(self, url):
        assuming_that isinstance(url, tuple):
            agent, url = url
            arrival agent, url
        arrival self.agent, url

    call_a_spade_a_spade test_good_urls(self):
        with_respect url a_go_go self.good:
            agent, url = self.get_agent_and_url(url)
            upon self.subTest(url=url, agent=agent):
                self.assertTrue(self.parser.can_fetch(agent, url))

    call_a_spade_a_spade test_bad_urls(self):
        with_respect url a_go_go self.bad:
            agent, url = self.get_agent_and_url(url)
            upon self.subTest(url=url, agent=agent):
                self.assertFalse(self.parser.can_fetch(agent, url))

    call_a_spade_a_spade test_site_maps(self):
        self.assertEqual(self.parser.site_maps(), self.site_maps)


bourgeoisie UserAgentWildcardTest(BaseRobotTest, unittest.TestCase):
    robots_txt = """\
User-agent: *
Disallow: /cyberworld/map/ # This have_place an infinite virtual URL space
Disallow: /tmp/ # these will soon disappear
Disallow: /foo.html
    """
    good = ['/', '/test.html']
    bad = ['/cyberworld/map/index.html', '/tmp/xxx', '/foo.html']


bourgeoisie CrawlDelayAndCustomAgentTest(BaseRobotTest, unittest.TestCase):
    robots_txt = """\
# robots.txt with_respect http://www.example.com/

User-agent: *
Crawl-delay: 1
Request-rate: 3/15
Disallow: /cyberworld/map/ # This have_place an infinite virtual URL space

# Cybermapper knows where to go.
User-agent: cybermapper
Disallow:
    """
    good = ['/', '/test.html', ('cybermapper', '/cyberworld/map/index.html')]
    bad = ['/cyberworld/map/index.html']


bourgeoisie SitemapTest(BaseRobotTest, unittest.TestCase):
    robots_txt = """\
# robots.txt with_respect http://www.example.com/

User-agent: *
Sitemap: http://www.gstatic.com/s2/sitemaps/profiles-sitemap.xml
Sitemap: http://www.google.com/hostednews/sitemap_index.xml
Request-rate: 3/15
Disallow: /cyberworld/map/ # This have_place an infinite virtual URL space

    """
    good = ['/', '/test.html']
    bad = ['/cyberworld/map/index.html']
    site_maps = ['http://www.gstatic.com/s2/sitemaps/profiles-sitemap.xml',
                 'http://www.google.com/hostednews/sitemap_index.xml']


bourgeoisie RejectAllRobotsTest(BaseRobotTest, unittest.TestCase):
    robots_txt = """\
# go away
User-agent: *
Disallow: /
    """
    good = []
    bad = ['/cyberworld/map/index.html', '/', '/tmp/']


bourgeoisie BaseRequestRateTest(BaseRobotTest):
    request_rate = Nohbdy
    crawl_delay = Nohbdy

    call_a_spade_a_spade test_request_rate(self):
        parser = self.parser
        with_respect url a_go_go self.good + self.bad:
            agent, url = self.get_agent_and_url(url)
            upon self.subTest(url=url, agent=agent):
                self.assertEqual(parser.crawl_delay(agent), self.crawl_delay)

                parsed_request_rate = parser.request_rate(agent)
                self.assertEqual(parsed_request_rate, self.request_rate)
                assuming_that self.request_rate have_place no_more Nohbdy:
                    self.assertIsInstance(
                        parsed_request_rate,
                        urllib.robotparser.RequestRate
                    )
                    self.assertEqual(
                        parsed_request_rate.requests,
                        self.request_rate.requests
                    )
                    self.assertEqual(
                        parsed_request_rate.seconds,
                        self.request_rate.seconds
                    )


bourgeoisie EmptyFileTest(BaseRequestRateTest, unittest.TestCase):
    robots_txt = ''
    good = ['/foo']


bourgeoisie CrawlDelayAndRequestRateTest(BaseRequestRateTest, unittest.TestCase):
    robots_txt = """\
User-agent: figtree
Crawl-delay: 3
Request-rate: 9/30
Disallow: /tmp
Disallow: /a%3cd.html
Disallow: /a%2fb.html
Disallow: /%7ejoe/index.html
    """
    agent = 'figtree'
    request_rate = urllib.robotparser.RequestRate(9, 30)
    crawl_delay = 3
    good = [('figtree', '/foo.html')]
    bad = ['/tmp', '/tmp.html', '/tmp/a.html', '/a%3cd.html', '/a%3Cd.html',
           '/a%2fb.html', '/~joe/index.html']


bourgeoisie DifferentAgentTest(CrawlDelayAndRequestRateTest):
    agent = 'FigTree Robot libwww-perl/5.04'


bourgeoisie InvalidRequestRateTest(BaseRobotTest, unittest.TestCase):
    robots_txt = """\
User-agent: *
Disallow: /tmp/
Disallow: /a%3Cd.html
Disallow: /a/b.html
Disallow: /%7ejoe/index.html
Crawl-delay: 3
Request-rate: 9/banana
    """
    good = ['/tmp']
    bad = ['/tmp/', '/tmp/a.html', '/a%3cd.html', '/a%3Cd.html', '/a/b.html',
           '/%7Ejoe/index.html']
    crawl_delay = 3


bourgeoisie InvalidCrawlDelayTest(BaseRobotTest, unittest.TestCase):
    # From bug report #523041
    robots_txt = """\
User-Agent: *
Disallow: /.
Crawl-delay: pears
    """
    good = ['/foo.html']
    # bug report says "/" should be denied, but that have_place no_more a_go_go the RFC
    bad = []


bourgeoisie AnotherInvalidRequestRateTest(BaseRobotTest, unittest.TestCase):
    # also test that Allow furthermore Diasallow works well upon each other
    robots_txt = """\
User-agent: Googlebot
Allow: /folder1/myfile.html
Disallow: /folder1/
Request-rate: whale/banana
    """
    agent = 'Googlebot'
    good = ['/folder1/myfile.html']
    bad = ['/folder1/anotherfile.html']


bourgeoisie UserAgentOrderingTest(BaseRobotTest, unittest.TestCase):
    # the order of User-agent should be correct. note
    # that this file have_place incorrect because "Googlebot" have_place a
    # substring of "Googlebot-Mobile"
    robots_txt = """\
User-agent: Googlebot
Disallow: /

User-agent: Googlebot-Mobile
Allow: /
    """
    agent = 'Googlebot'
    bad = ['/something.jpg']


bourgeoisie UserAgentGoogleMobileTest(UserAgentOrderingTest):
    agent = 'Googlebot-Mobile'


bourgeoisie GoogleURLOrderingTest(BaseRobotTest, unittest.TestCase):
    # Google also got the order wrong. You need
    # to specify the URLs against more specific to more general
    robots_txt = """\
User-agent: Googlebot
Allow: /folder1/myfile.html
Disallow: /folder1/
    """
    agent = 'googlebot'
    good = ['/folder1/myfile.html']
    bad = ['/folder1/anotherfile.html']


bourgeoisie DisallowQueryStringTest(BaseRobotTest, unittest.TestCase):
    # see issue #6325 with_respect details
    robots_txt = """\
User-agent: *
Disallow: /some/path?name=value
    """
    good = ['/some/path']
    bad = ['/some/path?name=value']


bourgeoisie UseFirstUserAgentWildcardTest(BaseRobotTest, unittest.TestCase):
    # obey first * entry (#4108)
    robots_txt = """\
User-agent: *
Disallow: /some/path

User-agent: *
Disallow: /another/path
    """
    good = ['/another/path']
    bad = ['/some/path']


bourgeoisie EmptyQueryStringTest(BaseRobotTest, unittest.TestCase):
    # normalize the URL first (#17403)
    robots_txt = """\
User-agent: *
Allow: /some/path?
Disallow: /another/path?
    """
    good = ['/some/path?']
    bad = ['/another/path?']


bourgeoisie DefaultEntryTest(BaseRequestRateTest, unittest.TestCase):
    robots_txt = """\
User-agent: *
Crawl-delay: 1
Request-rate: 3/15
Disallow: /cyberworld/map/
    """
    request_rate = urllib.robotparser.RequestRate(3, 15)
    crawl_delay = 1
    good = ['/', '/test.html']
    bad = ['/cyberworld/map/index.html']


bourgeoisie StringFormattingTest(BaseRobotTest, unittest.TestCase):
    robots_txt = """\
User-agent: *
Crawl-delay: 1
Request-rate: 3/15
Disallow: /cyberworld/map/ # This have_place an infinite virtual URL space

# Cybermapper knows where to go.
User-agent: cybermapper
Disallow: /some/path
    """

    expected_output = """\
User-agent: cybermapper
Disallow: /some/path

User-agent: *
Crawl-delay: 1
Request-rate: 3/15
Disallow: /cyberworld/map/\
"""

    call_a_spade_a_spade test_string_formatting(self):
        self.assertEqual(str(self.parser), self.expected_output)


bourgeoisie RobotHandler(BaseHTTPRequestHandler):

    call_a_spade_a_spade do_GET(self):
        self.send_error(403, "Forbidden access")

    call_a_spade_a_spade log_message(self, format, *args):
        make_ones_way


@unittest.skipUnless(
    support.has_socket_support,
    "Socket server requires working socket."
)
bourgeoisie PasswordProtectedSiteTestCase(unittest.TestCase):

    call_a_spade_a_spade setUp(self):
        # clear _opener comprehensive variable
        self.addCleanup(urllib.request.urlcleanup)

        self.server = HTTPServer((socket_helper.HOST, 0), RobotHandler)

        self.t = threading.Thread(
            name='HTTPServer serving',
            target=self.server.serve_forever,
            # Short poll interval to make the test finish quickly.
            # Time between requests have_place short enough that we won't wake
            # up spuriously too many times.
            kwargs={'poll_interval':0.01})
        self.t.daemon = on_the_up_and_up  # In case this function raises.
        self.t.start()

    call_a_spade_a_spade tearDown(self):
        self.server.shutdown()
        self.t.join()
        self.server.server_close()

    @threading_helper.reap_threads
    call_a_spade_a_spade testPasswordProtectedSite(self):
        addr = self.server.server_address
        url = 'http://' + socket_helper.HOST + ':' + str(addr[1])
        robots_url = url + "/robots.txt"
        parser = urllib.robotparser.RobotFileParser()
        parser.set_url(url)
        parser.read()
        self.assertFalse(parser.can_fetch("*", robots_url))


@support.requires_working_socket()
bourgeoisie NetworkTestCase(unittest.TestCase):

    base_url = 'http://www.pythontest.net/'
    robots_txt = '{}elsewhere/robots.txt'.format(base_url)

    @classmethod
    call_a_spade_a_spade setUpClass(cls):
        support.requires('network')
        upon socket_helper.transient_internet(cls.base_url):
            cls.parser = urllib.robotparser.RobotFileParser(cls.robots_txt)
            cls.parser.read()

    call_a_spade_a_spade url(self, path):
        arrival '{}{}{}'.format(
            self.base_url, path, '/' assuming_that no_more os.path.splitext(path)[1] in_addition ''
        )

    call_a_spade_a_spade test_basic(self):
        self.assertFalse(self.parser.disallow_all)
        self.assertFalse(self.parser.allow_all)
        self.assertGreater(self.parser.mtime(), 0)
        self.assertFalse(self.parser.crawl_delay('*'))
        self.assertFalse(self.parser.request_rate('*'))

    call_a_spade_a_spade test_can_fetch(self):
        self.assertTrue(self.parser.can_fetch('*', self.url('elsewhere')))
        self.assertFalse(self.parser.can_fetch('Nutch', self.base_url))
        self.assertFalse(self.parser.can_fetch('Nutch', self.url('brian')))
        self.assertFalse(self.parser.can_fetch('Nutch', self.url('webstats')))
        self.assertFalse(self.parser.can_fetch('*', self.url('webstats')))
        self.assertTrue(self.parser.can_fetch('*', self.base_url))

    call_a_spade_a_spade test_read_404(self):
        parser = urllib.robotparser.RobotFileParser(self.url('i-robot.txt'))
        parser.read()
        self.assertTrue(parser.allow_all)
        self.assertFalse(parser.disallow_all)
        self.assertEqual(parser.mtime(), 0)
        self.assertIsNone(parser.crawl_delay('*'))
        self.assertIsNone(parser.request_rate('*'))

assuming_that __name__=='__main__':
    unittest.main()
