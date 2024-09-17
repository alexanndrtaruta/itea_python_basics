# Task 4 Text Analyzer

def pre_processing(text_input):
    text_lower = text_input.lower()
    '''
        print(text_lower)
    '''
    for i in exclude_list_of_symbols:
        text_lower = text_lower.replace(i, ' ')
    '''
        print(text_lower, '\n')
    '''
    text_list = text_lower.split(' ')
    '''
        print(text_list)
    '''
    text_without_n = [i.replace('\n', ' ') for i in text_list]
    '''
        print(text_without_n)
    '''
    text_list_without_spaces = [i.strip() for i in text_without_n]
    '''
        print(text_list_without_spaces)
    '''

    # looks like shit
    for i in text_list_without_spaces:

        for j in i:
            j.split(' ')
    '''
        print(text_list_without_spaces, '\ncheck\n')
    '''
    text_list_without_empty_elements = [j for j in text_list_without_spaces if not j == '']
    '''
        print(text_list_without_empty_elements)

        print(len(text_list_without_empty_elements))
    '''
    text_without_excluding_words = [i for i in text_list_without_empty_elements if i not in exclude_list_of_words]
    '''
        print(text_without_excluding_words)
    '''
    text_list_without_small_words = [j for j in text_without_excluding_words if not len(j) < 4]

    return text_list_without_small_words


def calculate_words_quantity(filtered_list_text):
    return len(filtered_list_text)


def unique_words(filtered_list_text):
    unique_set = set(filtered_list_text)
    unique_list = list(unique_set)

    return len(unique_list)


def dictionary_of_words(list_of_words):
    dict_of_words = {i: list_of_words.count(i) for i in list_of_words}

    return dict_of_words


def keywords(some_dictionary):
    keywords_list = {(i, j) for j, i in some_dictionary.items()}
    return max(keywords_list)[1]


def frequency_for_each_word(dictionary):
    for i, j in dictionary.items():
        dictionary[i] = f'{int(j / len(dictionary) * 100)} %'

    return dictionary

    # frequency = [i, j / len(dictionary) * 100 for i in dictionary.items()]
    return frequency


text = "\nBUCK did not read the newspapers, or he would have known that\n" \
       "trouble was brewing, not alone for himself, but for every tide-\n" \
       "water dog, strong of muscle and with warm, long hair, from\n" \
       "Puget Sound to San Diego. Because men, groping in the Arctic darkness,\n" \
       "had found a yellow metal, and because steamship and transportation\n" \
       "companies were booming the find, thousands of men were rushing into\n" \
       "the Northland. These men wanted dogs, and the dogs they wanted were\n" \
       "heavy dogs, with strong muscles by which to toil, and furry coats to\n" \
       "protect them from the frost."

print(f'\nThe part of the text \n{text}')

exclude_list_of_symbols = ['.', ',', '!', '?', ':', ';', '\'', '\"', '-']
exclude_list_of_words = ['as' 'a', 'an', 'to', 'is', 'are', 'was', 'were',
                         'will', 'would', 'could', 'and', 'or', 'if', 'he',
                         'she', 'it', 'this', 'my', 'did', 'not', 'the',
                         'have', 'had', 'for', 'but', 'with']

print(f'\nThe number of words in text is:  {calculate_words_quantity(pre_processing(text))}')
print(f'\nThe number of unique words in text is:  {unique_words(pre_processing(text))}'
      f'\n\nThe text dictionary:\n\n{", ".join(list(set(pre_processing(text))))}')
print(f'\nKeywords:\n\n{keywords(dictionary_of_words(pre_processing(text)))}')
print(f'\nFrequency:{frequency_for_each_word(dictionary_of_words(pre_processing(text)))}\n')