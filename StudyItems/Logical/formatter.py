# keyword and default arguments
def is_unique(foo_ake):
    """this will tell you if the num is unique or not"""
    foo_ake = list(foo_ake)
    foo_ake.sort()

    for i in range(len(foo_ake) - 1):
        if foo_ake[i] == foo_ake[i + 1]:
            return 0
    return 1


def hello(arg):
    print(arg)

if __name__ == "__main__":
    print(is_unique(input()))
    hello('Noor')
