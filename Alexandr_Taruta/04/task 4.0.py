import operator
user_text_to_analyze = input('Enter text to want to analyze:').lower()
'''A list of characters that are not taken into account in the analysis'''
not_analyze_list = ['a', 'as', 'an', 'to', 'is', 'are', 'was', 'were', 'will', 'would', 'could',
                    'and', 'or', 'if', 'he', 'she', 'it', 'this', 'my', 'i']

'''We get rid of signs of pinning'''
clear_string_to_analyze = ''.join(i for i in user_text_to_analyze if i not in ('!', '.', ':', ','))

list_to_analyze = list(clear_string_to_analyze.split())
clear_list_to_analyze = []
for i in list_to_analyze:
    if i not in not_analyze_list:
        clear_list_to_analyze.append(i)


def words_count(text):
    """This function counts the number of words in the analyzed text.
    :param text: user text to count the words in it
    :type text: list
    :return returns words count
    :rtype: int
    """

    counter = 0
    for i in text:
        if i not in not_analyze_list:
            counter += 1

    return print('Words quantity:', counter)


def unique_words(text):
    """This function returns list of unique words in analyzed text
    :param text: analyzed text
    :type text: list
    :return: returns a list of unique words
    :rtype: list
    """

    list_of_words = []
    str_to_output = ' '
    for i in text:
        if i not in list_of_words and i not in not_analyze_list:
            list_of_words.append(i)
    return print('Text dictionary: ', str_to_output.join(list_of_words))


def key_words(text):
    """This function returns the top 3 frequently used words in the analyzed text
    ::param text: analyzed text
    :type text: list
    :return: top 3 frequently used words
    :rtype: dict
    """
    new_dict = dict.fromkeys(clear_list_to_analyze, 0)
    for i in list_to_analyze:
        if i not in not_analyze_list:
            new_dict[i] += 1
    new_dict = sorted(new_dict.items(), key=operator.itemgetter(1), reverse=True)
    return print('Keywords:', new_dict[0], new_dict[1], new_dict[2])


def frequency_word(text):
    """This function considers the percentage of use of each word in the text
    ::param text: analyzed text
    :type text: list
    :return: word frequency
    :rtype: dict
    """
    new_dict = dict.fromkeys(clear_list_to_analyze,0)
    for i in clear_list_to_analyze:
        if i not in not_analyze_list:
            new_dict[i] += 1
    for i in new_dict:
        new_dict[i] = round(new_dict[i] / len(clear_list_to_analyze) * 100)
    return print('Frequency:', new_dict)


words_quantity = words_count(clear_list_to_analyze)
text_dictionary = unique_words(clear_list_to_analyze)
top_3_words = key_words(clear_list_to_analyze)
frequency = frequency_word(clear_list_to_analyze)


