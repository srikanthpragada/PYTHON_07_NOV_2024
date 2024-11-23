# Word Frequency

st = "how do you do today, how did you do yesterday"
words = st.split(' ')

word_freq = {}
for w in set(words):
    word_freq[w] = words.count(w)

print(word_freq)


