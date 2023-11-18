def GetPositiveArray():
    x = input().split()
    return x


def main():
    Id = GetPositiveArray('Enter ID List:')
    Wait = GetPositiveArray('Enter Waiting Time List:')


if __name__ == "__main__":
    main()

Avg = ComputeAverage(Wait)
    print('Average Waiting time = %.2f\n' %Avg)
    IdLongWait = GetIDLongWait(Id, Wait, Avg)
    print('IDs for customers who waited longer than average are:')
    print(IdLongWait)
