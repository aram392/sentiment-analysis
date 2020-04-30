import pickle

#how to load model
f = open('MultinomialNB.pickle', 'rb')
MultinomialNB = pickle.load(f)
f.close()

f = open('CountVectorizer.pickle', 'rb')
CV = pickle.load(f)
f.close()

#how to use model for prediction

print(MultinomialNB.predict(CV.transform(["Buy Calls"])))