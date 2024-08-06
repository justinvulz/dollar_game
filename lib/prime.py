ODD_PRIME = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
             41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
PRIME = [2] + ODD_PRIME
PRIME_FACTOR = {}


def load_prime():
    global ODD_PRIME
    with open("./lib\prime.txt", encoding="utf-8") as f:
        for line in f:
            ODD_PRIME.append(int(line.strip()))


def fill_prime(n: int):

    for i in range(ODD_PRIME[-1]+2, n+1, 2):
        for p in ODD_PRIME:
            if p*p > i:
                ODD_PRIME.append(i)
                break
            if i % p == 0:
                break

    global PRIME
    PRIME = [2] + ODD_PRIME


def prime_factor(n: int) -> list[tuple[int, int]]:
    global PRIME_FACTOR
    global PRIME
    nn = n
    if n in PRIME_FACTOR:
        return PRIME_FACTOR[n]
    ans = []
    fill_prime(n)
    for p in PRIME:
        if p > n:
            break
        if n % p == 0:
            count = 0
            while n % p == 0:
                count += 1
                n //= p
            ans.append((p, count))
    PRIME_FACTOR[nn] = ans
    return ans
