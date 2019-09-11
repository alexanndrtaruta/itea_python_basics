def checker():

    """
    Function for numbers addiction
    :return num_sum: the first number plus the second number
    :rtype: int
    """

    while True:

        try:

            num_1 = int(input(' Enter the first number : '))
            num_2 = int(input(' Enter the second number : '))

        except ValueError as ERROR:

            print('Error : ')
            print(ERROR)
            continue

        num_sum = num_1 + num_2
        return (num_sum)
