def run():
    # squares = []
    # for i in range (1, 101):
    #     if i % 3 != 0:
    #         squares.append(i**2)

    # print(squares)
    squares = [i for i in range(1, 10000) if i % 36 == 0 and len(str(i)) < 6]
    print(squares)


if __name__ == "__main__":
    run()