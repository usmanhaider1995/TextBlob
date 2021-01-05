from textblob import TextBlob
from textblob import Word
import nltk
nltk.download('punkt')
nltk.download('wordnet')


#getting correct sentences
words = ['Machin','Learnin','corect']
corrected_words = []
for i in words:
    corrected_words.append(TextBlob(i))
print('worng words :', words)
print('Corrected words :')
for i in corrected_words:
    print(i.correct())
 
# Getting sentiment analysis
test = TextBlob('Usman is a great machine learning developer and also have some cloud knowledge')
print(test.sentiment)
print('Polarity :',test.sentiment.polarity)

# Add space before dot inorder to get in as a sentence
token = TextBlob("Usman is a great machine learning. " 
                      "developer and also. "
                      "have some cloud knowledge.")
# printing seperate words and sentences
print('Word :',token.words)
print('Sentences', token.sentences)
# Getting sentiments of those sentences
print('Sentences sentiments ::')
for i in token.sentences:
    print(i.sentiment)

# Words singularization and pluralization

sentence = TextBlob('we bought 5 tomatos from shop today')
print(sentence.words[5].pluralize())
print(sentence.words[3].singularize())
#for i in sentence.words:
#    print(i)

# correcting nouns

word = Word('speling')
print(word.correct())

zen =TextBlob('beautiful is better')
print(zen.upper())







