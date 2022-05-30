# Find the Runner-Up Score!

if __name__ == '__main__':
    n = int(input('Enter the number: '))
    arr = map(int, input().split())
    arr = list(dict.fromkeys(arr))
    arr.sort()
    arr.reverse()
    print(arr[1])
