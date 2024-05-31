word = input().upper()

set_word = set(word)
lst_word = list(word)
print(set_word)
dict_word = {}

for i in set_word:
    dict_word[f"{i}"] = lst_word.count(i)
print(dict_word)
