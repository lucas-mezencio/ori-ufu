# https://www.treinaweb.com.br/blog/manipulando-arquivos-com-python
def get_text(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    text = ""
    for line in lines:
        text += line
    return text


def write_text_file(filename, str_list):
    file = open(filename, 'a')
    for word in str_list:
        file.write(word + "\n")
