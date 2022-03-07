while 1:
    x, y, z =map(int, input().split())
    if x > y > z or x > z > y:
        if x*x == z*z + y*y:
            print("right")
        else:
            print("wrong")
    elif y > x > z or y > z > x:
        if y*y == x*x + z*z:
            print("right")
        else:
            print("wrong")
    elif z > x > y or z > y > x:
        if z*z == x*x + y*y:
            print("right")
        else:
            print("wrong")
    elif x == 0 and y == 0 and z == 0:
        break