def guess_number(range_top: int, x: int) -> int:
    steps = 0
    l = 0
    t = range_top
    m = -1
    while m != x:
        steps += 1
        m = int(l + (t - l) / 2)
        if m < x:
            l = m
        elif m > x:
            t = m
        

        
    return steps

assert guess_number(100, 50) == 1
assert guess_number(100, 25) == 2
assert guess_number(100, 75) == 2
assert guess_number(100, 40) == 5
assert guess_number(100, 67) == 7
print("success")
