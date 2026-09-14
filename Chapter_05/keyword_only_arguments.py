# This program demonstrates keyword-only function arguments.

def main():
    total = sum(a=1, b=2, c=3, d=4)
    print(total)

def sum(*, a, b, c, d):
    return a + b + c + d

if __name__ == '__main__':
    main()