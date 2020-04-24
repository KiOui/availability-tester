import pyping


class PingUpTest:

    def __init__(self, name, ip, column, row, rainbowrapper):

        self.name = name
        self.ip = ip
        self.column = column
        self.row = row
        self.rainbowrapper = rainbowrapper

    def test_once(self):
        response = pyping.ping(self.ip)

        r, g, b, up = self.getcolor(response.ret_code)
        self.rainbowrapper.set_pixel(self.column, self.row, r, g, b)
        self.rainbowrapper.show()

    def getcolor(self, code):
        if code == 0:
            return 0, 255, 0, True
        else:
            return 255, 0, 0, False
