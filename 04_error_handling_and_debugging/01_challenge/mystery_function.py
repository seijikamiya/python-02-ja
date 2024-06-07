def mystery_function(lst):
    result = lst
    for i in range(len(lst)):
        if result[i] % 2 == 0:
            result[i] = result[i] ** 2
    return result

if __name__ == "__main__":
    assert mystery_function([1, 2, 3, 4, 5]) == [1, 4, 3, 16, 5]
    assert mystery_function([4, 1, 6, 2, 10]) == [16, 1, 36, 4, 100]