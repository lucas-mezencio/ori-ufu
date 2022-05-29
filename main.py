# github repo: https://github.com/lucas-mezencio/ori-ufu
# colab link: https://colab.research.google.com/drive/1tVGJCSZvFmyX3DGjWOm9S51d20qzCQc7?usp=sharing


# string unidecode python
# https://www.digitalocean.com/community/tutorials/how-to-import-modules-in-python-3
# https://www.treinaweb.com.br/blog/manipulando-arquivos-com-python
# https://www.w3schools.com/python/python_arrays.asp


import ori
import file

print("==============================")
print("        EXERCICIO 1           ")
print("==============================")

input_str = file.get_text("io_files/input_text1.txt")

vocabulary = ori.get_vocabulary(input_str)

file.write_text_file("io_files/output_01.txt", vocabulary)

print(vocabulary)

print("==============================")
print("        EXERCICIO 2           ")
print("==============================")

# o arquivo de input do ex2 é o mesmo do output do ex1, que está salvo na variável "vocabulary"
doc_two_words = ori.get_vocabulary(file.get_text("io_files/input_text2.txt"))
bag = ori.get_bag_representation(vocabulary, doc_two_words)

print(bag)
file.write_singleline_file("io_files/output_02.txt", str(bag))
