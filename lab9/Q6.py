def sum_list(lst):
    if lst == []:
        return 0
    else:
        return lst[0] + sum_list(lst[1:])

def main():
    N = input("Enter the sequence of numbers separated by space: ").split()
    a = [int(i) for i in N]
    print(sum_list(a))

if __name__ == "__main__":
    main()
