def move(src: list[int], tar: list[int]):
    val = src.pop()
    tar.append(val)


def do_hanota(i: int, src: list[int], buf: list[int], tar: list[int]):
    if (i == 1):
        move(src, tar)
        return
    do_hanota(i-1, src, tar, buf)
    move(src, tar)
    do_hanota(i-1, buf, src, tar)


A = [6, 5, 4, 3, 2, 1]
B = []
C = []
print(f"A:{A}\nB:{B}\nC:{C}")
do_hanota(len(A), A, B, C)
print(f"A:{A}\nB:{B}\nC:{C}")
