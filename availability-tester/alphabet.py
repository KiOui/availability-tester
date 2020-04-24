class Alphabet:
    def __init__(self):
        self.letters = [
            [[False, True, False],
             [True, False, True],
             [True, True, True],
             [True, False, True]],
            [[True, True, True],
             [True, True, False],
             [True, False, True],
             [True, True, False]],
            [[False, True, True],
             [True, False, False],
             [True, False, False],
             [False, True, True]],
            [[True, True, False],
             [True, False, True],
             [True, False, True],
             [True, True, False]],
            [[True, True, True],
             [True, True, False],
             [True, False, False],
             [True, True, True]],
            [[True, True, True],
             [True, True, False],
             [True, False, False],
             [True, False, False]],
            [[False, True, True],
             [True, False, False],
             [True, False, True],
             [False, True, True]],
            [[True, False, True],
             [True, True, True],
             [True, False, True],
             [True, False, True]],
            [[True, True, True],
             [False, True, False],
             [False, True, False],
             [True, True, True]],
            [[True, True, True],
             [False, False, True],
             [True, False, True],
             [False, True, False]],
            [[True, False, True],
             [True, True, False],
             [True, False, True],
             [True, False, True]],
            [[True, False, False],
             [True, False, False],
             [True, False, False],
             [True, True, True]],
            [[True, True, True],
             [True, True, True],
             [True, False, True],
             [True, False, True]],
            [[True, True, False],
             [True, False, True],
             [True, False, True],
             [True, False, True]],
            [[False, True, False],
             [True, False, True],
             [True, False, True],
             [False, True, False]],
            [[True, True, True],
             [True, False, True],
             [True, True, True],
             [True, False, False]],
            [[False, True, False],
             [True, False, True],
             [True, True, True],
             [False, True, True]],
            [[True, True, False],
             [True, False, True],
             [True, True, True],
             [True, False, True]],
            [[True, True, True],
             [True, True, False],
             [False, False, True],
             [True, True, True]],
            [[True, True, True],
             [False, True, False],
             [False, True, False],
             [False, True, False]],
            [[True, False, True],
             [True, False, True],
             [True, False, True],
             [False, True, False]],
            [[True, False, True],
             [True, False, True],
             [True, True, False],
             [True, False, False]],
            [[True, False, True],
             [True, False, True],
             [True, True, True],
             [True, True, True]],
            [[True, False, True],
             [False, True, False],
             [True, False, True],
             [True, False, True]],
            [[True, False, True],
             [False, True, False],
             [False, True, False],
             [False, True, False]],
            [[True, True, True],
             [False, True, False],
             [True, False, False],
             [True, True, True]]
        ]

        self.blank = [[False],
                      [False],
                      [False],
                      [False]]
        self.dot = [[False],
                    [False],
                    [False],
                    [True]]

        self.numbers = [[[True, True, True],
                         [True, False, True],
                         [True, False, True],
                         [True, True, True]],
                        [[True, True, False],
                         [False, True, False],
                         [False, True, False],
                         [True, True, True]],
                        [[True, True, False],
                         [False, False, True],
                         [False, True, False],
                         [True, True, True]],
                        [[True, True, False],
                         [False, True, True],
                         [False, False, True],
                         [True, True, False]],
                        [[True, False, True],
                         [True, True, True],
                         [False, False, True],
                         [False, False, True]],
                        [[True, True, True],
                         [True, True, False],
                         [False, False, True],
                         [False, True, False]],
                        [[False, True, True],
                         [True, False, False],
                         [True, True, True],
                         [True, True, False]],
                        [[True, True, True],
                         [False, False, True],
                         [False, True, False],
                         [True, False, False]],
                        [[True, True, True],
                         [True, True, True],
                         [True, False, True],
                         [True, True, True]],
                        [[False, True, True],
                         [True, True, True],
                         [False, False, True],
                         [True, True, False]]
                        ]

    def append_2D_list(self, sentence, letter):
        for i in range(0, len(letter)):
            sentence[i] = sentence[i] + letter[i]

    def create_string(self, sentence):
        sentence_list = [[], [], [], []]

        for letter in sentence:
            if letter == '.':
                self.append_2D_list(sentence_list, self.dot)
            elif letter == ' ':
                self.append_2D_list(sentence_list, self.blank)
            elif ord(letter) >= ord('a') and ord(letter) <= ord('z'):
                self.append_2D_list(sentence_list, self.letters[ord(letter)-ord('a')])
            elif ord(letter) >= ord('0') and ord(letter) <= ord('9'):
                self.append_2D_list(sentence_list, self.numbers[ord(letter)-ord('0')])
            else:
                pass
            self.append_2D_list(sentence_list, self.blank)
        return sentence_list

    def print_string(self, sentence):
        for l in sentence:
            toprint = ""
            for item in l:
                if item:
                    toprint = toprint + "x"
                else:
                    toprint = toprint + " "
            print(toprint)