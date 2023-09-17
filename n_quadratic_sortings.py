""" n quadratic sortings """


def insert_sort(arr: list):
    """ Insert sorting func """
    for top in range(1, len(arr)):
        k = top
        while k > 0 and arr[k] < arr[k-1]:
            arr[k], arr[k-1] = arr[k-1], arr[k]
            k -= 1


def choice_sort(arr: list):
    """ Choice sorting func """
    for pos in range(0, len(arr)-1):
        for k in range(pos, len(arr)):
            if arr[k] < arr[pos]:
                arr[pos], arr[k] = arr[k], arr[pos]


def bubble_sort(arr: list):
    """ Bubble sorting func """
    for bypass in range(0, len(arr)):
        for k in range(1, len(arr) - bypass):
            if arr[k] < arr[k-1]:
                arr[k], arr[k-1] = arr[k-1], arr[k]


def test_func(sort_algorithm):
    """ Test sorting algorithm """

    print("Testing" + sort_algorithm.doc)

    print("Case #1: ", end='')
    A = [2, 4, 3, 5, 1]
    A_sorted = [1, 2, 3, 4, 5]
    sort_algorithm(A)
    print("Pass" if A == A_sorted else "Fail")

    print("Case #2: ", end='')
    A = list(range(10, 20)) + list(range(0, 10))
    A_sorted = list(range(0, 20))
    sort_algorithm(A)
    print("Pass" if A == A_sorted else "Fail")

    print("Case #3: ", end='')
    A = [20, 10, 30, 20, 30]
    A_sorted = [10, 20, 20, 30, 30]
    sort_algorithm(A)
    print("Pass" if A == A_sorted else "Fail")


if name == "main":
    test_func(insert_sort)
    test_func(choice_sort)
    test_func(bubble_sort)
