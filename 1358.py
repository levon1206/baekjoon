def in_square(w, h, x, y, px, py):
    X = (x <= px) and (px <= x + w)
    Y = (y <= py) and (py <= y + h)
    return X and Y

def in_circle(ox, oy, px, py, r):
    d = ((px-ox)**2 + (py-oy)**2)**(1/2)
    return d <= r

w, h, x, y, p = map(int, input().split())
result = 0
for _ in range(p):
    px, py = map(int, input().split())
    r = h // 2
    if in_square(w, h, x, y, px, py):
        result += 1
    elif in_circle(x, y + r, px, py, r):
        result += 1
    elif in_circle(x + w, y + r, px, py, r):
        result += 1
print(result)