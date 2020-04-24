import time


class RainbowWords:

    def __init__(self, rainbowrapper):
        self.rainbowrapper = rainbowrapper

    def show_word(self, word):
        if len(word) != 4 or len(word[0]) != 8 or len(word[1]) != 8 or len(word[2]) != 8 or len(word[3]) != 8:
            raise Exception("Word length not correct!")

        self.ready_word(word)

        for height in range(0, 4):
            for width in range(0, 8):
                if word[height][width]:
                    self.rainbowrapper.set_pixel(width, height, 255, 255, 255)
                else:
                    self.rainbowrapper.set_pixel(width, height, 0, 0, 0)

        self.rainbowrapper.show()

    def get_word(self, sentence, begin):
        retlist = []
        for l in sentence:
            toadd = []
            for i in range(begin, begin+8):
                toadd = toadd + [l[i]]
            retlist = retlist + [toadd]

        return retlist

    def show_sentence(self, sentence, speed):
        if len(sentence) != 4:
            raise Exception("Sentence length not correct!")

        firstwait = True
        max_l = self.max_length(sentence)

        self.append_lengths(sentence, max_l)

        for i in range(0, max_l - 8):
            to_print = self.get_word(sentence, i)
            self.show_word(to_print)
            if firstwait:
                time.sleep(speed*3)
                firstwait = False
            else:
                time.sleep(speed)

        time.sleep(speed*3)
        self.make_blank()

    def append_lengths(self, sentence, maximum):
        for l in sentence:
            while len(l) < maximum:
                l = l + [False]

    def max_length(self, sentence):
        length = 0
        for l in sentence:
            if length < len(l):
                length = len(l)
        return length

    def ready_word(self, word):
        for l in word:
            l.reverse()

        word.reverse()

    def make_blank(self):
        for height in range(0, 4):
            for width in range(0, 8):
                self.rainbowrapper.set_pixel(width, height, 0, 0, 0)
        self.rainbowrapper.show()
