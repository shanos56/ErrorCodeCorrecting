"""
Hamming 7/4
@description converts normal binary string to a hamming binary string and vice versa
             this is a tutorial on hamming error code correcting. Although this is working code
              its an example of an implementation. Working implementations require more error checking of input.
"""

class Hamming:

    bytes7 = []

    string = ""

    mask7 = 0x7f
    mask3 = 0x7
    mask4 = 0xf

    def __init__(self):
        string = ""

    def get_bits(self):
        binrep = int(self.string, 2)
        count = 0
        for i in range(0, len(self.string), 7):
            self.bytes7.append(self.string[i:i+7])
            
    # converts bianary string to hamming binary string
    def to_hamming(self,string):

        res = ""

        for i in range(0, len(string), 4):
            abcd = int(string[i:i + 4], 2)
            a = self.get_a(abcd)
            b = self.get_b(abcd)
            c = self.get_c(abcd)
            d = self.get_d(abcd)

            x = a ^ b ^ d
            y = a ^ c ^ d
            z = b ^ c ^ d

            byte7 = (a << 6) | (b << 5) | (c << 4) | (d << 3) | (x << 2) | (y << 1) | z

            strbyte7 = "{0:b}".format(byte7)
            while len(strbyte7) < 7:
                strbyte7 = "0" + strbyte7

            res += strbyte7

        return res
    # fetches either a, b, c, d
    def get_a(self,abcd):
        return (abcd >> 3) & 1

    def get_b(self, abcd):
        return (abcd >> 2) & 1

    def get_c(self, abcd):
        return (abcd >> 1) & 1

    def get_d(self, abcd):
        return abcd & 1

    # possible all cases of xyz being wrong
    def xxo(self, a):
        return (a ^ 1) | (1-a)

    def xox(self,b):
        return (b ^ 1) | (1 - b)

    def oxx(self,c):
        return (c ^ 1) | (1 - c)

    def xxx(self,d):
        return (d ^ 1) | (1 - d)

    # converts hammer code to normal code
    def to_normal(self, string):
        res = ""
        val = ""
        self.string = string
        self.get_bits()

        for byte in self.bytes7:

            byte = int(byte, 2)
            xyz = self.mask3 & byte

            abcd = (byte >> 3) & self.mask4


            a = self.get_a(abcd)
            b = self.get_b(abcd)
            c = self.get_c(abcd)
            d = self.get_d(abcd)

            x = (xyz >> 2) & 1
            y = (xyz >> 1) & 1
            z = xyz & 1

            appx = a ^ b ^ d
            appy = a ^ c ^ d
            appz = b ^ c ^ d

            xr = True if x == appx else False
            yr = True if y == appy else False
            zr = True if z == appz else False

            if xr:
                val = self.o(yr,zr,a,b,c,d)
            else:
                val = self.x(yr, zr, a, b, c, d)

            while len(val) < 4:
                val = "0" + val

            res += val


        return res

    def get_abcd(self, a, b, c, d):
        return (a << 3) | (b << 2) | (c << 1) | (d << 0)

    def x(self, yr, zr, a, b, c, d):
        if yr is True & zr is True:
            return "{0:b}".format(self.get_abcd(a,b,c,d))
        elif yr is False & zr is False:
            return "{0:b}".format(self.get_abcd(a,b,c,self.xxx(d)))
        elif yr is False:
            return "{0:b}".format(self.get_abcd(self.xxo(a),b,c,d))
        else:
            return "{0:b}".format(self.get_abcd(a,self.xox(b),c,d))

    def o(self, yr, zr, a, b, c, d):
        if yr is True | zr is True:
            return "{0:b}".format(self.get_abcd(a,b,c,d))
        else:
            return "{0:b}".format(self.get_abcd(a,b,self.oxx(c),d))


print('Enter the binary to convert to normal')
x = input()

res = Hamming()
r = res.to_normal(x)

print(r)

"""

print('Enter the binary to convert to hamming')
x = input()

res = Hamming()
r = res.to_hamming(x)

print(r)

normal binary: 100111100001
hamming binary: 100100111100000001111
"""
