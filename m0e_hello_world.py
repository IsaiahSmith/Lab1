import math

def main():
    print(test(10))

def test(n):
    s = ''
    for k in range(1, n + 1):
        s = s + str(k)
    return s

main()
