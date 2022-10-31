# 3. Написать функцию,
# аргументы имена сотрудников, возвращает словарь, 
# ключи — первые буквы имён, 
# значения — списки, содержащие имена,
# начинающиеся с соответствующей буквы.

from platform import architecture


def thesaurus(*args):
    names_dict={}
    for i in sorted(args):
        letter=i[0]
        if letter in names_dict:
           names_dict[letter]+=[i]
        else:
            names_dict[letter]=[i]
    return names_dict

print (thesaurus("Астер" , "Иван" , "Нина" , "Белла" ,"Шон" , "Вова" ))       