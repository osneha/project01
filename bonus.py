f = open("shorttext.txt", "r")

with open('shorttext.txt') as f:
    words = f.readlines()
count = 0

for word in words:
    count =+1
print(f'word {count}: {word}') 

print('\nNumber of unique words:', len(words))

f.close()
