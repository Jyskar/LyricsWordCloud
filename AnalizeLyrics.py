import nltk
import heapq

words = {}
f = open("Lyrics.txt", "r")
line = f.readline()
tokens = nltk.word_tokenize(line)
found = tokens[0]
out_of = tokens[1]
line = f.readline()
while line:
    tokens = nltk.word_tokenize(line)
    for word in tokens:
        if word.upper() not in words:
            words[word.upper()] = 1
        else:
            words[word.upper()] += 1
    line = f.readline()
print("Found lyrics for "+str(found)+" out of "+str(out_of)+".")
print(words)
f.close()

ordered = heapq.nlargest(500, words, key=lambda k: words[k])
print(ordered)

