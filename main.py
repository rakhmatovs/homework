
# #1
# def capitalize(names):
#     return names.title()
#
#
# names = ['alfred', 'tabitha', 'william', 'arla']
# print(list(map(capitalize, names)))

#2


# def filter_number(scores):
#     return scores > 75
#
#
# scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# print(list(filter(filter_number,scores)))

#3

# def word_palindrom(words):
#     if words.lower() == words[::-1].lower():
#         return True
#     return False
#
# words = ['Anna', 'Alexey', 'Alla', 'Kazak', 'Dom']
# print(list(filter(word_palindrom, words)))

#4
# def lens(word):
#     return len(word)
# lst =  ('apple', 'banana', 'cherry')
# print(list(map(lens, lst)))


#5

def lst3(word1, word2):
    return word1 + word2


lst1 = ['apple', 'banana', 'cherry']
lst2 =  ['orange', 'lemon', 'pineapple']
print(list(map(lst3,lst1,lst2)))




