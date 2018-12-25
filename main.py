from wordcloud import WordCloud

f = open("lyrics.txt", "r")
text = f.read()
wordcloud = WordCloud(width=1920, height=1080, margin=0, max_words=250, scale=2).generate(text)

import matplotlib.pyplot as plt
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")

# lower max_font_size
wordcloud = WordCloud(width=1920, height=1080, margin=0, max_words=250, max_font_size=400, scale=2).generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.plot(10,10)
plt.savefig("wordcloud.svg")
plt.show()
