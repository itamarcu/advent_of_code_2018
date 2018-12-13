from typing import List


class Cart:
    def __init__(self, loc: complex, di: complex, cr: int, index):
        self.loc = loc
        self.di = di
        self.cr = cr
        self.index = index
        self.dead = False


def solve_a(input_file_lines: List[str]) -> str:
    mapp = {}
    carts = []
    for y, line in enumerate(input_file_lines):
        for x, char in enumerate(line):
            if char == "\n":
                continue
            if char in "<v>^":
                direction = {
                    "<": -1,
                    "v": +1j,
                    ">": +1,
                    "^": -1j,
                }[char]
                carts.append(Cart(x + y * 1j, direction, 0, len(carts)))  # location, direction, crossings
                part = {
                    "<": "-",
                    "v": "|",
                    ">": "-",
                    "^": "|",
                }[char]
            else:
                part = char
            mapp[(x + y * 1j)] = part
    tick = 0
    while True:
        tick += 1
        carts.sort(key=lambda c: (c.loc.imag, c.loc.real))
        for cart in carts:
            cart.loc += cart.di
            if any(c2.loc == cart.loc for c2 in carts if c2.index != cart.index):
                return str(int(cart.loc.real)) + "," + str(int(cart.loc.imag))
            part = mapp[cart.loc]
            if part == "\\":
                if cart.di.real == 0:
                    cart.di *= -1j  # ↑↖←
                else:
                    cart.di *= +1j  # ←↖↑
            if part == "/":
                if cart.di.real == 0:
                    cart.di *= +1j
                else:
                    cart.di *= -1j
            if part == "+":
                cart.di *= -1j * 1j ** cart.cr
                cart.cr = (cart.cr + 1) % 3



def solve_b(input_file_lines: List[str]) -> str:
    mapp = {}
    carts = []
    for y, line in enumerate(input_file_lines):
        for x, char in enumerate(line):
            if char == "\n":
                continue
            if char in "<v>^":
                direction = {
                    "<": -1,
                    "v": +1j,
                    ">": +1,
                    "^": -1j,
                }[char]
                carts.append(Cart(x + y * 1j, direction, 0, len(carts)))  # location, direction, crossings
                part = {
                    "<": "-",
                    "v": "|",
                    ">": "-",
                    "^": "|",
                }[char]
            else:
                part = char
            mapp[(x + y * 1j)] = part
    tick = 0
    while True:
        tick += 1
        carts.sort(key=lambda c: (c.loc.imag, c.loc.real))
        for ci in range(len(carts)):
            cart = carts[ci]
            if cart.dead:
                continue
            cart.loc += cart.di
            for ci2 in range(len(carts)):
                if ci != ci2 and cart.loc == carts[ci2].loc and not carts[ci2].dead:
                    print("BOOM!", cart.index, carts[ci2].index)
                    cart.dead = True
                    carts[ci2].dead = True
            if cart.dead:
                continue
            part = mapp[cart.loc]
            if part == "\\":
                if cart.di.real == 0:
                    cart.di *= -1j  # ↑↖←
                else:
                    cart.di *= +1j  # ←↖↑
            if part == "/":
                if cart.di.real == 0:
                    cart.di *= +1j
                else:
                    cart.di *= -1j
            if part == "+":
                cart.di *= -1j * 1j ** cart.cr
                cart.cr = (cart.cr + 1) % 3
        carts = [c for c in carts if not c.dead]
        print(len(carts))
        if len(carts) == 1:
            cart = carts[0]
            return str(int(cart.loc.real)) + "," + str(int(cart.loc.imag))
