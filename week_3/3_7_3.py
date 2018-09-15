# Простейшая система проверки орфографии основана на использовании списка известных слов. Каждое слово в проверяемом тексте ищется в этом 
# списке и, если такое слово не найдено, оно помечается, как ошибочное.

# Напишем подобную систему.

# Через стандартный ввод подаётся следующая структура: первой строкой — количество d
# записей в списке известных слов, после передаётся  d строк с одним словарным словом на строку, затем — количество l строк текста, после 
# чего — l строк текста.

# Напишите программу, которая выводит слова из текста, которые не встречаются в словаре. Регистр слов не учитывается. 
# Порядок вывода слов произвольный. Слова, не встречающиеся в словаре, не должны повторяться в выводе программы.

dict = []
d  = int(input())
for i in range(d):
    s = input().lower()
    if s not in dict:
        dict.append(s)
list = []
l = int(input())
for j in range(l):
    s1 = [word.lower() for word in input().split()]
    for word in s1:
        if word not in dict:
            list.append(word)
list1 = set(list)
for word in list1:
    print(word)