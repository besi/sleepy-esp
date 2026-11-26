import unittest

from hid_parser import Parser


class TestStringMethods(unittest.TestCase):
    def marker(self, p):
        p.put('HID-00-00-00-00-00-00-00-00')  # marker

    def testAll(self):
        p = Parser()
        p.put('HID-00-00-00-00-00-00-00-00')  # marker
        p.put('HID-00-00-1a-00-00-00-00-00\n')
        p.put('HID-00-00-1a-08-00-00-00-00')
        p.put('HID-00-00-1a-08-15-00-00-00')
        p.put('HID-00-00-15-08-00-00-00-00')
        p.put('HID-00-00-15-00-00-00-00-00')
        p.put('HID-00-00-00-00-00-00-00-00')
        p.put('HID-00-00-17-00-00-00-00-00')
        p.put('HID-00-00-00-00-00-00-00-00')

        self.assertEqual(p.read(), 'wert')

    def test_uppercase_and_space(self):
        p = Parser()
        self.marker(p)
        p.put('HID-20-00-00-00-00-00-00-00')
        p.put('HID-20-00-04-00-00-00-00-00')
        p.put('HID-20-00-00-00-00-00-00-00')
        p.put('HID-20-00-2c-00-00-00-00-00')
        p.put('HID-20-00-00-00-00-00-00-00')
        p.put('HID-20-00-04-00-00-00-00-00')
        p.put('HID-20-00-00-00-00-00-00-00')

        self.assertEqual(p.read(), 'A A')


def test_all_uppercase(self):
        p = Parser()
        self.marker(p)
        p.put('HID-02-00-00-00-00-00-00-00')
        p.put('HID-02-00-17-00-00-00-00-00')
        p.put('HID-02-00-00-00-00-00-00-00')
        p.put('HID-02-00-12-00-00-00-00-00')
        p.put('HID-02-00-00-00-00-00-00-00')
        p.put('HID-02-00-07-00-00-00-00-00')
        p.put('HID-02-00-00-00-00-00-00-00')
        p.put('HID-02-00-12-00-00-00-00-00')
        p.put('HID-02-00-00-00-00-00-00-00')
        self.marker(p)

        self.assertEqual(p.read(), 'TODO')

def testWeirdMessages(self):
        p = Parser()

        self.marker(p)
        p.put('HID-00-00-1a-00-00-00-00-00\n')
        self.marker(p)
        self.assertEqual(p.read(), 'w')
        # WEIRD
        p.put('HID-ab-04-ef-gh-ih-00-00-00')
        p.put('HOD-02-04-04-00-00-00-00-00\n')
        p.put('\nHOD-ff-01-01-01-01-00-00-00\n') # no mapping
        p.put('when I was young I used to want to study HID thing')
        p.read()
        # ignored
        self.marker(p)
        p.put('HID-00-00-1a-00-00-00-00-00\n')
        self.marker(p)
        self.assertEqual(p.read(), 'w')

        # ignore OEM
        self.marker(p)
        p.put('HID-02-04-04-00-00-00-00-00\n')
        self.marker(p)
        self.assertEqual(p.read(), 'A')

        self.marker(p)

        self.marker(p)

if __name__ == '__main__':
    unittest.main()
