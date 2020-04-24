from .rainbowwrapper import RainbowWrapper
import urllib
import time
from .alphabet import Alphabet
from .rainbowwords import RainbowWords


class HTTPUpTest:

    def __init__(self, name, url, column, rainbowwrapper, test_list=None, amount_of_tests=30):
        if len(test_list) > amount_of_tests:
            raise Exception("Test list too large, size: " + str(len(test_list)))

        self.name = name
        self.url = url
        if test_list is None:
            self.test_list = list()
        else:
            self.test_list = test_list
        self.amount_of_tests = amount_of_tests
        self.column = column
        self.rainbowwrapper = rainbowwrapper
        self.shower = RainbowWords(rainbowwrapper)
        self.online = True
        self.alphabet = Alphabet()
        self.speed = 0.2

    def test_once(self):
        start = time.time()
        try:
            code = urllib.urlopen(self.url).getcode()
        except Exception:
            code = 502
        elapsed = time.time() - start

        red, green, blue, up = self.getcolor(code)

        maxbars = self.rainbowwrapper.height

        if up and not self.online:
            self.online = True
            sentence = self.alphabet.create_string(self.name + " online")
            self.shower.show_sentence(sentence, self.speed)
            return False
        elif up:
            self.test_list = [elapsed] + self.test_list
            if len(self.test_list) > self.amount_of_tests:
                self.test_list.pop()

            average = self.average()

            if elapsed > average:
                for i in range(0, self.rainbowwrapper.height-1):
                    if elapsed < average:
                        pass
                    else:
                        elapsed = elapsed - average
                        maxbars = maxbars - 1
        elif not up and self.online:
            self.online = False
            sentence = self.alphabet.create_string(self.name + " offline")
            self.shower.show_sentence(sentence, self.speed)
            return False

        for i in range(0, self.rainbowwrapper.height):
            if i < maxbars:
                self.rainbowwrapper.set_pixel(self.column, i, red, green, blue)
            else:
                self.rainbowwrapper.set_pixel(self.column, i, 0, 0, 0)
        self.rainbowwrapper.show()
        return True

    def getcolor(self, code):
        if code >= 100 and code < 200:
            return 255, 255, 0, False
        elif code == 200:
            return 0, 255, 0, True
        elif code > 200 and code < 300:
            return 0, 255, 0, True
        elif code >= 300 and code < 400:
            return 255, 150, 50, False
        elif code >= 400 and code < 500:
            return 255, 0, 0, False
        elif code >= 500 and code < 600:
            return 255, 0, 0, False
        else:
            return 0, 0, 0, False

    def average(self):
        if len(self.test_list) == 0:
            return 0

        total = 0
        for i in self.test_list:
            total = total + i
        return total/len(self.test_list)