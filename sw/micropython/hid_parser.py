from hid_mapping import mapping, uppercase_mapping
class Parser(object):
    NEW_KEY_MARKER = 'HID-00-00-00-00-00-00-00-00'
    SHIFT_MARKER = 'HID-02-00-00-00-00-00-00-00'

    @staticmethod
    def map(byte, modifier=None):
        m = uppercase_mapping if modifier else mapping
        if byte in m:
            return m[byte]
        return ''

    def __init__(self):
        self.reset()

    def read(self):
        res = self.result
        self.result = ''
        return res

    def reset(self):
        self.result = ''
        self.dirty = False
        self.new_keys = []
        self.modifier = None

    def updateKeys(self,keys):
        for k in keys:
            if k not in self.new_keys:
                self.new_keys.append(k)



    def extract(self, string):
        if not 'HID-' in string:
            return
        try:
            strings = string.split('-')[1:]
            bytes = list(map(lambda i: int(i, 16) if i != '00' else None, strings))

            self.modifier = bytes[0]

            keys = bytes[1:] # ignore modifier byte
            keys = [x for x in keys if x is not None] # skip empty entries
            self.updateKeys(keys)

        except Exception as e: 
            # silently ignore any parsing errors and reset the parser
            self.reset()
            pass

    def flush(self):
        for k in self.new_keys:
            if(k):
                self.result += Parser.map(k, self.modifier)
        self.new_keys = []

    def put(self, string):

        if string == self.NEW_KEY_MARKER or string == self.SHIFT_MARKER:
            if not self.dirty:
                self.flush()

        else:
            self.extract(string)


class Message:
    def __init__(self, string):
        self.marker = 0x00
        self.keys = []
        # Parse from the string


if __name__ == '__main__':
    p = Parser()
    p.put('HID-00-00-00-00-00-00-00-00')  # marker
    print(p.read())
    p.put('HID-00-00-1a-00-00-00-00-00')
    print(p.read())
    p.put('HID-00-00-1a-08-00-00-00-00')
    print(p.read())
    p.put('HID-00-00-1a-08-15-00-00-00')
    print(p.read())
    p.put('HID-00-00-15-08-00-00-00-00')
    print(p.read())
    p.put('HID-00-00-15-00-00-00-00-00')
    print(p.read())
    p.put('HID-00-00-00-00-00-00-00-00')
    print(p.read())
    p.put('HID-00-00-17-00-00-00-00-00')
    print(p.read())
    p.put('HID-00-00-00-00-00-00-00-00')
    print(p.read())
