# string unidecode python
# https://www.digitalocean.com/community/tutorials/how-to-import-modules-in-python-3
# https://www.treinaweb.com.br/blog/manipulando-arquivos-com-python
# https://www.w3schools.com/python/python_arrays.asp


from unidecode import unidecode
import ori
import file

input_str = file.get_text("input_files/input_text1.txt")

vocabulary = ori.get_vocabulary(input_str)

file.write_text_file("output_files/output_01.txt", vocabulary)

for word in vocabulary:
    print(unidecode(word))
