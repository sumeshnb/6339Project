"""
Reference: http://streamhacker.com/2010/05/10/text-classification-sentiment-analysis-naive-bayes-classifier/
"""
import nltk
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
 
def word_feats(words):
    return dict([(word, True) for word in words])
 
negids = movie_reviews.fileids('neg')
posids = movie_reviews.fileids('pos')
 
negfeats = [(word_feats(movie_reviews.words(fileids=[f])), 'neg') for f in negids]
posfeats = [(word_feats(movie_reviews.words(fileids=[f])), 'pos') for f in posids]

negcutoff = int(len(negfeats))
poscutoff = int(len(posfeats))
 
trainfeats = negfeats[:negcutoff] + posfeats[:poscutoff]
print ('train on ',len(trainfeats),'instances')
 
classifier = NaiveBayesClassifier.train(trainfeats)
f = open('D:\\books\\semester 5\\Special topics in advanced DB\\project\\cv000_29590.txt','r')

sentence = []
count = 0
posCount = 0
negCount = 0
output = []
for line in f:
    count = count + 1
    sentence = []
    a = line.split(' ')
    for i in a:
        sentence.append(i)
    result = classifier.classify(word_feats(sentence))
    if result == 'pos':
        posCount = posCount + 1
    else:
        negCount = negCount + 1
    string = line + ': ' + result
    output.append(string)
    #print('Line ',count,': ',result)
f.close()
print("Total Tweets:",count,",Positive tweets:",posCount,",and Negative tweets: ",negCount)
f = open('D:\\books\\semester 5\\Special topics in advanced DB\\project\\result.txt','a')
for out in output:
    out = str(out)
    f.write(out)
    f.write('\n')
f.flush()
f.close()
