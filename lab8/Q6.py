import math

def ask():
    return float(input("Enter degree of angles: "))
def con():
     return ask() * math.pi / 180
def out():
    print(f"the value of convert angle into a radians equal {con()}")
def main():
    out()

if __name__ == "__main__":
    main()
