print("")
print("example of creating country codes")
print("")
country_codes = {'Finland': 'fi', 'South Africa':'za', 'Nepal': 'np' }
print(country_codes)
print(len(country_codes))

if country_codes:
    print("country_codes is not empty")
else:
    print("country_codes is empty")

country_codes.clear()
if country_codes:
    print("country_codes is not empty")
else:
    print("country_codes is empty        #after using function .clear()")
print("")

print("Example of iterating dictionary")
print("")
days_per_month = {'January': 31, 'Feburary': 28, 'March': 31}
print(days_per_month)
print("")

for month, days in days_per_month.items():
    print(f'{month} has {days} days')
print("")

print("Examples of basic dictionary operations")
print("")
roman_numerals = {'I':1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5}
print(roman_numerals)
print("")
print(roman_numerals['V'])
roman_numerals['X'] = 10
print(roman_numerals)
roman_numerals['L'] = 50
print(roman_numerals)

print("")

del roman_numerals['III']
print(roman_numerals, "     #deleting III")

print(roman_numerals.pop('X'), "   #using pop X")
print("")

print(roman_numerals.get('III', 'III is not in dictonary'))
print("")

print("example using in and not in")
print("")
if 'V' in roman_numerals:
    print("True")
else:
    print("False")
if 'III' in roman_numerals:
    print("True")
else:
    print("False")
if 'V' not in roman_numerals:
    print("True")
else:
    print("False")
print("")


print("example using method keys and values")
print("")
month = {'January': 1, 'Feburary': 2, 'March': 3}
for month_name in month.keys():
    print(month_name, end=' ')
print("")
for month_number in month.values():
    print(month_number, end=' ')

print("")
print("#using views")
print("")
month_views = month.keys()
for keys in month_views:
    print(keys, end=" ")

print("")

print("adding new key-value pair")
month['December'] = 12

print(month)
print("")

print("example of converting dictionary key-value into list")
print("")
print(list(month.keys()))
print(list(month.values()))
print(list(month.items()))
print("")

print("Compairing dictionary")
print("")

country_capitals1 = {'Belgium': 'Brussels','Haiti': 'Port-au-Prince'}
country_capitals2 = {'Nepal': 'Kathmandu','Uruguay': 'Montevideo'}
country_capitals3 = {'Haiti': 'Port-au-Prince','Belgium': 'Brussels'}

if country_capitals1 == country_capitals2:
    print("True")
else:
    print("False")

if country_capitals1 == country_capitals3:
    print("True")
else:
    print("False")

if country_capitals1 != country_capitals2:
    print("True")
else:
    print("False")

print("")
print("example using word count")
print("")

# fig06_02.py
"""Tokenizing a string and counting unique words."""
text = ('this is sample text with several words '        'this is more sample text with some different words')
word_counts = {}

for word in text.split():
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1
print(f'{"word":<12}count')

for word, count in sorted(word_counts.items()):
    print(f'{word:<12}{count}')
print('\nNumber of unique words:', len(word_counts))

print("")

modified_text = ("But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born and I will give you a complete account of the system, and expound the actual teachings of the great explorer of the truth, the master-builder of human happiness. No one rejects, dislikes, or avoids pleasure itself, because it is pleasure, but because those who do not know how to pursue pleasure rationally encounter consequences that are extremely painful. Nor again is there anyone who loves or pursues or desires to obtain pain of itself, because it is pain, but because occasionally circumstances occur in which toil and pain can procure him some great pleasure. To take a trivial example, which of us ever undertakes laborious physical exercise, except to obtain some advantage from it? But who has any right to find fault with a man who chooses to enjoy a pleasure that has no annoying consequences, or one who avoids a pain that produces no resultant pleasure?")
word_counts2 = {}

for word2 in modified_text.split():
    if word2 in word_counts2:
        word_counts2[word2] += 1
    else:
        word_counts2[word2] = 1
print(f'{"word":<12}count')

for word2, count2 in sorted(word_counts2.items()):
    print(f'{word2:<12}{count2}')
print('\nNumber of unique words:', len(word_counts2))

print("")

print("Example with sets")
print("")

colors = {'red', 'orange', 'yellow', 'green', 'red', 'blue'}
print(colors)

print(len(colors))

if 'red' in colors:
    print("True")
else:
    print("False")

if 'purple' in colors:
    print("True")
else:
    print("False")

if 'purple' not in colors:
    print("True")
else:
    print("False")

print("")

for color in colors:
    print(color.upper(), end= ' ')

print("")

print("example of builtin fuction in set")
print("")

number_s = list(range(10)) + list(range(5))
print(number_s)
print("")

print(set(number_s))
print("")
