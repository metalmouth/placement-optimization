import math
import optimization
from PIL import Image, ImageDraw


people = ['Augustus', 'Charlie', 'Veruca', 'Violet', 'Mike', 'Joe']
links = [('Augustus', 'Charlie'),
         ('Charlie', 'Augustus'),
         ('Veruca', 'Violet'),
         ('Violet', 'Veruca'),
         ('Mike', 'Joe'),
         ('Joe', 'Veruca')
         ]


def crosscount(v):

    loc = dict([(people[i], (v[i * 2], v[i * 2 + 1])) for i in range(0, len(people))])
    total = 0


    for i in range(len(links)):
        for j in range(i + 1, len(links)):

            # Get the locations
            (x1, y1), (x2, y2) = loc[links[i][0]], loc[links[i][1]]
            (x3, y3), (x4, y4) = loc[links[j][0]], loc[links[j][1]]

            den = (y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1)

            if den == 0: continue

            ua = ((x4 - x3) * (y1 - y3) - (y4 - y3) * (x1 - x3)) / float(den)
            ub = ((x2 - x1) * (y1 - y3) - (y2 - y1) * (x1 - x3)) / float(den)


            if ua > 0 and ua < 1 and ub > 0 and ub < 1:
                total += 1
    for i in range(len(people)):
        for j in range(i + 1, len(people)):
            # Получить позиции обоих узлов
            (x1, y1), (x2, y2) = loc[people[i]], loc[people[j]]
            # Вычислить расстояние между ними
            dist = math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))
        # Штраф, если расстояние меньше 50 пикселей
        if dist < 50:
            total += (1.0 - (dist / 50.0))
    print("total=", total)

    return total


def drawnetwork(sol):
    jpeg = 'network_diagram.jpg'
    # Create the image
    img = Image.new('RGB', (400, 400), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    # Create the position dict
    pos = dict([(people[i], (sol[i * 2], sol[i * 2 + 1])) for i in range(0, len(people))])

    # Draw links
    for (a, b) in links:
        draw.line((pos[a], pos[b]), fill=(255, 0, 0))

    # draw people
    for n, p in pos.items():
        draw.text(p, n, (0, 0, 0))
    img.save(jpeg, 'JPEG')


domain = [(10, 370)] * (len(people) * 2)

sol = optimization.randomoptimize(domain, crosscount)
sol = optimization.annealingoptimize(domain, crosscount, step=50, cool=0.99)
print(sol)
drawnetwork(sol)


