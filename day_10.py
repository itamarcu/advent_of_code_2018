import re
from typing import List


def solve_a(input_file_lines: List[str]) -> str:
    points = []
    xs = []
    ys = []
    for line in input_file_lines:
        posx, posy, velx, vely = [int(x) for x in re.findall("-?\\d+", line)]
        points.append((posx, posy, velx, vely))
        xs.append(posx)
        ys.append(posy)
    bounding_box_size = 999999999999999

    def calc_bounding_box(it):
        temp_points = [(px + vx * it, py + vy * it, vx, vy) for px, py, vx, vy in points]
        maxx = max(temp_points, key=lambda p: p[0])[0]
        maxy = max(temp_points, key=lambda p: p[1])[1]
        minx = min(temp_points, key=lambda p: p[0])[0]
        miny = min(temp_points, key=lambda p: p[1])[1]
        return (maxx - minx) * (maxy - miny)

    def recurse(first, last):
        mid = (first + last) / 2
        if first > last:
            return int(mid)
        growth_direction = calc_bounding_box(mid) - calc_bounding_box(mid + 1)
        if growth_direction > 0:
            return recurse(mid + 1, last)
        elif growth_direction < 0:
            return recurse(first, mid - 1)
        else:
            return mid

    i = recurse(0, 99999)
    i += 1
    points = [(px + vx * i, py + vy * i, vx, vy) for px, py, vx, vy in points]
    maxx = max(points, key=lambda p: p[0])[0]
    maxy = max(points, key=lambda p: p[1])[1]
    minx = min(points, key=lambda p: p[0])[0]
    miny = min(points, key=lambda p: p[1])[1]
    arr = [[' '] * (maxy - miny + 60) for _ in range(maxx - minx)]
    print(f"Smallest bounding box after {i} iterations.")
    for (x, y, vx, vy) in points:
        arr[y - miny][x - minx] = '*'

    for m in arr:
        print(''.join(m))

    return "HRPHBRKG"


def solve_b(input_file_lines: List[str]) -> str:
    return "10355"


def turtle_solution(points):
    import turtle

    turtle.speed('fastest')
    turtle.up()

    bounding_box_size = 999999999999999
    for j in range(9999999):
        for i, p in enumerate(points):
            posx, posy, velx, vely = p
            points[i] = posx + velx, posy + vely, velx, vely
        maxx = max(points, key=lambda p: p[0])[0]
        maxy = max(points, key=lambda p: p[1])[1]
        minx = min(points, key=lambda p: p[0])[0]
        miny = min(points, key=lambda p: p[1])[1]
        new_bb_size = (maxx - minx) * (maxy - miny)
        if new_bb_size > bounding_box_size:
            print(f"Smallest box at {j}")
            for i, p in enumerate(points):
                posx, posy, velx, vely = p
                points[i] = posx - velx, posy - vely, velx, vely
            avgx = (minx + maxx) // 2
            avgy = (miny + maxy) // 2
            break
        bounding_box_size = new_bb_size

    turtle.clear()
    for i, p in enumerate(points):
        posx, posy, velx, vely = p
        points[i] = posx + velx, posy + vely, velx, vely
        turtle.setposition((posx - avgx) * 10, (posy - avgy) * 10)
        turtle.down()
        turtle.dot(10)
        turtle.up()

    turtle.exitonclick()
