def conv(f):
    c = (f - 32) * 5/9
    k = c + 273.15
    return c, k
def main():
    x = float(input("Enter temperature in Fahrenheit: "))
    res= conv(x)
    print(f"{x} degrees Fahrenheit is equal to {res} degrees Celsius and Kelvin.")
if __name__ == "__main__":
    main()
