import sys


MODULO = 10007


def count_palindrome_completions(s: str) -> int:
    n = len(s)
    total = 1
    i, j = 0, n - 1

    while i < j:
        left = s[i]
        right = s[j]

        if left != '?' and right != '?':
            if left != right:
                return 0
        elif left == '?' and right == '?':
            total = (total * 26) % MODULO
        # else exactly one is '?', only 1 way (match the known one)

        i += 1
        j -= 1

    if n % 2 == 1 and s[n // 2] == '?':
        total = (total * 26) % MODULO

    return total


def main() -> None:
    # Read all non-empty lines and process each as a separate test case
    data = sys.stdin.read().splitlines()
    for line in data:
        s = line.strip()
        if not s:
            continue
        print(count_palindrome_completions(s))


if __name__ == "__main__":
    main()

