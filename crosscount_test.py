import unittest

def crosscount(v, people, links):

    loc = dict([(people[i], (v[i * 2], v[i * 2 + 1])) for i in range(0, len(people))])
    total = 0


    for i in range(len(links)):
        for j in range(i + 1, len(links)):


            (x1, y1), (x2, y2) = loc[links[i][0]], loc[links[i][1]]
            (x3, y3), (x4, y4) = loc[links[j][0]], loc[links[j][1]]

            den = (y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1)


            if den == 0: continue


            ua = ((x4 - x3) * (y1 - y3) - (y4 - y3) * (x1 - x3)) / float(den)
            ub = ((x2 - x1) * (y1 - y3) - (y2 - y1) * (x1 - x3)) / float(den)


            if ua > 0 and ua < 1 and ub > 0 and ub < 1:
                total += 1
    return total

class TestCrosscount(unittest.TestCase):

    def test_simple_case(self):
        people = ['Charlie', 'Augustus', 'Veruca', 'Violet', 'Mike', 'Joe', 'Willy', 'Miranda']
        links = []
        v = [0, 0, 10, 10, 20, 20, 30, 30, 40, 40, 50, 50, 60, 60, 70, 70]
        self.assertEqual(crosscount(v, people, links), 0)

    def test_no_crossing_lines(self):
        people = ['Augustus', 'Charlie', 'Veruca', 'Violet']
        links = [('Augustus', 'Charlie'),
                 ('Charlie', 'Augustus'),
                 ('Veruca', 'Violet'),
                 ('Violet', 'Veruca')
                 ]
        v = [0, 0, 50, 50, 100, 100, 200, 200]
        self.assertEqual(crosscount(v, people, links), 0)

    def test_cross_lines(self):
        people = ['Augustus', 'Charlie', 'Veruca', 'Violet']
        links = [('Augustus', 'Charlie'),
                 ('Charlie', 'Augustus'),
                 ('Veruca', 'Violet'),
                 ('Violet', 'Veruca')
                 ]
        v = [0, 100, 300, 100, 190, 150, 170, 0]
        self.assertEqual(crosscount(v, people, links), 4)

    def test_two_cross_another_not(self):
        people = ['Augustus', 'Charlie', 'Veruca', 'Violet', 'Mike', 'Joe']
        links = [('Augustus', 'Charlie'),
                 ('Charlie', 'Augustus'),
                 ('Veruca', 'Violet'),
                 ('Violet', 'Veruca'),
                 ('Mike', 'Joe'),
                 ('Joe', 'Veruca')
                 ]
        v = [0, 100, 170, 150, 250, 150, 250, 0, 100, 100, 200, 200]
        self.assertEqual(crosscount(v, people, links), 2)

    def test_two_crossings(self):
        people = ['Augustus', 'Charlie', 'Veruca', 'Violet', 'Mike', 'Joe']
        links = [('Augustus', 'Charlie'),
                 ('Charlie', 'Augustus'),
                 ('Veruca', 'Violet'),
                 ('Violet', 'Veruca'),
                 ('Mike', 'Joe'),
                 ('Joe', 'Veruca')
                 ]
        v = [0, 100, 240, 170, 250, 150, 250, 0, 100, 100, 200, 200]
        self.assertEqual(crosscount(v, people, links), 4)

if __name__ == '__main__':
    unittest.main()