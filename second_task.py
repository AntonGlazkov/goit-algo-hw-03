import turtle


def koch_segment(length, level):
    if level == 0:
        turtle.forward(length)
    else:
        length /= 3.0
        koch_segment(length, level - 1)
        turtle.left(60)
        koch_segment(length, level - 1)
        turtle.right(120)
        koch_segment(length, level - 1)
        turtle.left(60)
        koch_segment(length, level - 1)


def koch_snowflake(length, level):
    for _ in range(3):
        koch_segment(length, level)
        turtle.right(120)


def main():
    level = int(input("Введіть рівень рекурсії: "))
    koch_snowflake(200, level)
    turtle.done()


if __name__ == "__main__":
    main()
