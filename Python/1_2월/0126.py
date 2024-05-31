word = input().upper()

# print(word)

set_word = set(word)
lst_word = list(word)
dict_word = {}

for i in set_word:
    dict_word[f"{i}"] = lst_word.count(i)

lst = []

for j in dict_word.values():
    lst.append(int(j))

# print(dict_word)

a = max(lst)

# print(a)

# print(lst.count(4))

if lst.count(a) > 1:
    print("?")
else:
    for key, value in dict_word.items():
        if value == a:
            print(key)
