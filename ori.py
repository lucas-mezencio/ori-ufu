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
