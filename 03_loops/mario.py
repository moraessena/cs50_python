def main():
    print_square(3)


def print_column(height):
    print("#\n" * 3, end="")


def print_square(size):
    for _ in range(size):
        print_row(size)


def print_row(size):
    print("#" * size)


main()
