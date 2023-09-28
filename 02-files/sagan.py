import string

file = open("carl_sagan.txt")

text = file.read()

print(text)

# Remove punctuation
for ch in string.punctuation:
    text = text.replace(ch, '')
# Set all text to lower case
text = text.lower()

words = text.split(' ')
print(words)
print("No of words: ", len(words))

# Find how many occurrences of each word we have
occurrences = {}
for w in words:
    if w in occurrences:
        occurrences[w] += 1
    else:
        occurrences[w] = 1

for key in occurrences:
    print(key + ": " + str(occurrences[key]))






