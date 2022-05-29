from unidecode import unidecode


def get_vocabulary(input_str):
    decoded_string = decode_string(input_str)
    str_arr = decoded_string.lower().replace(',', '').replace('\n', ' ').split(' ')
    str_arr.sort()

    # remove os elementos duplicados preservando a ordem original (pós sorted())
    vocabulary = list(dict.fromkeys(str_arr))
    return vocabulary


def decode_string(input_str):
    return unidecode(input_str)


def get_bag_representation(vocabulary, doc_words):
    bag = [0] * len(vocabulary)
    for v_index, v_word in enumerate(vocabulary):
        for d_word in doc_words:
            if v_word == d_word:
                bag[v_index] = 1
                break
    return bag
