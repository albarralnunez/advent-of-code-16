import os
import yaml
from libs import commons


class Screen(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.screen = [[0 for _ in range(x)] for _ in range(y)]
        dir_name = os.path.dirname(os.path.abspath(__file__))
        alphabet = os.path.join(dir_name, 'alphabet.YAML')
        with open(alphabet, 'r') as stream:
            self.alphabet = yaml.load(stream)

    def rect(self, x, y):
        for i in range(y):
            for j in range(x):
                self.screen[i][j] = 1

    def rotate_row(self, y, n):
        row = list(self.screen[y])
        for x in range(len(row)):
            disp = (x + n) % len(row)
            self.screen[y][disp] = row[x]

    def rotate_column(self, x, n):
        column = [row[x] for row in self.screen]
        for row in range(len(self.screen)):
            disp = (row + n) % len(self.screen)
            self.screen[disp][x] = column[row]

    def number_pixels_on(self):
        return len(filter(lambda x: x, commons.flatten(self.screen)))

    def pick_letter(self, index):
        col = (index * 5) % self.x
        row = (index / self.x) * 6
        return [[str(z) for z in i[col:col+5]] for i in self.screen[row:row+6]]

    @staticmethod
    def print_letter(letter):
        print '\n'.join([' '.join(x) for x in letter])

    def print_screen(self):
        for x in range((self.x*self.y)/(5*6)):
            letter = self.pick_letter(x)
            print '-> ', x+1, ' <-'
            print self.print_letter(letter)

    def decode(self):
        screen = ''
        for x in range((self.x*self.y)/(5*6)):
            letter = self.pick_letter(x)
            code = ''.join([''.join(x) for x in letter])
            screen += self.alphabet[code]
        return screen
