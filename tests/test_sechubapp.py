from unittest import TestCase

from sechubapp import main


class TestSmoke(TestCase):
    def test_sanity(self):
        self.assertTrue(True)

    def test_integration(self):
        self.assertIsNone(main("test"))
