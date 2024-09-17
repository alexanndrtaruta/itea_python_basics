def sum_two_integers(first, second):

    """
    This function converts two values to integers and sums its
    :param first:
    :param second:
    :type first: str
    :type second: str
    :return result: Sum of two integers
    :rtype result: int
    """

    result = ''

    try:

        first_integer = int(first)
        second_integer = int(second)

    except ValueError:

        print('You entered not an integer!')

    else:

        result = first_integer + second_integer

    return result


if __name__ == '__main__':
    first_value = input('Enter first value: \n')
    second_value = input('Enter second value: \n')
    summing_result = sum_two_integers(first_value, second_value)
    print(summing_result)

    with open('yevhen_makar_summing_result.txt', 'a+') as file:
        file.write(str(summing_result) + '\n')