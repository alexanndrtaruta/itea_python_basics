from Kahanovskyi_5_1 import checker

check_sum = str(checker())

with open('file_5_1.txt', 'w') as file:

    file.write(check_sum)  # write in file result of addiction

with open('file_5_1.txt', 'r') as file_read:

    text = file_read.read()

with open('file_5_1.txt', 'r') as file_read:

    for i in file_read:

        print(i)# reading file 2

with open('file_5_1.txt', 'r') as file_read:

    list_text = file_read.readlines()

print(text)# reading file 1
print(list_text) # reading file 3





