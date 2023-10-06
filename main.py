# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def bubble_sort(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers)-i):
            if j == len(numbers)-1:
                break
            if numbers[j]>numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    for i in range(len(numbers)):
        print(numbers[i], end=" ")

def selection_sort(numbers):
    min = 0
    for i in range(len(numbers)):
        min = numbers[i]
        for j in range(i, len(numbers)):
            if min>numbers[j]:
                min = numbers[j]
        for j in range(len(numbers)):
            if numbers[j]==min:
                numbers[j]=numbers[i]
        numbers[i]=min

    for i in range(len(numbers)):
        print(numbers[i], end=" ")

def insertion_sort(numbers):
    i = 0
    while i in range(len(numbers)):
        if i == len(numbers)-1:
            break
        if numbers[i]>numbers[i+1]:
            numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
        if i > 0 and numbers[i]<numbers[i-1]:
            numbers[i-1], numbers[i] = numbers[i], numbers[i-1]
            i -= 1
            continue
        i += 1

    for i in range(len(numbers)):
        print(numbers[i], end=" ")


def merge_sort(numbers):
    tree = 0
    som = {}
    def check_sorted(arr):
        sorted = 0
        for i in range(len(arr)):
            if i == len(arr)-1:
                break
            if arr[i] < arr[i+1]:
                sorted = 0
            elif arr[1]>arr[i+1]:
                sorted = 1
                break

    def divide(arr, som):
        nonlocal tree
        mid = round(len(arr) / 2)
        arr1 = []
        arr2 = []
        if len(arr) == 1:
            pass
        else:
            for i in range(len(arr)):
                if i < mid:
                    arr1.append(arr[i])
                else:
                    arr2.append(arr[i])
            key = "arr"+str(tree)
            som[key] = arr1
            tree+=1
            divide(som[key], som)
            key = "arr" + str(tree)
            som[key] = arr2
            tree+=1
            divide(som[key], som)
    divide(numbers, som)

    def delete(som):
        for key, values in som.items():
            if len(values)!=1:
                som.pop(key)
                break

    def merge(som):
        nonlocal numbers
        numbers.clear()
        for value in som.values():
            numbers.append(value)
            numbers.sort()

    for i in range(12):
        delete(som)

    merge(som)
    print(numbers)


def quick_sort(numbers):
    p , i, j = 0, 1, len(numbers)-1
    direction = 'i'

    sorted_array = numbers.copy()
    sorted_array.sort()
    while numbers!=sorted_array:
        if i>j:
            j = p - 1
            p=0
            i=1
            direction='i'
            if i == j - 1:
                p = i
                direction = 'j'


        if numbers[p]>numbers[i] and direction=='i':
            numbers[p], numbers[i] = numbers[i], numbers[p]
            p=i
            i+=1
        elif numbers[p]<numbers[i] and direction=='i' and p>i:
            numbers[p], numbers[i] = numbers[i], numbers[p]
            p = i
            i += 1
        elif numbers[p]<numbers[i]:
            direction='j'
        if direction=='j':
            if numbers[p]>numbers[j] and j>p:
                numbers[p], numbers[j] = numbers[j], numbers[p]
                p = j
                j-=1
            elif numbers[p]<numbers[j] and j<p:
                numbers[p], numbers[j] = numbers[j], numbers[p]
                p = j
                j -= 1
            elif numbers[p]<numbers[j] or numbers[p]>numbers[j]:
                direction='i'

    print(numbers)







def binary_search(sorted_array, key):
    low, high = 0, len(sorted_array)-1
    mid = round((low+high)/2)
    found=False
    while low<=high:
        if sorted_array[mid]==key:
            print("The Key is found at index ", mid)
            found=True
            break
        if key < sorted_array[mid]:
            high = mid-1
            mid=round((low+high)/2)
        if key>sorted_array[mid]:
            low = mid+1
            mid=round((low+high)/2)
    if found==False:
        print("The element is not present in the array")


def linear_search(numbers, key):
    for i in range(len(numbers)):
        if numbers[i]==key:
            print("Key Found")
            exit(0)
    print("Key not found")





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #merge_sort([95, 25, 65, 20, 15, 84, 4])
    quick_sort([20, 5, 3, 18, 55, 16])
    #linear_search([1, 2, 6, 14, 15, 18, 22, 34, 45, 56], 18)
    #binary_search([1, 2, 6, 14, 15, 18, 22, 34, 45, 56], 98)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
