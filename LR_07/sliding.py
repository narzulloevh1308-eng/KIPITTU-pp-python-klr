def max_elements_greater_than_x(arr, k, x):
    """
    Возвращает максимальное количество элементов > x
    в любом окне длины k.
    """
    if not isinstance(arr, list):
        raise TypeError("arr должен быть списком")
    if not isinstance(k, int) or not isinstance(x, (int, float)):
        raise TypeError("k должен быть int, x — число")
    if k <= 0:
        raise ValueError("k должен быть больше 0")
    if k > len(arr):
        raise ValueError("k не может быть больше длины списка")

    count = sum(1 for i in range(k) if arr[i] > x)
    max_count = count

    for right in range(k, len(arr)):
        if arr[right] > x:
            count += 1
        if arr[right - k] > x:
            count -= 1
        max_count = max(max_count, count)

    return max_count
