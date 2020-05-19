def func(arr, n):
    # [1, 2, 3, 9] - 8
    # [1, 2, 4, 4] - 8
    bool1 = False
    if n % 2 != 0:
        print(False)
    else:
        for x in range(len(arr)-1):
            set1 = set(arr[x+1:])
            if arr[x] in set1:
                if arr[x] * 2 == n:
                    print(True)
                    bool1 = True
                    break
        if bool1 == False:
            print(False)
def func2(arr, n):
    if n % 2 != 0:
        print(False)
    else:
        dict1 = dict()
        value = 1
        bool1 = False
        for x in range(len(arr)):
            if arr[x] not in dict1:
                dict1[arr[x]] = value
            else:
                dict1[arr[x]] += 1
        for x in range(len(dict1)):
            if dict1[arr[x]] == n / arr[x]:
                print(True)
                bool1 = True
                break
        if bool1 == False:
            print(False)
        




func([1, 2, 3, 9], 8)
func([1, 2, 4, 4], 8)
func([3, 7, 9, 10, 14], 11)
func([4, 8, 5, 1, 9, 5], 10)
func([4, 8, 3, 1, 9, 3], 10)
func2([1, 2, 3, 9], 8)
func2([1, 2, 4, 4], 8)
func2([3, 7, 9, 10, 14], 11)
func2([4, 8, 5, 1, 9, 5], 10)
func2([4, 8, 3, 1, 9, 3], 10)