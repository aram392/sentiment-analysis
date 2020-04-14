from textblob import TextBlob
sentence = TextBlob("i love dogs. They are family to me")
print(sentence.sentiment.polarity)