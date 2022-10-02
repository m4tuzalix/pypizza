class Figures:
    magazzine = [5, 10, 8, 7, 9, 3, 22]

    def __init__(self, start):
        self.start = start

    def looking_position(self):
        try:
            return [x for x in range(len(self.magazzine)) if self.magazzine[x] == self.start][0]
        except IndexError:
            return 'Not found'


figures = Figures(330)
print(figures.looking_position())