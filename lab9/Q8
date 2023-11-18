leng = []
foot = []
def con(x):
    for i in range(x):
        foot.append(float(input("Enter the length in feet: ")))

def check():
    for i in range(len(foot)):
        if foot[i] < 0:
            foot[i] = float(input(f"Enter a positive value for length in feet the place {i+1}: "))
        leng.append(foot[i] / 0.3048)
    return foot, leng

def pri():
    print("{:<15} {:<15}".format("Feet", "Meters"))
    for i in range(len(foot)):
        print("{:<15.4f} {:<15.4f}".format(foot[i], leng[i]))

def main():
    N = int(input("Enter the number of lengths to convert: "))
    con(N)
    check()
    pri()

if __name__ == "__main__":
    main()
