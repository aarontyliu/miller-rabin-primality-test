from math import log


def is_prime(n: int) -> int:
    """Perfome the Miller's Test (deterministic primality testing algorithm)."""
    assert n > 0, "Please insert a valid number!"

    if n == 1:
        return 0
    elif n < 4:
        return 1
    elif not n % 2:
        return 0
    else:
        d = n - 1
        r = 0
        while not d % 2:
            d //= 2
            r += 1
        if n < 2047:
            s_a = [2]
        elif n < 1373653:
            s_a = [2, 3]
        elif n < 9080191:
            s_a = [31, 73]
        elif n < 25326001:
            s_a = [2, 3, 5]
        else:
            s_a = range(2, int(min(n - 2, 2 * pow(log(n), 2))) + 1)
        for a in s_a:
            x = pow(a, d, n)
            if x == 1 or x == n - 1:
                continue
            for _ in range(r - 1):
                x = pow(x, 2, n)
                if x == n - 1:
                    break
            else:
                return 0
        return 1
