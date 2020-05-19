def func(arr, n):
    # We have an input as an array containing integers, and also a number. 
    #The task is to check whether there is a pair of numbers in the array that sums up to the given number.
    # If there is a pair that sums up to the given number, then the output should be True, and if not, the output should be False.
    # Here are two ways of solving the puzzle with the time complexity of O(n).
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
