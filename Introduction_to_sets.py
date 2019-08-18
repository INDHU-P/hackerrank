def average(array):
    total = 0
    array = set(array)
    # your code goes here
    for i in array:
        total += i
    return (total/(len(array)))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
