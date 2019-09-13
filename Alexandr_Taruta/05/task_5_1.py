def add():
    x = int(input('Enter first number: '))
    y = int(input('Enter second: '))
    try:
        result = x + y

    except ValueError:
        print('Enter number not str')

    return result


if __name__ == "__main__":
    with open("task5.txt", "w") as f:
        f.write(f"{str(sum_two_numbers())}\n")
