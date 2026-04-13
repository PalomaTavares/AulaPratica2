from test_framework import TestCase
from test_loader import TestLoader
from test_stub import TestStub
from test_spy import TestSpy
from test_suit import TestSuite


class TestLoaderTest(TestCase):
    def test_create_suite(self):
        loader = TestLoader()
        suite = loader.make_suite(TestStub)
        self.assert_equal(len(suite.tests), 3)