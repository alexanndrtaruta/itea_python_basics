from yevhen_makar_sum_two_integers import sum_two_integers

while True:

    decision = input('Do you want sum integers? Write down "yes" or "no": ')

    if decision == 'yes':
        summing_result = sum_two_integers(input('Enter first value: \n'), input('Enter second value: \n'))

        with open('yevhen_makar_summing_result.txt', 'a+') as file:
            file.write(str(summing_result) + '\n')

    elif decision == 'no':
        break

print('First method: ')

with open('yevhen_makar_summing_result.txt') as file:
    print(file.read())

print('------------------------')


print('Second method: ')

with open('yevhen_makar_summing_result.txt') as file:
    for i in file:
        print(i.rstrip())

print('------------------------')


print('Third method: ')

with open('yevhen_makar_summing_result.txt') as file:
    numbers_list = file.readlines()

for i in numbers_list:
    print(i.rstrip())

print('------------------------')