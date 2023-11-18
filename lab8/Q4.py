def polar(x, y):
    r = math.sqrt(x ** 2 + y ** 2)
    rad = math.atan2(y, x)
    theta = math.degrees(rad)
    return r, theta

def main():
    a = float(input("Enter the x coordinate: "))
    b = float(input("Enter the y coordinate: "))

    print(polar(a, b))

if __name__ == "__main__":
    main()
