def sum_list(lst):
    if lst == []:
        return 0
    else:
        return 1 + sum_list(lst[1:])

def main():
    N = input("Enter the sequence of numbers separated by space: ").split()
    print(sum_list(N))

if __name__ == "__main__":
    main()
