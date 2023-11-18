def sqrt(x):
    if x == 1:
      return 1
    return x**2 + sqrt(x-1)

def main():
    a = int(input("Enter th number: "))
    print(sqrt(a))
if __name__ =="__main__":
    main()
